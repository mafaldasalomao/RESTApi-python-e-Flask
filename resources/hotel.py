from flask_restful import Resource, reqparse

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
    def find_hotel(hotel_id):
        for hotel in hoteis:
            if hotel_id==hotel['hotel_id']:
                return hotel
        return None
    def get(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            return hotel
        return {'message': 'Hotel nao encontrado'}, 404

    def post(self, hotel_id):
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('nome')
        argumentos.add_argument('estrelas')
        argumentos.add_argument('diaria')
        argumentos.add_argument('cidade')
        dados = argumentos.parse_args()

        novo_hotel = {
            'hotel_id': 'delta',
            'nome': dados['nome'],
            'estrelas': dados['estrelas'],
            'diaria': dados['diaria'],
            'cidade': dados['cidade']
        }

        hoteis.append(novo_hotel)
        return novo_hotel, 200

    def put(self, hotel_id):
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('nome')
        argumentos.add_argument('estrelas')
        argumentos.add_argument('diaria')
        argumentos.add_argument('cidade')
        dados = argumentos.parse_args()

        novo_hotel = {
            'hotel_id': 'delta',
            'nome': dados['nome'],
            'estrelas': dados['estrelas'],
            'diaria': dados['diaria'],
            'cidade': dados['cidade']
        }
        return novo_hotel, 200
    def delete(self, hotel_id):
        pass