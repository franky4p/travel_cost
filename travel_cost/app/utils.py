import googlemaps
from datetime import datetime
from django.conf import settings

def get_hotel():
    gmaps = googlemaps.Client(key=settings.GOOGLE_API)

    # Geocoding an address
    addres = "Москва"
    geocode_result = gmaps.geocode(addres)
    location = geocode_result[0]['geometry']['location']

    # Request directions via public transit
    now = datetime.now()
    #directions_result = gmaps.directions("Sydney Town Hall","Parramatta, NSW", mode="transit", departure_time=now)

    place_result = gmaps.places_nearby(location=location, type="lodging", radius=5000)

    #гугл выводит 20 результатов, для получения следующих 20 нужно отправлять еще один запрос с токеном из place_result['next_page_token']
    result = place_result.get("results")

    return result

