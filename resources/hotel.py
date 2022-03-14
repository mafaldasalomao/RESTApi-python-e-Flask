from flask_restful import Resource

hoteis = [
    {
        'hotel_id': 'alpha',
        'nome':'alpha hotel',
        'estrelas': 4.5,
        'diaria': 343.00,
        'cidade':'Rio Branco'
    },
    {
        'hotel_id': 'beta',
        'nome':'beta hotel',
        'estrelas': 4,
        'diaria': 400.00,
        'cidade':'Rio Branco'
    },
    {
        'hotel_id': 'charlie',
        'nome':'charlie hotel',
        'estrelas': 4.6,
        'diaria': 300.00,
        'cidade':'Rio Branco'
    }
]
class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}

class Hotel(Resource):
    def get(self, hotel_id):
        for hotel in hoteis:
            if hotel_id==hotel['hotel_id']:
                return hotel
        return {'message': 'Hotel nao econtrado'}, 404

    def post(self, hotel_id):
        pass
    def put(self, hotel_id):
        pass
    def delete(self, hotel_id):
        pass