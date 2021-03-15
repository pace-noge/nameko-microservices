import json

from nameko.rpc import RpcProxy
from nameko.web.handlers import http


class GatewayService:
    name= 'gateway'

    airports_rpc = RpcProxy('airport_service')
    trips_rpc = RpcProxy('trips_service')

    @http('GET', '/airport/<string:airport_id>')
    def get_airport(self, request, airport_id):
        airport = self.airports_rpc.get(airport_id)
        return json.dumps({'airport': airport})

    @http('POST', '/airports')
    def post_airport(self, request):
        data = json.loads(request.get_data(as_text=True))
        airport_id = self.airports_rpc.create(data['airport'])

        return airport_id

    @http('GET', '/airports')
    def airport_list(self, request):
        airports = self.airports_rpc.load_airports()
        return json.dumps(airports)

    @http('GET', '/trip/<string:trip_id>')
    def get_trip(self, request, trip_id):
        trip = self.trips_rpc.get(trip_id)
        return json.dumps({"trip": trip})

    @http('POST', '/trips')
    def post_trip(self, request):
        data = json.loads(request.get_data(as_text=True))
        trip_id = self.trips_rpc.create(data['from'], data['to'])

        return trip_id

    @http('GET', '/trips')
    def trip_list(self, request):
        trips = self.trips_rpc.load_trips()
        return json.dumps(trips)

