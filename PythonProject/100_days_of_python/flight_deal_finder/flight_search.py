import requests as rt


class FlightSearch:
    def __init__(self):
        self.api_key = "UskuAWq8XMkjTiVTGijP3AOZJDU7EK9I",
        self.api_secret = "A6aqB7YZwkcwQNh6",
        self.access_token = "u3IDxPOpn2NMLmg74aYrPJ6KeaAM"
        self.Headers = {}
        self.generate_new_token()

    def generate_new_token(self):
        token_url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        # Note: Use 'data=' for x-www-form-urlencoded
        token_headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        token_data = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.api_secret
        }
        response = rt.post(url=token_url, data=token_data, headers=token_headers)

        if response.status_code == 200:
            self.access_token = response.json()["access_token"]
            # IMPORTANT: The space after 'Bearer ' is mandatory
            self.Headers = {
                "Authorization": f"Bearer {self.access_token}"
            }
            print(f"Token Refresh Successful. Token starts with: {self.access_token[:10]}...")
        else:
            print(f"FAILED TO GET TOKEN: {response.status_code}")
            # print(response.text)

    def get_iata(self,city):
        iata_params = {
            "keyword": city["city"],
            "max": "2",
            "include": "AIRPORTS",
        }
        response = rt.get("https://test.api.amadeus.com/v1/reference-data/locations/cities", headers=self.Headers, params=iata_params)
        print(self.Headers)
        if response.status_code == 401:
            self.generate_new_token()
            # RECURSION: The headers are now updated, so this call will work!
            return self.get_iata(city["city"])

            # CASE B: Successful search
        if response.status_code == 200:
            data = response.json().get("data", [])
            if data:
                return data[0]["iataCode"]

            # CASE C: City not found or other error
        print(f"No IATA found for {city["city"]}.")
        return "N/A"

    def search_flight(self, origin_city_code, destination_city_code, from_time,to_time):
        # Use the V2 Search API - much more stable!
        flight_search_api = "https://test.api.amadeus.com/v2/shopping/flight-offers"

        query_params = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": 1
        }

        response = rt.get(url=flight_search_api, headers=self.Headers, params=query_params)

        # Handle Token Expiry here too!
        if response.status_code == 401:
            self.generate_new_token()
            return self.search_flight(origin_city_code, destination_city_code, from_time,to_time)

        if response.status_code == 200:
            # print(response.status_code)
            # print(response.json())
            return response.json()


        else:
            print(f"Search failed with status: {response.status_code}")
            # print(response.text)
            return None

