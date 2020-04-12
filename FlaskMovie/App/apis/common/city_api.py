from flask_restful import Resource, fields, marshal

from App.apis.api_constent import HTTP_OK
from App.models.common.city_model import City, Letter
# 对城市进行序列化
city_fields = {
    "id": fields.Integer(attribute='c_id'),
    "parentId": fields.Integer(attribute='c_parentId'),
    "regionName": fields.String(attribute='c_regionName'),
    "cityCode": fields.Integer(attribute='c_cityCode'),
    "pinYin": fields.String(attribute='c_pinYin')
}


class CitiesResource(Resource):

    def get(self):
        letters = Letter.query.all()
        letters_cities = {}
        letters_cities_fields = {}
        for letter in letters:
            letter_cities = City.query.filter_by(letter=letter.id)
            letters_cities[letter.letter] = letter_cities
            # 动态产生"A"
            letters_cities_fields[letter.letter] = fields.List(fields.Nested(city_fields))

            data = {
                "msg": "ok",
                "status": HTTP_OK,
                "data": marshal(letters_cities, letters_cities_fields)
            }
            return data