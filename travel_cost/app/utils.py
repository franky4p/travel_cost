import googlemaps
from datetime import datetime
from django.conf import settings

def get_info(type_s, addres):
    gmaps = googlemaps.Client(key=settings.GOOGLE_API)

    # Geocoding an address
    if addres:
        geocode_result = gmaps.geocode(addres)
    else:
        geocode_result = gmaps.geocode("Москва")
    
    location = geocode_result[0]['geometry']['location']

    if type_s:
        place_result = gmaps.places_nearby(location=location, type=type_s, radius=5000)
    else:
        place_result = gmaps.places_nearby(location=location, type="lodging", radius=5000)

    #гугл выводит 20 результатов, для получения следующих 20 нужно отправлять еще один запрос с токеном из place_result['next_page_token']
    result = place_result.get("results")

    return result