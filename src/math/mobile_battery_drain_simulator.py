# Problem Statement:
# Simulate mobile battery drain based on app usage.
#
# - The battery starts at 100%.
# - Each app drains a fixed percentage per minute (drain_per_minute).
# - The simulation stops when battery level becomes less than or equal to 0.
# - Print the total number of minutes the battery lasted.
#
# Input:
# drain_per_minute   # integer or float, percentage drained per minute
#
# Output:
# minutes           # total minutes before battery reaches 0 or below
#

def mobile_battery_drain_simulator(drain_per_minute):
  minutes = 0
  battery = 100
  while battery > 0:
    minutes += 1
    battery -= drain_per_minute
  return minutes

drain_per_minute = float(input("Enter drain per minute: "))
print(mobile_battery_drain_simulator(drain_per_minute))
