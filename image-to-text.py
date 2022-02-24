from PIL import Image
from matplotlib.pyplot import text
import pytesseract
im = Image.open("image.jpg")
text = pytesseract.image_to_string(im,lang="eng",)

print(text)