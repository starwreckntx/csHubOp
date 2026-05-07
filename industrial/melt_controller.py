# Melt Team Operational Controller - v2.1
# Managing Molten Metal Pours (40lbs to 3000lbs)

POUR_RATE = 150 # lbs per second
MAX_TEMP = 2800 # Fahrenheit
SHUTDOWN_THRESHOLD = 3000

def check_failsafe(temp):
    if temp > SHUTDOWN_THRESHOLD:
        print("CRITICAL: Failsafe triggered. Terminating Pour.")
        return False
    return True

def initiate_pour(weight):
    print(f"INITIATING {weight}lb POUR AT {POUR_RATE} lbs/sec")
    # Vulnerability: The Pour Rate is not sanitised against the temp threshold.
  
