import easyocr
import cv2

reader = easyocr.Reader(['en'])
result = reader.readtext('6.png',paragraph=True)
result

import matplotlib.pyplot as plt
import cv2
top_left = tuple(result[0][0][0])
bottom_right = tuple(result[0][0][2])
text = result[0][1]
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.imread('6.png')
spacer = 300
font = cv2.FONT_HERSHEY_SIMPLEX
for detection in result: 
    top_left = tuple(detection[0][0])
    bottom_right = tuple(detection[0][2])
    text = detection[1]
    img = cv2.rectangle(img,top_left,bottom_right,(0,255,0),3)
    #img = cv2.putText(img,text,(20,spacer), font, 0.5,(255,255,0),2,cv2.LINE_AA)
    spacer+=15
plt.figure(figsize=(10,10))
plt.imshow(img)
plt.show()
with open('Refs.txt', 'w',encoding='utf-8') as f:
    for i in result:
        f.write(i[1])
        f.write('\n')
        print(i[1])
# with open("output.txt", "w") as f:
#     for line in :
#         print(line, file=f)


