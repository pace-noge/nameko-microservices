import uuid
import json

from nameko.rpc import rpc
from nameko_redis import Redis


class AirportServices:
    name = "airport_service"

    redis = Redis('development')

    @rpc
    def get(self, airport_id):
        airport = self.redis.get(airport_id)
        return airport


    @rpc
    def create(self, airport):
        airport_id = uuid.uuid4().hex
        self.redis.set(airport_id, airport)
        airports = self.redis.get('airports')
        if airports:
            airports = json.loads(airports)
        else:
            airports = []
        airports.append({"airport_id": airport_id, "airport": airport})
        self.redis.set('airports', json.dumps(airports))
        return airport_id

    @rpc
    def load_airports(self):
        airports = self.redis.get('airports')
        return json.loads(self.redis.get('airports'))


