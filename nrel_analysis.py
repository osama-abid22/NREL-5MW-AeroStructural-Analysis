import numpy as np
import matplotlib.pyplot as plt

# Simple sample data (to guarantee the script works)
wind_speed = np.array([3, 5, 7, 9, 11, 13, 15, 17])
power_kw = np.array([0, 50, 200, 500, 1200, 2000, 3000, 3500])

plt.figure(figsize=(8, 5))
plt.plot(wind_speed, power_kw, linewidth=2)
plt.title("Test Wind Turbine Power Curve")
plt.xlabel("Wind Speed (m/s)")
plt.ylabel("Power Output (kW)")
plt.grid(True)

plt.savefig("power_curve_test.png", dpi=300)
print("✔ Plot generated successfully: power_curve_test.png")
