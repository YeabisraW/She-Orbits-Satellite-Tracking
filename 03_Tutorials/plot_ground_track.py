import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the data you generated
df = pd.read_csv('02_Data/iss_orbit_path.csv')

# 2. Create the plot
plt.figure(figsize=(12, 6))
plt.plot(df['lon'], df['lat'], 'ro-', markersize=2, label='ISS Path')

# 3. Add formatting to make it look like a World Map
plt.title('ISS Ground Track - 100 Minute Orbit (Week 3)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True, linestyle='--', alpha=0.5)
plt.axhline(0, color='black', linewidth=1) # Equator
plt.legend()

# 4. Save the result to Media folder
plt.savefig('Media/iss_ground_track_plot.png')
print("✅ Visualization saved to Media/iss_ground_track_plot.png")
plt.show()
