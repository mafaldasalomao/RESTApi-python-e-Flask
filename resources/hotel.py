from flask_restful import Resource, reqparse
from models.hotel import HotelModel
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
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')
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
        dados = Hotel.argumentos.parse_args()
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()
        # novo_hotel = {'hotel_id': 'delta', **dados}
        hoteis.append(novo_hotel)
        return novo_hotel, 200

    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200
        hoteis.append(novo_hotel)
        return novo_hotel, 201


    def delete(self, hotel_id):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
        return {'message':'Hotel deleted.'}