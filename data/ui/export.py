# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'export.ui'
#
# Created: Wed May 15 18:12:11 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Export(object):
    def setupUi(self, Export):
        Export.setObjectName("Export")
        Export.resize(791, 451)
        self.horizontalLayout_4 = QtGui.QHBoxLayout(Export)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tree_profiles = QtGui.QTreeWidget(Export)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tree_profiles.sizePolicy().hasHeightForWidth())
        self.tree_profiles.setSizePolicy(sizePolicy)
        self.tree_profiles.setMaximumSize(QtCore.QSize(191, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.tree_profiles.setPalette(palette)
        self.tree_profiles.setObjectName("tree_profiles")
        self.tree_profiles.headerItem().setText(0, "1")
        self.verticalLayout_5.addWidget(self.tree_profiles)
        self.line_export = QtGui.QLineEdit(Export)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_export.sizePolicy().hasHeightForWidth())
        self.line_export.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.line_export.setPalette(palette)
        self.line_export.setObjectName("line_export")
        self.verticalLayout_5.addWidget(self.line_export)
        self.button_save = QtGui.QPushButton(Export)
        self.button_save.setMaximumSize(QtCore.QSize(191, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/actions/actions/filesaveas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_save.setIcon(icon)
        self.button_save.setObjectName("button_save")
        self.verticalLayout_5.addWidget(self.button_save)
        self.button_load = QtGui.QPushButton(Export)
        self.button_load.setMaximumSize(QtCore.QSize(191, 16777215))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/actions/actions/fileopen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_load.setIcon(icon1)
        self.button_load.setObjectName("button_load")
        self.verticalLayout_5.addWidget(self.button_load)
        self.button_delete = QtGui.QPushButton(Export)
        self.button_delete.setMaximumSize(QtCore.QSize(191, 16777215))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/actions/actions/editdelete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_delete.setIcon(icon2)
        self.button_delete.setObjectName("button_delete")
        self.verticalLayout_5.addWidget(self.button_delete)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tree_leagues = QtGui.QTreeWidget(Export)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tree_leagues.sizePolicy().hasHeightForWidth())
        self.tree_leagues.setSizePolicy(sizePolicy)
        self.tree_leagues.setMaximumSize(QtCore.QSize(250, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.tree_leagues.setPalette(palette)
        self.tree_leagues.setObjectName("tree_leagues")
        self.tree_leagues.headerItem().setText(0, "1")
        self.verticalLayout_4.addWidget(self.tree_leagues)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(Export)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_2 = QtGui.QLabel(Export)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.spin_min = QtGui.QSpinBox(Export)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.spin_min.setPalette(palette)
        self.spin_min.setMinimum(1)
        self.spin_min.setMaximum(40)
        self.spin_min.setProperty("value", 5)
        self.spin_min.setObjectName("spin_min")
        self.horizontalLayout_3.addWidget(self.spin_min)
        self.spin_max = QtGui.QSpinBox(Export)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.spin_max.setPalette(palette)
        self.spin_max.setMinimum(1)
        self.spin_max.setMaximum(50)
        self.spin_max.setProperty("value", 50)
        self.spin_max.setObjectName("spin_max")
        self.horizontalLayout_3.addWidget(self.spin_max)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.button_add = QtGui.QPushButton(Export)
        self.button_add.setMaximumSize(QtCore.QSize(250, 16777215))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/actions/actions/edit_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_add.setIcon(icon3)
        self.button_add.setObjectName("button_add")
        self.verticalLayout_4.addWidget(self.button_add)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.table_leagues = QtGui.QTableWidget(Export)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.table_leagues.setPalette(palette)
        self.table_leagues.setObjectName("table_leagues")
        self.table_leagues.setColumnCount(0)
        self.table_leagues.setRowCount(0)
        self.verticalLayout_3.addWidget(self.table_leagues)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_remove = QtGui.QPushButton(Export)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/actions/actions/edit_remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_remove.setIcon(icon4)
        self.button_remove.setObjectName("button_remove")
        self.horizontalLayout.addWidget(self.button_remove)
        self.button_clear = QtGui.QPushButton(Export)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/actions/actions/editclear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_clear.setIcon(icon5)
        self.button_clear.setObjectName("button_clear")
        self.horizontalLayout.addWidget(self.button_clear)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.line_export_name = QtGui.QLineEdit(Export)
        self.line_export_name.setObjectName("line_export_name")
        self.verticalLayout_2.addWidget(self.line_export_name)
        self.button_export = QtGui.QPushButton(Export)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/actions/actions/player_play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_export.setIcon(icon6)
        self.button_export.setObjectName("button_export")
        self.verticalLayout_2.addWidget(self.button_export)
        self.progress_2 = QtGui.QProgressBar(Export)
        self.progress_2.setProperty("value", 0)
        self.progress_2.setObjectName("progress_2")
        self.verticalLayout_2.addWidget(self.progress_2)
        self.text_export = QtGui.QTextBrowser(Export)
        self.text_export.setObjectName("text_export")
        self.verticalLayout_2.addWidget(self.text_export)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.retranslateUi(Export)
        QtCore.QMetaObject.connectSlotsByName(Export)

    def retranslateUi(self, Export):
        Export.setWindowTitle(QtGui.QApplication.translate("Export", "Export manager", None, QtGui.QApplication.UnicodeUTF8))
        self.line_export.setText(QtGui.QApplication.translate("Export", "profile_name_here", None, QtGui.QApplication.UnicodeUTF8))
        self.button_save.setText(QtGui.QApplication.translate("Export", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.button_load.setText(QtGui.QApplication.translate("Export", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.button_delete.setText(QtGui.QApplication.translate("Export", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setToolTip(QtGui.QApplication.translate("Export", "Min rounds played", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Export", "   r_min", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setToolTip(QtGui.QApplication.translate("Export", "Max round played", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Export", "   r_max", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_min.setToolTip(QtGui.QApplication.translate("Export", "Min rounds played", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_max.setToolTip(QtGui.QApplication.translate("Export", "Max rounds played", None, QtGui.QApplication.UnicodeUTF8))
        self.button_add.setText(QtGui.QApplication.translate("Export", "Add league", None, QtGui.QApplication.UnicodeUTF8))
        self.button_remove.setText(QtGui.QApplication.translate("Export", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.button_clear.setText(QtGui.QApplication.translate("Export", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.line_export_name.setText(QtGui.QApplication.translate("Export", "export_name_here", None, QtGui.QApplication.UnicodeUTF8))
        self.button_export.setText(QtGui.QApplication.translate("Export", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.progress_2.setFormat(QtGui.QApplication.translate("Export", "%p%", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
