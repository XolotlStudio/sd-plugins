import os
import sd

from  sd.api.sdvalueint import SDValueInt
from  sd.api.sdvalueint2 import SDValueInt2
from  sd.api.sdvalueint3 import SDValueInt3
from  sd.api.sdvalueint4 import SDValueInt4
from sd.api.sdvaluefloat import SDValueFloat
from sd.api.sdvaluefloat2 import SDValueFloat2
from sd.api.sdvaluefloat3 import SDValueFloat3
from sd.api.sdvaluefloat4 import SDValueFloat4
from sd.api.sdvaluebool import SDValueBool
from sd.api.sdvaluebool2 import SDValueBool2
from sd.api.sdvaluebool3 import SDValueBool3
from sd.api.sdvaluebool4 import SDValueBool4
from sd.api.sdtypeenum import SDTypeEnum

from sd.api.sdbasetypes import int2, int3, int4, float2, float3, float4, bool2, bool3, bool4

from sd.api.sdproperty import SDPropertyInheritanceMethod

from PySide2.QtCore import Qt
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QVBoxLayout, QWidget, QSlider, QLabel


class NoneUI(QWidget):

    def __init__(self):
        super(NoneUI, self).__init__()
        self.__loadUI()

    def __loadUI(self):
        __currdir__ = os.path.dirname(__file__)
        uiPath = os.path.join(__currdir__,"ui/none.ui")
        self.widget = QUiLoader().load(uiPath)
        self.lyt_main = QVBoxLayout()
        self.setLayout(self.lyt_main)
        self.lyt_main.addWidget(self.widget)


    def __valueChanged(self):
        self.widget.chk_value.setChecked(True)

    def setValue(self, prop):
        self.widget.lbl_name.setText(prop['label'])
        self.widget.lbl_info.setText("Value type [" + prop['type'] + "] is not supported yet")

    def getValue(self):
        return None

class IntUI(QWidget):

    def __init__(self):
        super(IntUI, self).__init__()
        self.__loadUI()

    def __loadUI(self):
        __currdir__ = os.path.dirname(__file__)
        uiPath = os.path.join(__currdir__,"ui/int.ui")
        self.widget = QUiLoader().load(uiPath)
        self.lyt_main = QVBoxLayout()
        self.setLayout(self.lyt_main)
        self.lyt_main.addWidget(self.widget)

        self.widget.txt_value.valueChanged.connect(self.__valueChanged)
        self.widget.cmb_inheritance.currentIndexChanged.connect(self.__valueChanged)

    def __valueChanged(self):
        self.widget.chk_value.setChecked(True)

    def setValue(self, prop):
        if prop["id"].find('$') != -1:
            self.widget.cmb_inheritance.show()
            self.widget.cmb_inheritance.setCurrentIndex(int(prop['inheritance']))
            self.widget.chk_value.setChecked(False)
        else:
            self.widget.cmb_inheritance.hide()
        self.widget.lbl_name.setText(prop['label'])
        self.widget.txt_value.setValue(int(prop['value']))
        self.widget.chk_value.setChecked(False)

    def getValue(self):
        if self.widget.chk_value.isChecked():
            return self.widget.txt_value.value()
        else:
            return None

    def getInheritance(self):
        return self.widget.cmb_inheritance.currentIndex()

    def setEnable(self, enable):
        self.widget.chk_value.setChecked(enable)


class Int2UI(QWidget):

    def __init__(self):
        super(Int2UI, self).__init__()
        self.__loadUI()

    def __loadUI(self):
        __currdir__ = os.path.dirname(__file__)
        uiPath = os.path.join(__currdir__,"ui/int2.ui")
        self.widget = QUiLoader().load(uiPath)
        self.lyt_main = QVBoxLayout()
        self.setLayout(self.lyt_main)
        self.lyt_main.addWidget(self.widget)

        self.widget.txt_value_x.valueChanged.connect(self.__valueChanged)
        self.widget.txt_value_y.valueChanged.connect(self.__valueChanged)
        self.widget.cmb_inheritance.currentIndexChanged.connect(self.__valueChanged)

    def __valueChanged(self):
        self.widget.chk_value.setChecked(True)

    def setValue(self, prop):
        if prop["id"].find('$') != -1:
            self.widget.cmb_inheritance.show()
            self.widget.cmb_inheritance.setCurrentIndex(int(prop['inheritance']))
            self.widget.chk_value.setChecked(False)
        else:
            self.widget.cmb_inheritance.hide()
        self.widget.lbl_name.setText(prop['label'])
        self.widget.txt_value_x.setValue(int(prop['value'].x))
        self.widget.txt_value_y.setValue(int(prop['value'].y))
        self.widget.chk_value.setChecked(False)

    def getValue(self):
        if self.widget.chk_value.isChecked():
            return int2(self.widget.txt_value_x.value(), self.widget.txt_value_y.value())
        else:
            return None

    def getInheritance(self):
        return self.widget.cmb_inheritance.currentIndex()

    def setEnable(self, enable):
        self.widget.chk_value.setChecked(enable)


class Int3UI(QWidget):

    def __init__(self):
        super(Int3UI, self).__init__()
        self.__loadUI()

    def __loadUI(self):
        __currdir__ = os.path.dirname(__file__)
        uiPath = os.path.join(__currdir__,"ui/int3.ui")
        self.widget = QUiLoader().load(uiPath)
        self.lyt_main = QVBoxLayout()
        self.setLayout(self.lyt_main)
        self.lyt_main.addWidget(self.widget)

        self.widget.txt_value_x.valueChanged.connect(self.__valueChanged)
        self.widget.txt_value_y.valueChanged.connect(self.__valueChanged)
        self.widget.txt_value_z.valueChanged.connect(self.__valueChanged)
        self.widget.cmb_inheritance.currentIndexChanged.connect(self.__valueChanged)

    def __valueChanged(self):
        self.widget.chk_value.setChecked(True)

    def setValue(self, prop):
        if prop["id"].find('$') != -1:
            self.widget.cmb_inheritance.show()
            self.widget.cmb_inheritance.setCurrentIndex(int(prop['inheritance']))
            self.widget.chk_value.setChecked(False)
        else:
            self.widget.cmb_inheritance.hide()
        self.widget.lbl_name.setText(prop['label'])
        self.widget.txt_value_x.setValue(int(prop['value'].x))
        self.widget.txt_value_y.setValue(int(prop['value'].y))
        self.widget.txt_value_z.setValue(int(prop['value'].z))
        self.widget.chk_value.setChecked(False)

    def getValue(self):
        if self.widget.chk_value.isChecked():
            return int3(self.widget.txt_value_x.value(), self.widget.txt_value_y.value(), self.widget.txt_value_z.value())
        else:
            return None

    def getInheritance(self):
        return self.widget.cmb_inheritance.currentIndex()

    def setEnable(self, enable):
        self.widget.chk_value.setChecked(enable)


class Int4UI(QWidget):

    def __init__(self):
        super(Int4UI, self).__init__()
        self.__loadUI()

    def __loadUI(self):
        __currdir__ = os.path.dirname(__file__)
        uiPath = os.path.join(__currdir__,"ui/int4.ui")
        self.widget = QUiLoader().load(uiPath)
        self.lyt_main = QVBoxLayout()
        self.setLayout(self.lyt_main)
        self.lyt_main.addWidget(self.widget)

        self.widget.txt_value_w.valueChanged.connect(self.__valueChanged)
        self.widget.txt_value_x.valueChanged.connect(self.__valueChanged)
        self.widget.txt_value_y.valueChanged.connect(self.__valueChanged)
        self.widget.txt_value_z.valueChanged.connect(self.__valueChanged)
        self.widget.cmb_inheritance.currentIndexChanged.connect(self.__valueChanged)

    def __valueChanged(self):
        self.widget.chk_value.setChecked(True)

    def setValue(self, prop):
        if prop["id"].find('$') != -1:
            self.widget.cmb_inheritance.show()
            self.widget.cmb_inheritance.setCurrentIndex(int(prop['inheritance']))
            self.widget.chk_value.setChecked(False)
        else:
            self.widget.cmb_inheritance.hide()
        self.widget.lbl_name.setText(prop['label'])
        self.widget.txt_value_w.setValue(int(prop['value'].w))
        self.widget.txt_value_x.setValue(int(prop['value'].x))
        self.widget.txt_value_y.setValue(int(prop['value'].y))
        self.widget.txt_value_z.setValue(int(prop['value'].z))
        self.widget.chk_value.setChecked(False)

    def getValue(self):
        if self.widget.chk_value.isChecked():
            return int4(self.widget.txt_value_w.value(), self.widget.txt_value_x.value(), self.widget.txt_value_y.value(), self.widget.txt_value_z.value())
        else:
            return None

    def getInheritance(self):
        return self.widget.cmb_inheritance.currentIndex()

    def setEnable(self, enable):
        self.widget.chk_value.setChecked(enable)


class FloatUI(QWidget):

    def __init__(self):
        super(FloatUI, self).__init__()
        self.__loadUI()

    def __loadUI(self):
        __currdir__ = os.path.dirname(__file__)
        uiPath = os.path.join(__currdir__,"ui/float.ui")
        self.widget = QUiLoader().load(uiPath)
        self.lyt_main = QVBoxLayout()
        self.setLayout(self.lyt_main)
        self.lyt_main.addWidget(self.widget)

        self.widget.txt_value.valueChanged.connect(self.__valueChanged)
        self.widget.cmb_inheritance.currentIndexChanged.connect(self.__valueChanged)

    def __valueChanged(self):
        self.widget.chk_value.setChecked(True)

    def setValue(self, prop):
        if prop["id"].find('$') != -1:
            self.widget.cmb_inheritance.show()
            self.widget.cmb_inheritance.setCurrentIndex(int(prop['inheritance']))
            self.widget.chk_value.setChecked(False)
        else:
            self.widget.cmb_inheritance.hide()
        self.widget.lbl_name.setText(prop['label'])
        self.widget.txt_value.setValue(float(prop['value']))
        self.widget.chk_value.setChecked(False)

    def getValue(self):
        if self.widget.chk_value.isChecked():
            return self.widget.txt_value.value()
        else:
            return None

    def getInheritance(self):
        return self.widget.cmb_inheritance.currentIndex()

    def setEnable(self, enable):
        self.widget.chk_value.setChecked(enable)


class Float2UI(QWidget):

    def __init__(self):
        super(Float2UI, self).__init__()
        self.__loadUI()

    def __loadUI(self):
        __currdir__ = os.path.dirname(__file__)
        uiPath = os.path.join(__currdir__,"ui/float2.ui")
        self.widget = QUiLoader().load(uiPath)
        self.lyt_main = QVBoxLayout()
        self.setLayout(self.lyt_main)
        self.lyt_main.addWidget(self.widget)

        self.widget.txt_value_x.valueChanged.connect(self.__valueChanged)
        self.widget.txt_value_y.valueChanged.connect(self.__valueChanged)
        self.widget.cmb_inheritance.currentIndexChanged.connect(self.__valueChanged)

    def __valueChanged(self):
        self.widget.chk_value.setChecked(True)

    def setValue(self, prop):
        if prop["id"].find('$') != -1:
            self.widget.cmb_inheritance.show()
            self.widget.cmb_inheritance.setCurrentIndex(int(prop['inheritance']))
            self.widget.chk_value.setChecked(False)
        else:
            self.widget.cmb_inheritance.hide()
        self.widget.lbl_name.setText(prop['label'])
        self.widget.txt_value_x.setValue(float(prop['value'].x))
        self.widget.txt_value_y.setValue(float(prop['value'].y))
        self.widget.chk_value.setChecked(False)

    def getValue(self):
        if self.widget.chk_value.isChecked():
            return float2(self.widget.txt_value_x.value(), self.widget.txt_value_y.value())
        else:
            return None

    def getInheritance(self):
        return self.widget.cmb_inheritance.currentIndex()

    def setEnable(self, enable):
        self.widget.chk_value.setChecked(enable)


class Float3UI(QWidget):

    def __init__(self):
        super(Float3UI, self).__init__()
        self.__loadUI()

    def __loadUI(self):
        __currdir__ = os.path.dirname(__file__)
        uiPath = os.path.join(__currdir__,"ui/float3.ui")
        self.widget = QUiLoader().load(uiPath)
        self.lyt_main = QVBoxLayout()
        self.setLayout(self.lyt_main)
        self.lyt_main.addWidget(self.widget)

        self.widget.txt_value_x.valueChanged.connect(self.__valueChanged)
        self.widget.txt_value_y.valueChanged.connect(self.__valueChanged)
        self.widget.txt_value_z.valueChanged.connect(self.__valueChanged)
        self.widget.cmb_inheritance.currentIndexChanged.connect(self.__valueChanged)

    def __valueChanged(self):
        self.widget.chk_value.setChecked(True)

    def setValue(self, prop):
        if prop["id"].find('$') != -1:
            self.widget.cmb_inheritance.show()
            self.widget.cmb_inheritance.setCurrentIndex(int(prop['inheritance']))
            self.widget.chk_value.setChecked(False)
        else:
            self.widget.cmb_inheritance.hide()
        self.widget.lbl_name.setText(prop['label'])
        self.widget.txt_value_x.setValue(float(prop['value'].x))
        self.widget.txt_value_y.setValue(float(prop['value'].y))
        self.widget.txt_value_z.setValue(float(prop['value'].z))
        self.widget.chk_value.setChecked(False)

    def getValue(self):
        if self.widget.chk_value.isChecked():
            return float3(self.widget.txt_value_x.value(), self.widget.txt_value_y.value(), self.widget.txt_value_z.value())
        else:
            return None

    def getInheritance(self):
        return self.widget.cmb_inheritance.currentIndex()

    def setEnable(self, enable):
        self.widget.chk_value.setChecked(enable)


class Float4UI(QWidget):

    def __init__(self):
        super(Float4UI, self).__init__()
        self.__loadUI()

    def __loadUI(self):
        __currdir__ = os.path.dirname(__file__)
        uiPath = os.path.join(__currdir__,"ui/float4.ui")
        self.widget = QUiLoader().load(uiPath)
        self.lyt_main = QVBoxLayout()
        self.setLayout(self.lyt_main)
        self.lyt_main.addWidget(self.widget)

        self.widget.txt_value_w.valueChanged.connect(self.__valueChanged)
        self.widget.txt_value_x.valueChanged.connect(self.__valueChanged)
        self.widget.txt_value_y.valueChanged.connect(self.__valueChanged)
        self.widget.txt_value_z.valueChanged.connect(self.__valueChanged)
        self.widget.cmb_inheritance.currentIndexChanged.connect(self.__valueChanged)

    def __valueChanged(self):
        self.widget.chk_value.setChecked(True)

    def setValue(self, prop):
        if prop["id"].find('$') != -1:
            self.widget.cmb_inheritance.show()
            self.widget.cmb_inheritance.setCurrentIndex(int(prop['inheritance']))
            self.widget.chk_value.setChecked(False)
        else:
            self.widget.cmb_inheritance.hide()
        self.widget.lbl_name.setText(prop['label'])
        self.widget.txt_value_w.setValue(float(prop['value'].w))
        self.widget.txt_value_x.setValue(float(prop['value'].x))
        self.widget.txt_value_y.setValue(float(prop['value'].y))
        self.widget.txt_value_z.setValue(float(prop['value'].z))
        self.widget.chk_value.setChecked(False)

    def getValue(self):
        if self.widget.chk_value.isChecked():
            return float4(self.widget.txt_value_w.value(), self.widget.txt_value_x.value(), self.widget.txt_value_y.value(), self.widget.txt_value_z.value(),)
        else:
            return None

    def getInheritance(self):
        return self.widget.cmb_inheritance.currentIndex()

    def setEnable(self, enable):
        self.widget.chk_value.setChecked(enable)


class BoolUI(QWidget):

    def __init__(self):
        super(BoolUI, self).__init__()
        self.__loadUI()
        self.__value = False

    def __loadUI(self):
        __currdir__ = os.path.dirname(__file__)
        uiPath = os.path.join(__currdir__,"ui/bool.ui")
        self.widget = QUiLoader().load(uiPath)
        self.lyt_main = QVBoxLayout()
        self.setLayout(self.lyt_main)
        self.lyt_main.addWidget(self.widget)

        self.widget.btn_value.clicked.connect(lambda:self.__btnValueClick(self.widget.btn_value))
        self.widget.cmb_inheritance.currentIndexChanged.connect(self.__valueChanged)

    def __btnValueClick(self, btn):
        self.__value = not self.__value
        if self.__value:
            btn.setText('True')
        else:
            btn.setText('False')
        self.__valueChanged()

    def __valueChanged(self):
        self.widget.chk_value.setChecked(True)

    def setValue(self, prop):
        if prop["id"].find('$') != -1:
            self.widget.cmb_inheritance.show()
            self.widget.cmb_inheritance.setCurrentIndex(int(prop['inheritance']))
            self.widget.chk_value.setChecked(False)
        else:
            self.widget.cmb_inheritance.hide()
        self.widget.lbl_name.setText(prop['label'])
        self.__value = prop['value']
        if self.__value:
            self.widget.btn_value.setText('True')
        else:
            self.widget.btn_value.setText('False')

    def getValue(self):
        if self.widget.chk_value.isChecked():
            return self.__value
        else:
            return None

    def getInheritance(self):
        return self.widget.cmb_inheritance.currentIndex()

    def setEnable(self, enable):
        self.widget.chk_value.setChecked(enable)


class EnumUI(QWidget):

    def __init__(self):
        super(EnumUI, self).__init__()
        self.__loadUI()

    def __loadUI(self):
        __currdir__ = os.path.dirname(__file__)
        uiPath = os.path.join(__currdir__,"ui/enum.ui")
        self.widget = QUiLoader().load(uiPath)
        self.lyt_main = QVBoxLayout()
        self.setLayout(self.lyt_main)
        self.lyt_main.addWidget(self.widget)

        self.widget.cmb_value.currentIndexChanged.connect(self.__valueChanged)
        self.widget.cmb_inheritance.currentIndexChanged.connect(self.__valueChanged)

    def __valueChanged(self):
        self.widget.chk_value.setChecked(True)

    def setValue(self, prop):
        if prop["id"].find('$') != -1:
            self.widget.cmb_inheritance.show()
            self.widget.cmb_inheritance.setCurrentIndex(int(prop['inheritance']))
            self.widget.chk_value.setChecked(False)
        else:
            self.widget.cmb_inheritance.hide()
        self.prop = prop
        self.widget.lbl_name.setText(prop['label'])
        self.widget.cmb_value.clear()
        # print(parm['label'], parm["enums"], parm["value"])
        for e in prop["enums"]:
            self.widget.cmb_value.addItem(e["label"])

        idx = 0
        for e in prop["enums"]:
            if e["value"] == prop['value']:
                self.widget.cmb_value.setCurrentIndex(idx)
            idx += 1
        self.widget.chk_value.setChecked(False)

    def getValue(self):
        if self.widget.chk_value.isChecked():
            idx = self.widget.cmb_value.currentIndex()
            return self.prop["enums"][idx]["value"]
        else:
            return None

    def getInheritance(self):
        return self.widget.cmb_inheritance.currentIndex()

    def setEnable(self, enable):
        self.widget.chk_value.setChecked(enable)


class MainUI(QWidget):
    def __init__(self, uiMgr):
        super(MainUI, self).__init__()
        self.uiMgr = uiMgr
        self.props = []
        self.__loadUI()

    def __loadUI(self):
        __currdir__ = os.path.dirname(__file__)
        uiPath = os.path.join(__currdir__,"ui/main.ui")
        self.widget = QUiLoader().load(uiPath)
        self.lyt_props = QVBoxLayout()
        self.lyt_props.setAlignment(Qt.AlignTop)
        self.lyt_props.setSpacing(0)
        self.widget.scr_parms.setLayout(self.lyt_props)

        self.widget.btn_load.clicked.connect(lambda:self.__btnLoadClick(self.widget.btn_load))
        self.widget.btn_set.clicked.connect(lambda:self.__btnSetClick(self.widget.btn_set))
        self.widget.btn_clear.clicked.connect(lambda:self.__btnClearClick(self.widget.btn_clear))

        self.widget.btn_enableAll.clicked.connect(lambda:self.__btnEnableClick(True))
        self.widget.btn_disableAll.clicked.connect(lambda:self.__btnEnableClick(False))

    def __btnEnableClick(self, enable):
        items = self.widget.scr_parms.findChildren(QWidget)
        for item in items:
            try:
                item.setEnable(enable)
            except:
                pass

    def __btnClearClick(self, btn):
        self.__clearProps()

    def __btnLoadClick(self, btn):
        self.__clearProps()
        self.__getProps()
        for prop in self.props:
            self.__initProp(prop)

    def __btnSetClick(self, btn):
        selection = self.uiMgr.getCurrentGraphSelection()

        for prop in self.props:
            value = self.__setProp(prop)
            for node in selection:
                if value is not None:
                    if prop["id"].find("$") > -1:
                        inheritance = SDPropertyInheritanceMethod.RelativeToInput
                        if prop['widget'].getInheritance() == 1 :
                            inheritance = SDPropertyInheritanceMethod.RelativeToParent
                        elif prop['widget'].getInheritance() == 2:
                            inheritance = SDPropertyInheritanceMethod.Absolute

                        node.setInputPropertyInheritanceMethodFromId(prop["id"], inheritance)

                    node.setInputPropertyValueFromId(prop["id"], value)

        graph = self.uiMgr.getCurrentGraph()
        graph.compute()

    def __clearProps(self):
        items = self.widget.scr_parms.findChildren(QWidget)
        for item in items:
            item.setParent(None)
            #TODO: add delete widget
        self.props = []

    def __getProps(self):
        try:
            graph = self.uiMgr.getCurrentGraph()
        except:
            print('ERROR: A graph must be open')
            return

        selection = self.uiMgr.getCurrentGraphSelection()
        if len(selection) < 2:
            print("ERROR: Select at least two nodes")
            return

        for prop in selection[0].getProperties(sd.api.sdproperty.SDPropertyCategory.Input):
            if not prop.isConnectable():
                exist = 1
                for idx in range(1, len(selection)):
                    item = selection[idx].getPropertyFromId(prop.getId(),sd.api.sdproperty.SDPropertyCategory.Input)
                    if item is not None and item.getType().getId() == prop.getType().getId():
                        exist += 1

                if exist == len(selection):
                    enums = []
                    value = selection[0].getInputPropertyValueFromId(prop.getId()).get()
                    type = prop.getType().getId()
                    if  isinstance(prop.getType(), SDTypeEnum):
                        opts = prop.getType().getEnumerators()
                        type = "enum"
                        for e in opts:
                            enums.append({"label":e.getLabel(),"value":e.getDefaultValue().get()})

                    if prop.getId().find("$") > -1:
                        inheritance = selection[0].getPropertyInheritanceMethod(prop)
                    else:
                        inheritance = None

                    inh = 0
                    if inheritance == SDPropertyInheritanceMethod.RelativeToParent :
                        inh = 1
                    elif inheritance == SDPropertyInheritanceMethod.Absolute:
                        inh = 2

                    self.props.append({
                        "id":prop.getId(),
                        "label":prop.getLabel(),
                        "type":type,
                        "value":value,
                        "enums":enums,
                        "inheritance":inh
                    })

    def __initProp(self, prop):
        if prop['type'] == 'int':
            widget = IntUI()
            widget.setValue(prop)
        elif prop['type'] == 'int2':
            widget = Int2UI()
            widget.setValue(prop)
        elif prop['type'] == 'int3':
            widget = Int3UI()
            widget.setValue(prop)
        elif prop['type'] == 'int4':
            widget = Int4UI()
            widget.setValue(prop)
        elif prop['type'] == 'float':
            widget = FloatUI()
            widget.setValue(prop)
        elif prop['type'] == 'float2':
            widget = Float2UI()
            widget.setValue(prop)
        elif prop['type'] == 'float3':
            widget = Float3UI()
            widget.setValue(prop)
        elif prop['type'] == 'float4':
            widget = Float4UI()
            widget.setValue(prop)
        elif prop['type'] == 'bool':
            widget = BoolUI()
            widget.setValue(prop)
        elif prop['type'] == "enum":
            widget = EnumUI()
            widget.setValue(prop)
        else:
            widget = NoneUI()
            widget.setValue(prop)

        prop['widget'] = widget
        self.lyt_props.addWidget(widget)
        self.lyt_props.setAlignment(widget, Qt.AlignTop)

    def __setProp(self,prop):
        if prop["type"] == 'int' and prop['widget'].getValue() is not None:
            return SDValueInt.sNew(prop['widget'].getValue())
        elif prop["type"] == 'int2' and prop['widget'].getValue() is not None:
            return SDValueInt2.sNew(prop['widget'].getValue())
        elif prop["type"] == 'int3' and prop['widget'].getValue() is not None:
            return SDValueInt3.sNew(prop['widget'].getValue())
        elif prop["type"] == 'int4' and prop['widget'].getValue() is not None:
            return SDValueInt4.sNew(prop['widget'].getValue())
        elif prop["type"] == 'float' and prop['widget'].getValue() is not None:
            return SDValueFloat.sNew(prop['widget'].getValue())
        elif prop["type"] == 'float2' and prop['widget'].getValue() is not None:
            return SDValueFloat2.sNew(prop['widget'].getValue())
        elif prop["type"] == 'float3' and prop['widget'].getValue() is not None:
            return SDValueFloat3.sNew(prop['widget'].getValue())
        elif prop["type"] == 'float4' and prop['widget'].getValue() is not None:
            return SDValueFloat4.sNew(prop['widget'].getValue())
        elif prop["type"] == 'bool' and prop['widget'].getValue() is not None:
            return SDValueBool.sNew(prop['widget'].getValue())
        elif prop["type"] == 'enum' and prop['widget'].getValue() is not None:
            return SDValueInt.sNew(prop['widget'].getValue())
        else:
            return None


def initializeSDPlugin():
    ctx = sd.getContext()
    app = ctx.getSDApplication()
    uiMgr = app.getQtForPythonUIMgr()

    widget = uiMgr.newDockWidget('sd_multinode_editor', 'Multi Node Editor')
    lyt_main = QVBoxLayout()
    widget.setLayout(lyt_main)

    main_ui = MainUI(uiMgr)
    widget.layout().addWidget(main_ui.widget)

def uninitializeSDPlugin():
    pass
