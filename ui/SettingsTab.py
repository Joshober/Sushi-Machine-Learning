# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SettingsTab.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_settings_tab(object):
    def setupUi(self, settings_tab):
        settings_tab.setObjectName("settings_tab")
        settings_tab.resize(750, 561)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ui/resources/tab_icons/settings_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        settings_tab.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(settings_tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_37 = QtWidgets.QFrame(settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_37.sizePolicy().hasHeightForWidth())
        self.frame_37.setSizePolicy(sizePolicy)
        self.frame_37.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_37.setObjectName("frame_37")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_37)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.frame_33 = QtWidgets.QFrame(self.frame_37)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_33.sizePolicy().hasHeightForWidth())
        self.frame_33.setSizePolicy(sizePolicy)
        self.frame_33.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_33.setObjectName("frame_33")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_33)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_24 = QtWidgets.QLabel(self.frame_33)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_19.addWidget(self.label_24, 0, QtCore.Qt.AlignHCenter)
        self.frame_34 = QtWidgets.QFrame(self.frame_33)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_34.sizePolicy().hasHeightForWidth())
        self.frame_34.setSizePolicy(sizePolicy)
        self.frame_34.setObjectName("frame_34")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frame_34)
        self.gridLayout_11.setHorizontalSpacing(10)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_30 = QtWidgets.QLabel(self.frame_34)
        self.label_30.setObjectName("label_30")
        self.gridLayout_11.addWidget(self.label_30, 5, 0, 1, 1)
        self.other_directory_edit = QtWidgets.QLineEdit(self.frame_34)
        self.other_directory_edit.setReadOnly(True)
        self.other_directory_edit.setObjectName("other_directory_edit")
        self.gridLayout_11.addWidget(self.other_directory_edit, 1, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.frame_34)
        self.label_25.setObjectName("label_25")
        self.gridLayout_11.addWidget(self.label_25, 0, 0, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.frame_34)
        self.label_29.setObjectName("label_29")
        self.gridLayout_11.addWidget(self.label_29, 1, 0, 1, 1)
        self.concurrent_vendors_help_button = QtWidgets.QPushButton(self.frame_34)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.concurrent_vendors_help_button.sizePolicy().hasHeightForWidth())
        self.concurrent_vendors_help_button.setSizePolicy(sizePolicy)
        self.concurrent_vendors_help_button.setMaximumSize(QtCore.QSize(25, 25))
        self.concurrent_vendors_help_button.setObjectName("concurrent_vendors_help_button")
        self.gridLayout_11.addWidget(self.concurrent_vendors_help_button, 7, 2, 1, 1)
        self.other_directory_button = QtWidgets.QPushButton(self.frame_34)
        self.other_directory_button.setObjectName("other_directory_button")
        self.gridLayout_11.addWidget(self.other_directory_button, 1, 2, 1, 1)
        self.yearly_directory_button = QtWidgets.QPushButton(self.frame_34)
        self.yearly_directory_button.setObjectName("yearly_directory_button")
        self.gridLayout_11.addWidget(self.yearly_directory_button, 0, 2, 1, 1)
        self.yearly_directory_edit = QtWidgets.QLineEdit(self.frame_34)
        self.yearly_directory_edit.setReadOnly(True)
        self.yearly_directory_edit.setObjectName("yearly_directory_edit")
        self.gridLayout_11.addWidget(self.yearly_directory_edit, 0, 1, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.frame_34)
        self.label_32.setObjectName("label_32")
        self.gridLayout_11.addWidget(self.label_32, 8, 0, 1, 1)
        self.concurrent_reports_spin_box = QtWidgets.QSpinBox(self.frame_34)
        self.concurrent_reports_spin_box.setMaximum(999)
        self.concurrent_reports_spin_box.setObjectName("concurrent_reports_spin_box")
        self.gridLayout_11.addWidget(self.concurrent_reports_spin_box, 8, 1, 1, 1)
        self.concurrent_reports_help_button = QtWidgets.QPushButton(self.frame_34)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.concurrent_reports_help_button.sizePolicy().hasHeightForWidth())
        self.concurrent_reports_help_button.setSizePolicy(sizePolicy)
        self.concurrent_reports_help_button.setMaximumSize(QtCore.QSize(25, 25))
        self.concurrent_reports_help_button.setObjectName("concurrent_reports_help_button")
        self.gridLayout_11.addWidget(self.concurrent_reports_help_button, 8, 2, 1, 1)
        self.yearly_directory_help_button = QtWidgets.QPushButton(self.frame_34)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yearly_directory_help_button.sizePolicy().hasHeightForWidth())
        self.yearly_directory_help_button.setSizePolicy(sizePolicy)
        self.yearly_directory_help_button.setMaximumSize(QtCore.QSize(25, 25))
        self.yearly_directory_help_button.setObjectName("yearly_directory_help_button")
        self.gridLayout_11.addWidget(self.yearly_directory_help_button, 0, 3, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.frame_34)
        self.label_33.setObjectName("label_33")
        self.gridLayout_11.addWidget(self.label_33, 10, 0, 1, 1)
        self.request_interval_help_button = QtWidgets.QPushButton(self.frame_34)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.request_interval_help_button.sizePolicy().hasHeightForWidth())
        self.request_interval_help_button.setSizePolicy(sizePolicy)
        self.request_interval_help_button.setMaximumSize(QtCore.QSize(25, 25))
        self.request_interval_help_button.setObjectName("request_interval_help_button")
        self.gridLayout_11.addWidget(self.request_interval_help_button, 5, 2, 1, 1)
        self.request_timeout_spin_box = QtWidgets.QSpinBox(self.frame_34)
        self.request_timeout_spin_box.setMaximum(9999)
        self.request_timeout_spin_box.setSingleStep(30)
        self.request_timeout_spin_box.setObjectName("request_timeout_spin_box")
        self.gridLayout_11.addWidget(self.request_timeout_spin_box, 6, 1, 1, 1)
        self.request_interval_spin_box = QtWidgets.QSpinBox(self.frame_34)
        self.request_interval_spin_box.setMaximum(999)
        self.request_interval_spin_box.setObjectName("request_interval_spin_box")
        self.gridLayout_11.addWidget(self.request_interval_spin_box, 5, 1, 1, 1)
        self.empty_cell_help_button = QtWidgets.QPushButton(self.frame_34)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.empty_cell_help_button.sizePolicy().hasHeightForWidth())
        self.empty_cell_help_button.setSizePolicy(sizePolicy)
        self.empty_cell_help_button.setMaximumSize(QtCore.QSize(25, 25))
        self.empty_cell_help_button.setObjectName("empty_cell_help_button")
        self.gridLayout_11.addWidget(self.empty_cell_help_button, 10, 2, 1, 1)
        self.other_directory_help_button = QtWidgets.QPushButton(self.frame_34)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.other_directory_help_button.sizePolicy().hasHeightForWidth())
        self.other_directory_help_button.setSizePolicy(sizePolicy)
        self.other_directory_help_button.setMaximumSize(QtCore.QSize(25, 25))
        self.other_directory_help_button.setObjectName("other_directory_help_button")
        self.gridLayout_11.addWidget(self.other_directory_help_button, 1, 3, 1, 1)
        self.empty_cell_edit = QtWidgets.QLineEdit(self.frame_34)
        self.empty_cell_edit.setObjectName("empty_cell_edit")
        self.gridLayout_11.addWidget(self.empty_cell_edit, 10, 1, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.frame_34)
        self.label_31.setObjectName("label_31")
        self.gridLayout_11.addWidget(self.label_31, 7, 0, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.frame_34)
        self.label_37.setObjectName("label_37")
        self.gridLayout_11.addWidget(self.label_37, 6, 0, 1, 1)
        self.request_timeout_help_button = QtWidgets.QPushButton(self.frame_34)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.request_timeout_help_button.sizePolicy().hasHeightForWidth())
        self.request_timeout_help_button.setSizePolicy(sizePolicy)
        self.request_timeout_help_button.setMaximumSize(QtCore.QSize(25, 25))
        self.request_timeout_help_button.setObjectName("request_timeout_help_button")
        self.gridLayout_11.addWidget(self.request_timeout_help_button, 6, 2, 1, 1)
        self.concurrent_vendors_spin_box = QtWidgets.QSpinBox(self.frame_34)
        self.concurrent_vendors_spin_box.setMaximum(999)
        self.concurrent_vendors_spin_box.setObjectName("concurrent_vendors_spin_box")
        self.gridLayout_11.addWidget(self.concurrent_vendors_spin_box, 7, 1, 1, 1)
        self.label_73 = QtWidgets.QLabel(self.frame_34)
        self.label_73.setObjectName("label_73")
        self.gridLayout_11.addWidget(self.label_73, 11, 0, 1, 1)
        self.user_agent_edit = QtWidgets.QLineEdit(self.frame_34)
        self.user_agent_edit.setObjectName("user_agent_edit")
        self.gridLayout_11.addWidget(self.user_agent_edit, 11, 1, 1, 1)
        self.user_agent_help_button = QtWidgets.QPushButton(self.frame_34)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_agent_help_button.sizePolicy().hasHeightForWidth())
        self.user_agent_help_button.setSizePolicy(sizePolicy)
        self.user_agent_help_button.setMaximumSize(QtCore.QSize(25, 25))
        self.user_agent_help_button.setObjectName("user_agent_help_button")
        self.gridLayout_11.addWidget(self.user_agent_help_button, 11, 2, 1, 1)
        self.verticalLayout_19.addWidget(self.frame_34)
        self.gridLayout_10.addWidget(self.frame_33, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.frame_37)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(-1, 30, -1, 30)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.save_button = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_button.sizePolicy().hasHeightForWidth())
        self.save_button.setSizePolicy(sizePolicy)
        self.save_button.setObjectName("save_button")
        self.horizontalLayout.addWidget(self.save_button)
        self.gridLayout_10.addWidget(self.frame, 4, 0, 1, 1)
        self.frame_35 = QtWidgets.QFrame(self.frame_37)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_35.sizePolicy().hasHeightForWidth())
        self.frame_35.setSizePolicy(sizePolicy)
        self.frame_35.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_35.setObjectName("frame_35")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.frame_35)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_26 = QtWidgets.QLabel(self.frame_35)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_20.addWidget(self.label_26, 0, QtCore.Qt.AlignHCenter)
        self.settings_restore_database_button = QtWidgets.QPushButton(self.frame_35)
        self.settings_restore_database_button.setObjectName("settings_restore_database_button")
        self.verticalLayout_20.addWidget(self.settings_restore_database_button)
        self.gridLayout_10.addWidget(self.frame_35, 3, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.frame_37)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_27 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_2.addWidget(self.label_27, 0, QtCore.Qt.AlignHCenter)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.show_debug_check_box = QtWidgets.QCheckBox(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.show_debug_check_box.sizePolicy().hasHeightForWidth())
        self.show_debug_check_box.setSizePolicy(sizePolicy)
        self.show_debug_check_box.setText("")
        self.show_debug_check_box.setObjectName("show_debug_check_box")
        self.gridLayout.addWidget(self.show_debug_check_box, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.gridLayout_10.addWidget(self.frame_2, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_37)

        self.retranslateUi(settings_tab)
        QtCore.QMetaObject.connectSlotsByName(settings_tab)

    def retranslateUi(self, settings_tab):
        _translate = QtCore.QCoreApplication.translate
        settings_tab.setWindowTitle(_translate("settings_tab", "Settings"))
        self.label_24.setText(_translate("settings_tab", "Reports"))
        self.label_30.setText(_translate("settings_tab", "Report Request Interval"))
        self.label_25.setText(_translate("settings_tab", "Yearly Reports Directory"))
        self.label_29.setText(_translate("settings_tab", "Other Reports Directory"))
        self.concurrent_vendors_help_button.setText(_translate("settings_tab", "?"))
        self.other_directory_button.setText(_translate("settings_tab", "Choose"))
        self.yearly_directory_button.setText(_translate("settings_tab", "Choose"))
        self.label_32.setText(_translate("settings_tab", "Concurrent Reports"))
        self.concurrent_reports_help_button.setText(_translate("settings_tab", "?"))
        self.yearly_directory_help_button.setText(_translate("settings_tab", "?"))
        self.label_33.setText(_translate("settings_tab", "Empty Cell"))
        self.request_interval_help_button.setText(_translate("settings_tab", "?"))
        self.empty_cell_help_button.setText(_translate("settings_tab", "?"))
        self.other_directory_help_button.setText(_translate("settings_tab", "?"))
        self.label_31.setText(_translate("settings_tab", "Concurrent Vendors"))
        self.label_37.setText(_translate("settings_tab", "Request Timeout"))
        self.request_timeout_help_button.setText(_translate("settings_tab", "?"))
        self.label_73.setText(_translate("settings_tab", "User Agent"))
        self.user_agent_help_button.setText(_translate("settings_tab", "?"))
        self.save_button.setText(_translate("settings_tab", "Save Changes"))
        self.label_26.setText(_translate("settings_tab", "Search"))
        self.settings_restore_database_button.setText(_translate("settings_tab", "Restore Database"))
        self.label_27.setText(_translate("settings_tab", "General"))
        self.label.setText(_translate("settings_tab", "Show Debug Messages in Console Window"))
import Resources_rc
