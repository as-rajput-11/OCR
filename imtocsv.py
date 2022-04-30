import easyocr
import csv

def createList(r1, r2):
    return list(range(r1, r2+1))

r1, r2 = 0, 8
list = createList(r1, r2)  

reader = easyocr.Reader(['en']) 
for i in list:
    result = reader.readtext('image/'+str(i)+'.jpg',detail=0)
    print(result)

    with open('1.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(result)