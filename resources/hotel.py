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
    def get(self):
        pass
    def post(self):
        pass
    def put(self):
        pass
    def delete(self):
        pass