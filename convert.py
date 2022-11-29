import json
import csv
import codecs
import re

def generateNewCsv():
    jsonData = codecs.open('new-house.json', 'r', 'utf-8')
    csvfile = open('new.csv', 'w', newline='')
    writer = csv.writer(csvfile, delimiter=',')
    keys = ['name', 'house_type', 'position', 'room_type', 'area', 'unit_price', 'total_price']
    writer.writerow(keys)
    for line in jsonData:
        dic = json.loads(line)
        name = dic['name'][0]
        house_type = dic['house_type'][0]
        position = dic['position'][0]
        if dic['room_type'] == []:
            room_type = ''
        else:
            room_type = 0
            for item in dic['room_type']:
                room_type += int(re.findall(r"\d+", item)[0])
            room_type /= len(dic['room_type'])
            room_type = str(int(room_type))
        if dic['area'] == []:
            area = ''
        else:
            area = 0
            ls = re.findall(r"\d+", dic['area'][0])
            for num in ls:
                area += int(num)
            area /= len(ls)
            area = str(int(area))
        unit_price = str(int(re.findall(r"\d+", dic['unit_price'][0])[0]))
        if dic['total_price'] == []:
            total_price = ''
        else:
            total_price = 0
            ls = re.findall(r"\d+", dic['total_price'][0])
            for num in ls:
                total_price += int(num)
            total_price /= len(ls)
            total_price = str(int(total_price))
        writer.writerow([name, house_type, position, room_type, area, unit_price, total_price])
    jsonData.close()
    csvfile.close()

if __name__ == '__main__':
    generateNewCsv()