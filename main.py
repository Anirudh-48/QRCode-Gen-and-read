from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton,QStatusBar,QVBoxLayout,QHBoxLayout
import sys
from PIL.ImageQt import ImageQt
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMessageBox
import PyQt5
import qrcode
import os
import sys
from pyzbar.pyzbar import decode
from PIL import Image

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1000,900)

        mainLayout=QVBoxLayout()
        btnLayout=QHBoxLayout()
        self.btnEncrypt=QPushButton('Convert text into QR')
        self.btnEncrypt.clicked.connect(QRGen)
        self.btnDec=QPushButton('Decode QR into text')
        self.btnDec.clicked.connect(QRdec)
        btnLayout.addWidget(self.btnEncrypt)
        btnLayout.addWidget(self.btnDec)
        self.btnEncrypt.clicked.connect(self.on_pushButton_clicked)
        self.btnDec.clicked.connect(self.on_decpushButton_clicked)
        mainLayout.addLayout(btnLayout)
        self.setLayout(mainLayout)
        self.dialog=QRGen()
        self.dialog1=QRdec()
        
    def on_pushButton_clicked(self):
        self.dialog.show()
    
    def on_decpushButton_clicked(self):
        self.dialog1.show()
    
class QRGen(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1000,900)
        self.setWindowTitle('QR Code!!')
        self.UIinit()
        
    def UIinit(self):
        font=QFont('Open Sans',20)
        
        mainLayout=QVBoxLayout()
        entryLayout=QHBoxLayout()
        btnLayout=QHBoxLayout()
        imgLayout=QVBoxLayout()
        imgLayout.addStretch()
        
        label=QLabel('Enter Text:')
        label.setFont(font)
        self.textEntry=QLineEdit()
        self.textEntry.setFont(font)
        self.textEntry1=QLineEdit()
        self.textEntry1.setFont(font)
        entryLayout.addWidget(label)
        entryLayout.addWidget(self.textEntry)
        
        label1=QLabel('Enter File Name')
        label1.setFont(font)
        self.textEntry1=QLineEdit()
        self.textEntry1.setFont(font)
        entryLayout.addWidget(label1)
        entryLayout.addWidget(self.textEntry1)
        
        
        mainLayout.addLayout(entryLayout)
        
        self.btnGenerate=QPushButton('Generate QR Code')
        self.btnGenerate.clicked.connect(self.create_qr)
        self.btnsaveimg=QPushButton('Save QR Code')
        self.btnsaveimg.clicked.connect(self.save)
        self.btnclear=QPushButton('Clear')
        self.btnclear.clicked.connect(self.clear)
        
        btnLayout.addWidget(self.btnGenerate)
        btnLayout.addWidget(self.btnsaveimg)
        btnLayout.addWidget(self.btnclear)
        mainLayout.addLayout(btnLayout)
        self.imagelabel=QLabel()       
        
        self.imageLabel=QLabel()
        self.imageLabel.setAlignment(Qt.AlignCenter)
        imgLayout.addWidget(self.imageLabel)
        mainLayout.addLayout(imgLayout)
        
        
        self.statusBar=QStatusBar()
        mainLayout.addWidget(self.statusBar)
        
        self.setLayout(mainLayout)
    
    def clear(self):
        self.textEntry.clear()
        self.imageLabel.clear()
        self.textEntry1.clear()
        
    def create_qr(self):
        text=self.textEntry.text()
        img=qrcode.make(text)
        qr=ImageQt(img)
        pix=QPixmap.fromImage(qr)
        self.imageLabel.setPixmap(pix)
        
    def save(self):
        curdir=os.getcwd()
        filename=self.textEntry1.text()
        
        if filename:
            self.imageLabel.pixmap().save(os.path.join(curdir,filename+'.png'))
            
            
class QRdec(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1000,900)
        self.setWindowTitle('QR Code!!')
        self.UIinit()
        
    def UIinit(self):
        mainLayout=QVBoxLayout()
        btnLayout=QHBoxLayout()
        entryLayout=QHBoxLayout()
        font=QFont('Open Sans',20)
        self.textEntry=QLineEdit()
        self.textEntry.setFont(font)
        entryLayout.addWidget(self.textEntry)
        self.imgLayout=QVBoxLayout()
        self.imgLayout.addStretch()
        mainLayout.addLayout(entryLayout)
                
        self.btn=QPushButton('Click Here to decrypt the QR code')
        self.btn.clicked.connect(self.decrypt)
        
        btnLayout.addWidget(self.btn)
        mainLayout.addLayout(btnLayout)
        self.setLayout(mainLayout)
        
    def decrypt(self):
        filename=self.textEntry.text()
        textboxValue=decode(Image.open(filename))
        message=QMessageBox()
        message.setInformativeText('The data is: '+str(textboxValue[0][0])[2:-1])
        message.exec_()
        
        
app=QApplication(sys.argv)
app.setStyleSheet('QPushButton{Height: 50px; font-size:20px}')

qr1=MainWin()
qr1.show()

sys.exit(app.exec_())
