import os
import requests

API_KEY = os.getenv("OMDB_API_KEY", "d01064d6")


def get_movie_rating():
    movie_name = input("Enter the name of the movie: ")

    url = "https://www.omdbapi.com/"
    params = {
        "t": movie_name,
        "apikey": API_KEY,
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data.get("Response") == "True":
            print("\nMovie Name:", data.get("Title"))
            print("Year:", data.get("Year"))
            print("IMDb Rating:", data.get("imdbRating"))
        else:
            print("Movie not found:", data.get("Error"))

    except requests.RequestException as e:
        print("Connection error:", e)


if __name__ == "__main__":
    get_movie_rating()