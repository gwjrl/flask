# 导入城市脚本
import json

import pymysql


def load_data():
    with open('cities.json', 'r', encoding='UTF-8') as city_json_file:
        cities_json_str = city_json_file.read()
        city_json = json.loads(cities_json_str)
    return city_json

def insert_cities(citie_json):
    cities = citie_json.get("returnValue")
    keys = cities.keys()
    # 连接数据库
    db = pymysql.Connect(host='121.43.43.59', port=3306, user='root', password='GL@LT', database='ToPo', charset='utf8mb4')
    cursor = db.cursor()

    for key in keys:

        cursor.execute("INSERT INTO letter(letter) VALUES ('%s');" % key)
        db.commit()
        cursor.execute("SELECT letter.id FROM letter WHERE letter='%s'" % key)
        letter = cursor.fetchone()[0]
        cities_letter = cities.get(key)

        for city in cities_letter:
            c_id = city.get('id')
            c_parentId = city.get('parentId')
            c_regionName = city.get('regionName')
            c_cityCode = city.get('cityCode')
            c_pinYin = city.get('pinYin')
            cursor.execute("INSERT INTO city(letter, c_id, c_parentId, c_regionName, c_cityCode, c_pinYin) VALUES (%d, %d, %d, '%s', %d, '%s');" % (letter, c_id, c_parentId, c_regionName, c_cityCode, c_pinYin))
            db.commit()

if __name__ == '__main__':
    cities_json = load_data()
    insert_cities(cities_json)