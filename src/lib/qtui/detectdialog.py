#!/usr/bin/env python
# coding=UTF-8
#
# Generated by pykdeuic4 from detectdialog.ui on Sat Mar 10 13:47:59 2012
#
# WARNING! All changes to this file will be lost.
from PyKDE4 import kdecore
from PyKDE4 import kdeui
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 240)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.titleLabel = QtGui.QLabel(self.groupBox)
        self.titleLabel.setObjectName(_fromUtf8("titleLabel"))
        self.verticalLayout_2.addWidget(self.titleLabel)
        self.classLabel = QtGui.QLabel(self.groupBox)
        self.classLabel.setObjectName(_fromUtf8("classLabel"))
        self.verticalLayout_2.addWidget(self.classLabel)
        self.verticalLayout.addWidget(self.groupBox)
        self.kbuttongroup = KButtonGroup(Form)
        self.kbuttongroup.setObjectName(_fromUtf8("kbuttongroup"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.kbuttongroup)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.classButton = QtGui.QRadioButton(self.kbuttongroup)
        self.classButton.setObjectName(_fromUtf8("classButton"))
        self.verticalLayout_3.addWidget(self.classButton)
        self.titleButton = QtGui.QRadioButton(self.kbuttongroup)
        self.titleButton.setObjectName(_fromUtf8("titleButton"))
        self.verticalLayout_3.addWidget(self.titleButton)
        self.verticalLayout.addWidget(self.kbuttongroup)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(kdecore.i18n(_fromUtf8("Form")))
        self.groupBox.setTitle(kdecore.i18n(_fromUtf8("Window information of selected window")))
        self.titleLabel.setText(kdecore.i18n(_fromUtf8("TextLabel")))
        self.classLabel.setText(kdecore.i18n(_fromUtf8("TextLabel")))
        self.kbuttongroup.setTitle(kdecore.i18n(_fromUtf8("Window property selection")))
        self.classButton.setText(kdecore.i18n(_fromUtf8("Window class (entire application)")))
        self.titleButton.setText(kdecore.i18n(_fromUtf8("Window title")))

from PyKDE4.kdeui import KButtonGroup