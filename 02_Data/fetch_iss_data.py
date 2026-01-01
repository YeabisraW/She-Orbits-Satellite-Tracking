import requests

# URL for Space Stations (includes ISS)
ISS_TLE_URL = "https://celestrak.org/NORAD/elements/gp.php?GROUP=stations&FORMAT=tle"

def fetch_tle():
    print("Connecting to CelesTrak...")
    try:
        response = requests.get(ISS_TLE_URL)
        if response.status_code == 200:
            lines = response.text.splitlines()
            # The first 3 lines are usually the ISS
            iss_tle = lines[:3]
            print("\n--- Current ISS TLE Data ---")
            for line in iss_tle:
                print(line)
            return iss_tle
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fetch_tle()
