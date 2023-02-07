#!/usr/bin/env python
#Jet:这个是挺好用的模板！编码框架清晰，值得参考。
#一个简单的文本编辑器，中文显示乱码！
#to do: 可以改编成一个python课程的案例， 文本编辑器

from PyQt5.QtCore import (QFile, QFileInfo, QPoint, QRect, QSettings, QSize,
        Qt, QTextStream)
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import (QAction, QApplication, QFileDialog, QMainWindow,
        QMessageBox, QTextEdit)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.curFile = ''

        #创建TestEdit，并居中
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        self.createActions()
        self.createMenus()
        self.createToolBars()
        self.createStatusBar()

        self.readSettings()

        self.textEdit.document().contentsChanged.connect(self.documentWasModified)

        self.setCurrentFile('')

    def closeEvent(self, event):
        if self.maybeSave():
            self.writeSettings()
            event.accept()
        else:
            event.ignore()

    def newFile(self):
        if self.maybeSave():
            self.textEdit.clear()
            self.setCurrentFile('')

    def open(self):
        #检查当前是否做了修改
        if self.maybeSave():
            fileName, _ = QFileDialog.getOpenFileName(self)
            if fileName:
                self.loadFile(fileName)
    #保存文件
    def save(self):
        #如果修改的文件已经存在
        if self.curFile:
            return self.saveFile(self.curFile)
        #否则另存为
        return self.saveAs()

    def saveAs(self):
        fileName, _ = QFileDialog.getSaveFileName(self)
        if fileName:
            return self.saveFile(fileName)

        return False

    def about(self):
        QMessageBox.about(self, "About Application",
                "The <b>Application</b> example demonstrates how to write "
                "modern GUI applications using Qt, with a menu bar, "
                "toolbars, and a status bar.")

    def documentWasModified(self):
        self.setWindowModified(self.textEdit.document().isModified())
    #QAction
    def createActions(self):
        root = QFileInfo(__file__).absolutePath()

        self.newAct = QAction(QIcon(root + '/images/new.png'), "&New", self,
                shortcut=QKeySequence.New, statusTip="Create a new file",
                triggered=self.newFile)

        self.openAct = QAction(QIcon(root + '/images/open.png'), "&Open...",
                self, shortcut=QKeySequence.Open,
                statusTip="Open an existing file", triggered=self.open)

        self.saveAct = QAction(QIcon(root + '/images/save.png'), "&Save", self,
                shortcut=QKeySequence.Save,
                statusTip="Save the document to disk", triggered=self.save)

        self.saveAsAct = QAction("Save &As...", self,
                shortcut=QKeySequence.SaveAs,
                statusTip="Save the document under a new name",
                triggered=self.saveAs)

        self.exitAct = QAction("E&xit", self, shortcut="Ctrl+Q",
                statusTip="Exit the application", triggered=self.close)

        self.cutAct = QAction(QIcon(root + '/images/cut.png'), "&Cut", self,
                shortcut=QKeySequence.Cut,
                statusTip="Cut the current selection's contents to the clipboard",
                triggered=self.textEdit.cut)

        self.copyAct = QAction(QIcon(root + '/images/copy.png'), "&Copy", self,
                shortcut=QKeySequence.Copy,
                statusTip="Copy the current selection's contents to the clipboard",
                triggered=self.textEdit.copy)

        self.pasteAct = QAction(QIcon(root + '/images/paste.png'), "&Paste",
                self, shortcut=QKeySequence.Paste,
                statusTip="Paste the clipboard's contents into the current selection",
                triggered=self.textEdit.paste)

        self.aboutAct = QAction("&About", self,
                statusTip="Show the application's About box",
                triggered=self.about)

        self.aboutQtAct = QAction("About &Qt", self,
                statusTip="Show the Qt library's About box",
                triggered=QApplication.instance().aboutQt)
        #初始状态时将cutAct和copyAct禁止
        self.cutAct.setEnabled(False)
        self.copyAct.setEnabled(False)
        #当文本框里有内容的时候将cutAct和copyAct打开
        self.textEdit.copyAvailable.connect(self.cutAct.setEnabled)
        self.textEdit.copyAvailable.connect(self.copyAct.setEnabled)
    #菜单
    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.newAct)
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.saveAct)
        self.fileMenu.addAction(self.saveAsAct)
        self.fileMenu.addSeparator();
        self.fileMenu.addAction(self.exitAct)

        self.editMenu = self.menuBar().addMenu("&Edit")
        self.editMenu.addAction(self.cutAct)
        self.editMenu.addAction(self.copyAct)
        self.editMenu.addAction(self.pasteAct)

        self.menuBar().addSeparator()

        self.helpMenu = self.menuBar().addMenu("&Help")
        self.helpMenu.addAction(self.aboutAct)
        self.helpMenu.addAction(self.aboutQtAct)
    #工具栏
    def createToolBars(self):
        self.fileToolBar = self.addToolBar("File")
        self.fileToolBar.addAction(self.newAct)
        self.fileToolBar.addAction(self.openAct)
        self.fileToolBar.addAction(self.saveAct)

        self.editToolBar = self.addToolBar("Edit")
        self.editToolBar.addAction(self.cutAct)
        self.editToolBar.addAction(self.copyAct)
        self.editToolBar.addAction(self.pasteAct)
    #状态栏显示”ready“
    def createStatusBar(self):
        self.statusBar().showMessage("Ready")

    def readSettings(self):
        #创建一个QSettings，第一个参数是公司名，后一个参数可以是项目名
        #settings = QSettings("Trolltech", "Application Example")
        settings = QSettings("./Qt.ini", QSettings.IniFormat)
        #设定窗口位置、大小默认值
        pos = settings.value("pos", QPoint(200, 200))
        size = settings.value("size", QSize(400, 400))
        self.resize(size)
        self.move(pos)
    """
    QSettings具体参数可以用python查看
    from PyQt5.QtCore import QSettings
    help(QSettings)
    """
    def writeSettings(self):
        settings = QSettings("./Qt.ini", QSettings.IniFormat)
        settings.setValue("pos", self.pos())
        settings.setValue("size", self.size())

    def maybeSave(self):
        #检查是否做了修改
        if self.textEdit.document().isModified():
            #进行提示，提供三个选择
            ret = QMessageBox.warning(self, "Application",
                    "The document has been modified.\nDo you want to save "
                    "your changes?",
                    QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)

            if ret == QMessageBox.Save:
                return self.save()

            if ret == QMessageBox.Cancel:
                return False

        return True

    def loadFile(self, fileName):
        file = QFile(fileName)
        if not file.open(QFile.ReadOnly | QFile.Text):
            QMessageBox.warning(self, "Application",
                    "Cannot read file %s:\n%s." % (fileName, file.errorString()))
            return

        inf = QTextStream(file)
        #Jet adds:
        inf.setCodec("utf-8") #避免中文出现乱码

        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.textEdit.setPlainText(inf.readAll())
        QApplication.restoreOverrideCursor()

        self.setCurrentFile(fileName)
        self.statusBar().showMessage("File loaded", 2000)
    #文件进行保存
    def saveFile(self, fileName):
        #QFile实例化
        file = QFile(fileName)
        '''参数有：ReadOnly/WriteOnly/ReadWrite/Append/Truncate/
        Text/Unbuffered'''
        if not file.open(QFile.WriteOnly | QFile.Text):
            QMessageBox.warning(self, "Application",
                    "Cannot write file %s:\n%s." % (fileName, file.errorString()))
            return False
        #相当于一个数据流buffer
        outf = QTextStream(file)
        # Jet adds:
        outf.setCodec("utf-8")  # 避免中文出现乱码

        #设置为等待光标
        QApplication.setOverrideCursor(Qt.WaitCursor)
        #读取textEdit内容，往数据流中写入.
        outf << self.textEdit.toPlainText()
        file.close()
        #恢复为普通光标
        QApplication.restoreOverrideCursor()

        self.setCurrentFile(fileName);

        #5000：显示的时长
        self.statusBar().showMessage("File saved", 5000)
        return True

    def setCurrentFile(self, fileName):
        self.curFile = fileName
        self.textEdit.document().setModified(False)
        self.setWindowModified(False)

        if self.curFile:
            #移除文件名中的路径字符
            shownName = self.strippedName(self.curFile)
        else:
            shownName = 'untitled.txt'
        #设置窗口标题
        self.setWindowTitle("%s[*] - Application" % shownName)

    def strippedName(self, fullFileName):
        #返回文件名
        return QFileInfo(fullFileName).fileName()


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
'''
————————————————
版权声明：本文为CSDN博主「慢几步-深几度-前行」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/lugandong/article/details/50596029
'''