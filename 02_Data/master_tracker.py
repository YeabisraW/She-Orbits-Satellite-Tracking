import requests
from skyfield.api import load, EarthSatellite

def get_live_iss_position():
    # 1. Fetch live TLE
    url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=stations&FORMAT=tle"
    response = requests.get(url)
    lines = response.text.splitlines()
    
    # Extract ISS (usually first 3 lines)
    name, line1, line2 = lines[0], lines[1], lines[2]
    
    # 2. Propagate to now
    ts = load.timescale()
    satellite = EarthSatellite(line1, line2, name, ts)
    geocentric = satellite.at(ts.now())
    subpoint = geocentric.subpoint()
    
    print(f"\n🚀 {name} FOUND")
    print(f"LAT: {subpoint.latitude.degrees:.2f}")
    print(f"LON: {subpoint.longitude.degrees:.2f}")
    print(f"ALT: {subpoint.elevation.km:.2f} km")

if __name__ == "__main__":
    get_live_iss_position()
