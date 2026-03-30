from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from flight_data import get_cheapest_flight
import time

gsheet_data = DataManager()
cities = gsheet_data.get_data()
flight_search = FlightSearch()
ORIGIN_CITY_IATA = "LON"

###------------------------------------------------------------IATA CODE GENERATION------------------------------------------------------------###
# for city in cities:
#     iata_code = flight_search.get_iata(city)
#     city["iataCode"] = iata_code
#     gsheet_data.update_data(city["id"],city,"iataCode")


###-----------------------------------------------------------------FLIGHT SEARCH-------------------------------------------------------------###
tomorrow = datetime.now() + timedelta(days=1)
six_months_from_now = tomorrow + timedelta(days=180)

for destination in cities:
    flights = flight_search.search_flight(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_now
    )
    cheapest_flight = get_cheapest_flight(flights)
    try:
        if int(cheapest_flight.price) < int(destination["lowestPrice"]):
            print(f"cheapest flight found for {destination['city']} from london! new price: {cheapest_flight.price}, old price: {destination['lowestPrice']}")
            destination["lowestPrice"] = cheapest_flight
            gsheet_data.update_data(destination["id"], destination, "lowestPrice")
    except:
        pass

    print(f"{destination['city']}: £{cheapest_flight.price}")
    # Slowing down requests to avoid rate limit
    time.sleep(2)



#{'city': 'Phuket', 'iataCode': 'HKT', 'lowestPrice': 54, 'id': 2}