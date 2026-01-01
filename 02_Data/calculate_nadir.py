from skyfield.api import Topos, load, EarthSatellite
from datetime import datetime

# The TLE data you just fetched
line1 = '1 25544U 98067A   25365.75865998  .00015131  00000+0  28223-3 0  9998'
line2 = '2 25544  51.6330  48.2919 0007527 325.0385  35.0108 15.48982944545803'
satellite = EarthSatellite(line1, line2, 'ISS (ZARYA)', load.timescale())

# Get current time
ts = load.timescale()
t = ts.now()

# Calculate position (Nadir Point)
geocentric = satellite.at(t)
subpoint = geocentric.subpoint()

print(f"--- ISS Real-Time Location ---")
print(f"Timestamp: {t.utc_strftime('%Y-%m-%d %H:%M:%S')} UTC")
print(f"Latitude:  {subpoint.latitude.degrees:.4f}")
print(f"Longitude: {subpoint.longitude.degrees:.4f}")
print(f"Altitude:  {subpoint.elevation.km:.2f} km")
