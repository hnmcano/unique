# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Clientes.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(465, 610)
        MainWindow.setMinimumSize(QSize(465, 610))
        MainWindow.setMaximumSize(QSize(465, 610))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.BrightText, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush1)
        brush2 = QBrush(QColor(255, 255, 220, 255))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipBase, brush2)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipText, brush1)
        brush3 = QBrush(QColor(255, 255, 255, 127))
        brush3.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush3)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Accent, brush1)
#endif
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Light, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.BrightText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipBase, brush2)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush3)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Accent, brush1)
#endif
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Light, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.BrightText, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipBase, brush2)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipText, brush1)
        brush4 = QBrush(QColor(0, 0, 0, 127))
        brush4.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush4)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Accent, brush1)
#endif
        MainWindow.setPalette(palette)
        MainWindow.setStyleSheet(u"QLineEdit{\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #000000, stop: 1 #000000);\n"
"    color: white;\n"
"    border: 1px solid red;\n"
"    padding: 4px 2px;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"    font-size: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #4e4e4e, stop: 1 #4e4e4e);\n"
"}\n"
"\n"
"QLineEdit:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #1a5fb4, stop: 1 #4a00e0);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        palette1 = QPalette()
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush1)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, brush)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush)
        brush5 = QBrush(QColor(127, 127, 127, 255))
        brush5.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush5)
        brush6 = QBrush(QColor(170, 170, 170, 255))
        brush6.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush6)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush1)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.BrightText, brush)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush1)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush1)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipBase, brush2)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush4)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Accent, brush)
#endif
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Light, brush)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush5)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush6)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.BrightText, brush)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipBase, brush2)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush4)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Accent, brush)
#endif
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush5)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Light, brush)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush5)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush6)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush5)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.BrightText, brush)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush5)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush1)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipBase, brush2)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipText, brush1)
        brush7 = QBrush(QColor(127, 127, 127, 127))
        brush7.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush7)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Accent, brush)
#endif
        self.centralwidget.setPalette(palette1)
        self.centralwidget.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 90))
        palette2 = QPalette()
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush1)
        gradient = QLinearGradient(0, 0, 0, 1)
        gradient.setSpread(QGradient.Spread.PadSpread)
        gradient.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient.setColorAt(0, QColor(0, 0, 0, 255))
        gradient.setColorAt(0.5, QColor(0, 0, 0, 255))
        gradient.setColorAt(1, QColor(0, 0, 0, 255))
        brush8 = QBrush(gradient)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush8)
        brush9 = QBrush(QColor(255, 0, 0, 255))
        brush9.setStyle(Qt.BrushStyle.SolidPattern)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, brush9)
        brush10 = QBrush(QColor(212, 0, 0, 255))
        brush10.setStyle(Qt.BrushStyle.SolidPattern)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush10)
        brush11 = QBrush(QColor(85, 0, 0, 255))
        brush11.setStyle(Qt.BrushStyle.SolidPattern)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush11)
        brush12 = QBrush(QColor(113, 0, 0, 255))
        brush12.setStyle(Qt.BrushStyle.SolidPattern)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush12)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush1)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.BrightText, brush)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush1)
        gradient1 = QLinearGradient(0, 0, 0, 1)
        gradient1.setSpread(QGradient.Spread.PadSpread)
        gradient1.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient1.setColorAt(0, QColor(0, 0, 0, 255))
        gradient1.setColorAt(0.5, QColor(0, 0, 0, 255))
        gradient1.setColorAt(1, QColor(0, 0, 0, 255))
        brush13 = QBrush(gradient1)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush13)
        gradient2 = QLinearGradient(0, 0, 0, 1)
        gradient2.setSpread(QGradient.Spread.PadSpread)
        gradient2.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient2.setColorAt(0, QColor(0, 0, 0, 255))
        gradient2.setColorAt(0.5, QColor(0, 0, 0, 255))
        gradient2.setColorAt(1, QColor(0, 0, 0, 255))
        brush14 = QBrush(gradient2)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush14)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush1)
        brush15 = QBrush(QColor(212, 127, 127, 255))
        brush15.setStyle(Qt.BrushStyle.SolidPattern)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush15)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipBase, brush2)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush4)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Accent, brush)
#endif
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush1)
        gradient3 = QLinearGradient(0, 0, 0, 1)
        gradient3.setSpread(QGradient.Spread.PadSpread)
        gradient3.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient3.setColorAt(0, QColor(0, 0, 0, 255))
        gradient3.setColorAt(0.5, QColor(0, 0, 0, 255))
        gradient3.setColorAt(1, QColor(0, 0, 0, 255))
        brush16 = QBrush(gradient3)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush16)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Light, brush9)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush10)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush11)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush12)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush1)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.BrightText, brush)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush1)
        gradient4 = QLinearGradient(0, 0, 0, 1)
        gradient4.setSpread(QGradient.Spread.PadSpread)
        gradient4.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient4.setColorAt(0, QColor(0, 0, 0, 255))
        gradient4.setColorAt(0.5, QColor(0, 0, 0, 255))
        gradient4.setColorAt(1, QColor(0, 0, 0, 255))
        brush17 = QBrush(gradient4)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush17)
        gradient5 = QLinearGradient(0, 0, 0, 1)
        gradient5.setSpread(QGradient.Spread.PadSpread)
        gradient5.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient5.setColorAt(0, QColor(0, 0, 0, 255))
        gradient5.setColorAt(0.5, QColor(0, 0, 0, 255))
        gradient5.setColorAt(1, QColor(0, 0, 0, 255))
        brush18 = QBrush(gradient5)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush18)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush1)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush15)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipBase, brush2)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush4)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Accent, brush)
#endif
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush11)
        gradient6 = QLinearGradient(0, 0, 0, 1)
        gradient6.setSpread(QGradient.Spread.PadSpread)
        gradient6.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient6.setColorAt(0, QColor(0, 0, 0, 255))
        gradient6.setColorAt(0.5, QColor(0, 0, 0, 255))
        gradient6.setColorAt(1, QColor(0, 0, 0, 255))
        brush19 = QBrush(gradient6)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush19)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Light, brush9)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush10)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush11)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush12)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush11)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.BrightText, brush)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush11)
        gradient7 = QLinearGradient(0, 0, 0, 1)
        gradient7.setSpread(QGradient.Spread.PadSpread)
        gradient7.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient7.setColorAt(0, QColor(0, 0, 0, 255))
        gradient7.setColorAt(0.5, QColor(0, 0, 0, 255))
        gradient7.setColorAt(1, QColor(0, 0, 0, 255))
        brush20 = QBrush(gradient7)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush20)
        gradient8 = QLinearGradient(0, 0, 0, 1)
        gradient8.setSpread(QGradient.Spread.PadSpread)
        gradient8.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient8.setColorAt(0, QColor(0, 0, 0, 255))
        gradient8.setColorAt(0.5, QColor(0, 0, 0, 255))
        gradient8.setColorAt(1, QColor(0, 0, 0, 255))
        brush21 = QBrush(gradient8)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush21)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush1)
        brush22 = QBrush(QColor(170, 0, 0, 255))
        brush22.setStyle(Qt.BrushStyle.SolidPattern)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush22)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipBase, brush2)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipText, brush1)
        brush23 = QBrush(QColor(85, 0, 0, 127))
        brush23.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush23)
#endif
        brush24 = QBrush(QColor(221, 0, 0, 255))
        brush24.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Accent, brush24)
#endif
        self.widget.setPalette(palette2)
        self.widget.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(0, 0, 0);\n"
"    border-bottom: 1px solid red;\n"
"    \n"
"    /* Gradiente para profundidade */\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #000000, \n"
"        stop: 0.5 #000000,\n"
"        stop: 1 #000000);\n"
"    \n"
"    /* Sombra externa para efeito 3D */\n"
"    box-shadow: 3px 3px 5px rgba(0, 0, 0, 0.2),\n"
"                -1px -1px 2px rgba(255, 255, 255, 0.3);\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Monotype Corsiva"])
        font.setPointSize(45)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.widget_2)
        self.frame_2.setObjectName(u"frame_2")
        palette3 = QPalette()
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.frame_2.setPalette(palette3)
        self.frame_2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setSpacing(9)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(9, 9, 9, 9)
        self.label_telefone = QLabel(self.frame_2)
        self.label_telefone.setObjectName(u"label_telefone")

        self.gridLayout_2.addWidget(self.label_telefone, 1, 0, 1, 1)

        self.telefone_input = QLineEdit(self.frame_2)
        self.telefone_input.setObjectName(u"telefone_input")
        self.telefone_input.setStyleSheet(u"border: 1px solid red;")

        self.gridLayout_2.addWidget(self.telefone_input, 1, 1, 1, 1)

        self.label_email = QLabel(self.frame_2)
        self.label_email.setObjectName(u"label_email")

        self.gridLayout_2.addWidget(self.label_email, 3, 0, 1, 1)

        self.nome_input = QLineEdit(self.frame_2)
        self.nome_input.setObjectName(u"nome_input")
        self.nome_input.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #000000, stop: 1 #000000);\n"
"    color: white;\n"
"    border: 1px solid red;\n"
"    padding: 12px 24px;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #4e4e4e, stop: 1 #4e4e4e);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #1a5fb4, stop: 1 #4a00e0);\n"
"}")
        self.nome_input.setCursorPosition(0)

        self.gridLayout_2.addWidget(self.nome_input, 0, 1, 1, 1)

        self.label_nome = QLabel(self.frame_2)
        self.label_nome.setObjectName(u"label_nome")

        self.gridLayout_2.addWidget(self.label_nome, 0, 0, 1, 1)

        self.email_input = QLineEdit(self.frame_2)
        self.email_input.setObjectName(u"email_input")
        self.email_input.setStyleSheet(u"border: 1px solid red;")

        self.gridLayout_2.addWidget(self.email_input, 3, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame = QFrame(self.widget_2)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(9, -1, -1, -1)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_25 = QLabel(self.frame_3)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout.addWidget(self.label_25)

        self.cepinput = QLineEdit(self.frame_3)
        self.cepinput.setObjectName(u"cepinput")
        self.cepinput.setStyleSheet(u"border: 1px solid red;")

        self.horizontalLayout.addWidget(self.cepinput)

        self.btn_viacep = QPushButton(self.frame_3)
        self.btn_viacep.setObjectName(u"btn_viacep")
        self.btn_viacep.setEnabled(True)
        self.btn_viacep.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #000000, stop: 1 #000000);\n"
"    color: white;\n"
"    border: 1px solid red;\n"
"    padding: 5px 17px;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"    font-size: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #4e4e4e, stop: 1 #4e4e4e);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #1a5fb4, stop: 1 #4a00e0);\n"
"}")

        self.horizontalLayout.addWidget(self.btn_viacep)


        self.gridLayout_3.addWidget(self.frame_3, 0, 0, 1, 3)

        self.complemento_input = QLineEdit(self.frame)
        self.complemento_input.setObjectName(u"complemento_input")
        self.complemento_input.setStyleSheet(u"border: 1px solid red;")

        self.gridLayout_3.addWidget(self.complemento_input, 10, 1, 1, 1)

        self.label_28 = QLabel(self.frame)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_3.addWidget(self.label_28, 10, 0, 1, 1)

        self.endereco_input = QLineEdit(self.frame)
        self.endereco_input.setObjectName(u"endereco_input")
        self.endereco_input.setStyleSheet(u"border: 1px solid red;")

        self.gridLayout_3.addWidget(self.endereco_input, 3, 1, 1, 1)

        self.bairro_input = QLineEdit(self.frame)
        self.bairro_input.setObjectName(u"bairro_input")
        self.bairro_input.setStyleSheet(u"border: 1px solid red;")

        self.gridLayout_3.addWidget(self.bairro_input, 7, 1, 1, 1)

        self.label_30 = QLabel(self.frame)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_3.addWidget(self.label_30, 8, 0, 1, 1)

        self.cidade_input = QLineEdit(self.frame)
        self.cidade_input.setObjectName(u"cidade_input")
        self.cidade_input.setStyleSheet(u"border: 1px solid red;")

        self.gridLayout_3.addWidget(self.cidade_input, 8, 1, 1, 1)

        self.label_27 = QLabel(self.frame)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_3.addWidget(self.label_27, 7, 0, 1, 1)

        self.label_22 = QLabel(self.frame)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_3.addWidget(self.label_22, 3, 0, 1, 1)

        self.referencia_input = QLineEdit(self.frame)
        self.referencia_input.setObjectName(u"referencia_input")
        self.referencia_input.setStyleSheet(u"border: 1px solid red;")

        self.gridLayout_3.addWidget(self.referencia_input, 11, 1, 1, 1)

        self.label_29 = QLabel(self.frame)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_3.addWidget(self.label_29, 11, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(16777215, 75))
        self.widget_3.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.cad_clientes = QPushButton(self.widget_3)
        self.cad_clientes.setObjectName(u"cad_clientes")
        self.cad_clientes.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #000000, stop: 1 #000000);\n"
"    color: white;\n"
"    border: 1px solid red;\n"
"    padding: 5px 17px;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #4e4e4e, stop: 1 #4e4e4e);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #1a5fb4, stop: 1 #4a00e0);\n"
"}\n"
"")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ContactNew))
        self.cad_clientes.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.cad_clientes)

        self.cancelar = QPushButton(self.widget_3)
        self.cancelar.setObjectName(u"cancelar")
        self.cancelar.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #000000, stop: 1 #000000);\n"
"    color: white;\n"
"    border: 1px solid red;\n"
"    padding: 5px 17px;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #4e4e4e, stop: 1 #4e4e4e);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #1a5fb4, stop: 1 #4a00e0);\n"
"}")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit))
        self.cancelar.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.cancelar)


        self.verticalLayout.addWidget(self.widget_3)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.nome_input, self.telefone_input)
        QWidget.setTabOrder(self.telefone_input, self.email_input)
        QWidget.setTabOrder(self.email_input, self.cad_clientes)
        QWidget.setTabOrder(self.cad_clientes, self.cancelar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Cadastro de Clientes", None))
        self.label_telefone.setText(QCoreApplication.translate("MainWindow", u"Telefone:", None))
        self.label_email.setText(QCoreApplication.translate("MainWindow", u"E-mail:", None))
        self.label_nome.setText(QCoreApplication.translate("MainWindow", u"Cliente:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Cep:", None))
        self.cepinput.setText("")
        self.cepinput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite seu CEP aqui...", None))
        self.btn_viacep.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Complemento:", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Cidade:", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Bairro:", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o:", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Ref:", None))
        self.cad_clientes.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Cliente", None))
        self.cancelar.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
    # retranslateUi

