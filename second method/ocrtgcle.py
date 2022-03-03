import matplotlib.pyplot as plt
import cv2
import easyocr
from pylab import rcParams
from IPython.display import Image
rcParams['figure.figsize'] =20,16
reader = easyocr.Reader(['en'])
# file_name = "/home/bisag/Downloads/ocr/second method/6.png"
file_name = "6.png"
Image(file_name)
output = reader.readtext(file_name)
output
cord = output[0][0]
x_min, y_min =[int(min(idx)) for idx in zip(*cord)]
x_max, y_max =[int(min(idx)) for idx in zip(*cord)]
image = cv2.imread(file_name)
cv2.rectangle(image,(x_min,y_min),(x_max,y_max),(255,0,0),1)
plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
