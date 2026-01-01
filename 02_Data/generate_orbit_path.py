import requests
import pandas as pd
from skyfield.api import load, EarthSatellite
from datetime import datetime, timedelta

# 1. Fetch live TLE
url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=stations&FORMAT=tle"
lines = requests.get(url).text.splitlines()
name, l1, l2 = lines[0], lines[1], lines[2]

# 2. Setup Propagation
ts = load.timescale()
satellite = EarthSatellite(l1, l2, name, ts)
start_time = ts.now()

# 3. Generate 100 points (approx 1 full orbit)
data = []
for i in range(100):
    # Move forward in 1-minute increments
    time = start_time + timedelta(minutes=i)
    geocentric = satellite.at(time)
    subpoint = geocentric.subpoint()
    
    data.append({
        'minute': i,
        'lat': subpoint.latitude.degrees,
        'lon': subpoint.longitude.degrees
    })

# 4. Save to CSV for the tutorial
df = pd.DataFrame(data)
df.to_csv('02_Data/iss_orbit_path.csv', index=False)
print("✅ Successfully generated 100-minute orbit path in 02_Data/iss_orbit_path.csv")
