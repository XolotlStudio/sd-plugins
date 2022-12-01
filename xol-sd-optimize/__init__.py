from functools import partial
import sys
import os
import weakref

import sd
from sd.tools import graphlayout
import sd.api as api
from sd.api.sdproperty import SDPropertyCategory

from PySide2 import QtCore, QtGui, QtWidgets, QtSvg


def equal_parm(type, a, b):
    if type == 'SDTypeBool' or type == 'SDTypeDouble' or type == 'SDTypeFloat' or type == 'SDTypeInt' or type == 'SDTypeString':
        return a == b
    elif type == 'SDTypeBool2' or type == 'SDTypeDouble2' or type == 'SDTypeFloat2' or type == 'SDTypeInt2':
        return a.x == b.x and a.y == b.y
    elif type == 'SDTypeBool3' or type == 'SDTypeDouble3' or type == 'SDTypeFloat3' or type == 'SDTypeInt3':
        return a.x == b.x and a.y == b.y and a.z == b.z
    elif type == 'SDTypeBool4' or type == 'SDTypeDouble4' or type == 'SDTypeFloat4' or type == 'SDTypeInt4':
        return a.w == b.w and a.x == b.x and a.y == b.y and a.z == b.z
    elif type == 'SDTypeColorRGB':
        return a.r == b.r and a.g == b.g and a.b == b.b
    elif type == 'SDTypeColorRGBA':
        return a.r == b.r and a.g == b.g and a.b == b.b and a.a == b.a
    elif type == 'SDTypeEnum':
        return a == b
    else:
        return False


def loadSvgIcon(iconName, size):
    currentDir = os.path.dirname(__file__)
    iconFile = os.path.abspath(os.path.join(currentDir, iconName + '.svg'))

    svgRenderer = QtSvg.QSvgRenderer(iconFile)
    if svgRenderer.isValid():
        pixmap = QtGui.QPixmap(QtCore.QSize(size, size))

        if not pixmap.isNull():
            pixmap.fill(QtCore.Qt.transparent)
            painter = QtGui.QPainter(pixmap)
            svgRenderer.render(painter)
            painter.end()

        return QtGui.QIcon(pixmap)

    return None


class NodeOptimizeToolBar(QtWidgets.QToolBar):
    __toolbarList = {}

    def __init__(self, graphViewID, uiMgr):
        super(NodeOptimizeToolBar, self).__init__(parent=uiMgr.getMainWindow())

        self.setObjectName("xolotl.com.node_optimize_toolbar")

        self.__graphViewID = graphViewID
        self.__uiMgr = uiMgr

        act = self.addAction(loadSvgIcon("optimize", DEFAULT_ICON_SIZE), "Optimize")
        act.setShortcut(QtGui.QKeySequence('Shift+O'))
        act.setToolTip(self.tr("Optimize the nodes"))
        act.triggered.connect(self.__onOptimizeNodes)

        self.__toolbarList[graphViewID] = weakref.ref(self)
        self.destroyed.connect(partial(NodeOptimizeToolBar.__onToolbarDeleted, graphViewID=graphViewID))

    def tooltip(self):
        return self.tr("Optimize")

    def __onOptimizeNodes(self):
        nodes = self.__getSelectedNodes()
        graph = self.__getCurrentGraph()

        if len(nodes) == 0:
            nodes = graph.getNodes()

        # Group Nodes by Type
        ordered_nodes = {}
        for node in nodes:
            if node.getDefinition().getLabel() not in ordered_nodes:
                ordered_nodes[node.getDefinition().getLabel()] = []
            ordered_nodes[node.getDefinition().getLabel()].append(node)

        # Order nodes by graph position
        for key in ordered_nodes:
            first_node = ordered_nodes[key][0]
            ordered_nodes[key].sort(key=lambda x: x.getPosition().x, reverse=False)

        for key in ordered_nodes:

            for idx in range(0, len(ordered_nodes[key])):
                base = ordered_nodes[key][idx]
                parm_names = []
                has_inputs = False
                for parm in base.getProperties(SDPropertyCategory.Input):
                    if not parm.isConnectable():
                        parm_names.append(parm.getId())
                    else:
                        has_inputs = True

                if not has_inputs:
                    for jdx in range(idx, len(ordered_nodes[key])):
                        node = ordered_nodes[key][jdx]
                        if node is not base:
                            equal = True
                            for parm in parm_names:
                                type = base.getPropertyFromId(parm, SDPropertyCategory.Input).getType().getClassName()
                                a = base.getPropertyValueFromId(parm, SDPropertyCategory.Input).get()  if base.getPropertyValueFromId(parm, SDPropertyCategory.Input) is not None else None
                                b = node.getPropertyValueFromId(parm, SDPropertyCategory.Input).get() if node.getPropertyValueFromId(parm, SDPropertyCategory.Input) is not None else None
                                base_prop = base.getPropertyFromId(parm, SDPropertyCategory.Input)
                                node_prop = node.getPropertyFromId(parm, SDPropertyCategory.Input)

                                if a is None or b is None:
                                    type = None

                                if not equal_parm(type, a, b) or base.getPropertyInheritanceMethod(base_prop) != node.getPropertyInheritanceMethod(node_prop):
                                    equal = False
                            if equal:
                                # Connect to base
                                for p in node.getProperties(SDPropertyCategory.Output):
                                    if p.isConnectable():
                                        conns = node.getPropertyConnections(p)
                                        for conn in conns:
                                            input_node = conn.getInputPropertyNode()
                                            input_prop = conn.getInputProperty()
                                            output_prop = conn.getOutputProperty()
                                            base.newPropertyConnectionFromId(output_prop.getId(), input_node, input_prop.getId())
                                # Delete Node
                                graph.deleteNode(node)



    def __getSelectedNodes(self):
        return self.__uiMgr.getCurrentGraphSelectionFromGraphViewID(self.__graphViewID)

    def __getCurrentGraph(self):
        return self.__uiMgr.getGraphFromGraphViewID(self.__graphViewID)

    @classmethod
    def __onToolbarDeleted(cls, graphViewID):
        del cls.__toolbarList[graphViewID]

    @classmethod
    def removeAllToolbars(cls):
        for toolbar in cls.__toolbarList.values():
            if toolbar():
                toolbar().deleteLater()


DEFAULT_ICON_SIZE = 24
graphViewCreatedCallbackID = 0


def onNewGraphViewCreated(graphViewID, uiMgr):
    toolbar = NodeOptimizeToolBar(graphViewID, uiMgr)
    uiMgr.addToolbarToGraphView(
        graphViewID,
        toolbar,
        icon=loadSvgIcon("optimize", DEFAULT_ICON_SIZE),
        tooltip=toolbar.tooltip())


def initializeSDPlugin():
    ctx = sd.getContext()
    app = ctx.getSDApplication()
    uiMgr = app.getQtForPythonUIMgr()

    if uiMgr:
        global graphViewCreatedCallbackID
        graphViewCreatedCallbackID = uiMgr.registerGraphViewCreatedCallback(
            partial(onNewGraphViewCreated, uiMgr=uiMgr))


def uninitializeSDPlugin():
    ctx = sd.getContext()
    app = ctx.getSDApplication()
    uiMgr = app.getQtForPythonUIMgr()

    if uiMgr:
        global graphViewCreatedCallbackID
        uiMgr.unregisterCallback(graphViewCreatedCallbackID)
        NodeAlignmentToolBar.removeAllToolbars()
