import fastf1
import matplotlib.pyplot as plt

# Save downloaded data locally so we don't re-download every
fastf1.Cache.enable_cache("cache")

# Get qualifying from Tokyo 2025 (
session = fastf1.get_session(2025, "Tokyo", "Q")
session.load()

#Hamiliton fastest lap and its telemetry
laps = session.laps.pick_drivers("HAM").pick_fastest()
telemetry = laps.get_car_data()
telemetry = telemetry.add_distance()

print(telemetry[['Distance', 'Speed', 'Throttle', 'Brake', 'nGear']].head())

#Draw speed vs. distance 
plt.plot(telemetry["Distance"], telemetry["Speed"])
plt.xlabel("Distance (m)")
plt.ylabel("Speed (km/h)")
plt.title("hamilton - Tokyo Quali, fastest lap")
plt.show()