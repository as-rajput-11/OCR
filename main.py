from tracemalloc import get_object_traceback
import cv2
import easyocr
import matplotlib.pyplot as plt
import numpy as np
from pyproj import Transformer
import os
import json


os.environ["CUDA_VISIBLE_DEVICES"] = ""

_easyocr = easyocr.Reader(["en"])

transformer = Transformer.from_crs(24379, 4326)

# img = cv2.imread("Handycam.JPG")
img = cv2.imread("0.jpg")

start_x, start_y = 440, 25
end_x, end_y = 890, 62



# start_x, start_y = 440, 155
# end_x, end_y = 634, 475
# 194x320


img = img[start_y: end_y, start_x: end_x]
# img = cv2.resize(img, (400, 660))
cv2.imwrite('resized.jpg', img)

result = _easyocr.readtext(np.array(img))

keywords = {
    'E': 1,
    'N': 1,
    'range': 1,
    'az': 1,
    'speed': 2,
    'heading': 1
}
detections = {}
i = 0


def does_contain(text):
    for k, v in keywords.items():
        if k in text:
            return k, v



# for result in results:
#     box = result[0]
#     text = result[1].lower().strip()
#     img = cv2.rectangle(img, (box[0][0], box[0][1]), (box[2][0], box[2][1]), (0, 0, 255), 1)
#     img = cv2.putText(img, text, (box[0][0], box[0][1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
# top_left = tuple(result[0][0][0])
# bottom_right = tuple(result[0][0][2])
# text = result[0][1]
# font = cv2.FONT_HERSHEY_SIMPLEX
# img = cv2.imread('output.jpg')
# # img.shape()
# spacer = 300
# font = cv2.FONT_HERSHEY_SIMPLEX
# for detection in result:
#     top_left = tuple(detection[0][0])
#     bottom_right = tuple(detection[0][2])
#     text = detection[1]
#     img = cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 3)
#     #img = cv2.putText(img,text,(20,spacer), font, 0.5,(255,255,0),2,cv2.LINE_AA)
#     spacer += 15
# plt.figure(figsize=(10, 10))
# plt.imshow(img)
# plt.show()



# print(result)

for i in result:
    # print(i[1])
    # list.append(i[1])
    E_N=(i[1].replace("Z","2").replace("D","0").replace("E","6").replace("A","3").replace("T","7"))
    E_N = (E_N.replace("6","E",1))
    # word = re.findall("^E...\w+",bbb)
    E_N = (E_N.replace("E","E,").replace("N",",N,"))
    # print(E_N)

    # E_N="".join(E_N)
    E_N=E_N.split(",")
    # E_N="\n".join(E_N)
    # E_N = (E_N.replace(" ",""))
    # print(E_N)
    it = iter(E_N)
    res_dct = dict(zip(it, it))
    # print(res_dct)

# while i < len(results):
#     box = results[i][0]
#     text = results[i][1].lower().strip()
#     ret = does_contain(text)
#     if ret is not None:
#         detections[ret[0]] = results[i + ret[1]][1].lower().strip()
#         i += ret[1]
#     i += 1
    # img = cv2.rectangle(img, (box[0][0], box[0][1]), (box[2][0], box[2][1]), (0, 0, 255), 1)
    # img = cv2.putText(img, text, (box[0][0], box[0][1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)

lt=[]


geojson = {"type": "FeatureCollection", "features": []}


dic = {'type': 'FeatureCollection','features':[{'type':'Feature','properties':{},'geometry': {'type': 'Point','coordinates': []}}]}
geo = dic['features'][0]['geometry']['coordinates']
print(geo)
point_43279 = [(float(res_dct['E']), float(res_dct['N']))]

# # print(lt)
# print(point_43279)
point_4326 = transformer.itransform(point_43279)
point_4326 = (tuple(reversed(x)) for x in point_4326) 
# print(point_4326)
# # geo.append(*point_4326)
# print(geo)
l = []
for i in point_4326:
#     print(i)
    for j in i:
        # print(j)
        geo.append(j)
#         feature = {"type": "Feature", "geometry": {"type": "Point", "coordinates": []}, "properties": {}}
#         geojson['features'].append(j)
# with open('geojson13.geojson', 'w') as fp:
#     json.dump(geojson, fp) 


# print(geo)
# print(type(geo))
# geo.append(print(*point_4326))
print(dic)
dp = json.dumps(dic)
print(dp)
with open('geojson33.geojson','w') as file:
    json.dump(dic,file)
# print(geo)
# plt.imshow(img)
# plt.show()
cv2.imwrite('out.jpg', img)
# print(detections)




# geojson = {"type": "FeatureCollection", "features": []}

    
# for _, row in udx.iterrows():
    
#     feature = {"type": "Feature", "geometry": {"type": "Point", "coordinates": [row['LOGITUDE'], row['LATITUDE']]}, "properties": {"STATION CO": row['STATION CO'],"STATION FU": row['STATION FU'],"Remarks":str(row['Remarks'])}}
#     geojson['features'].append(feature)

# with open('geojson11.geojson', 'w') as fp:
#     json.dump(geojson, fp) 


# print('-------filesaved---------')
