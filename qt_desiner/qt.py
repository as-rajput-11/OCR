import sys
import cv2
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage ,QPixmap
from PyQt5.QtWidgets import QDialog ,QApplication
from PyQt5.uic import loadUi

class tehseencode(QDialog):
  def _init__(self):
    super(tehseencode, self).__init__()
    loadUi('rt.ui' , self)
    self.logic=0
    self.value=1
    self.SHOW.clicked.connect(self.onclicked)
    self.CAPTURE.clicked.connect(self.Captureclicked)

@pyqtSlot()
    
def onclicked(self):
  cap = cv2.videoCapture('qw.mp4')
  while (cap.isOpened()):
    ret,frame = cap.read()
    if ret ==True:
      
      self.displayImage(frame,1)
      cv2.waitkey()

      if(self.logic.logic==2):
        self.value=self.value+1
        cv2.imwrite('%s.jpg'%(self.value), frame)

        self.logic=1

      else:
        print("image not found")
  cap.release()
  cv2.destroyAllWindows()


def Captureclicked(self):
  self.logic=2


def displayImage(self, img,window=1):
  qformat =QImage.Format_Indexed8

  if len(img.shape) == 3:
    if (img.shape[2]) == 4:
      qformat = QImage.Format_RGB888

    else:
      qformat = QImage.Format_RGB888
  img = QImage(img, img.shape[1], img.shape[0], qformat)
  img = img.rgbSwapped()
  self.imgLabel.setPixmap(QPixmap.fromImage(img))
  self.imgLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
app = QApplication(sys.argv)
window = tehseencode()
window.show()
try:
  sys.exit(app.exec_())
except:
  print("exiting")

