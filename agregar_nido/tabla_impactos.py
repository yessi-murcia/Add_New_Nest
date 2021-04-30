from qgis.PyQt.QtWidgets import * 
from .tabla_impactos_dialog import Ui_Dialog

class DlgTabla(QDialog, Ui_Dialog):
    def __init__(self):
        super(DlgTabla, self).__init__()
        self.setupUI(self)
        
        self.tbl.set.ColumnWidth(1, 200)