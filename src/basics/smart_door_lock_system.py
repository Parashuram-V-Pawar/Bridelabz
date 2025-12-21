# Problem Statement:
# Simulate a smart door lock system that allows a user
# up to 3 attempts to enter the correct PIN.
#
# Rules:
# 1. User is given exactly 3 attempts to enter the PIN
# 2. If any attempt matches the correct PIN → ACCESS GRANTED
# 3. If all 3 attempts are incorrect → LOCKED
#
# Input:
# correct_pin   # integer representing the correct PIN
# attempt1      # first PIN attempt
# attempt2      # second PIN attempt
# attempt3      # third PIN attempt
#
# Output:
# ACCESS GRANTED / LOCKED
#

def smart_door_lock_system(correct_pin):
  if len(str(correct_pin)) != 4 :
    print("Pin should be 4 digits")
    exit()
  else:
    attempts = 3
    while attempts > 0 :
      pin = int(input("Enter your 4 digit pin: "))
      if pin == correct_pin:
        return True
      else:
        print(f"Incorrect Pin, tries remaining: {attempts-1} ")
      attempts -= 1
    return False
  



correct_pin = int(input("Set 4 digit pin: "))
if correct_pin < 0:
  print("Pin cannot be negative value")
else:
  print("ACCESS GRANTED") if smart_door_lock_system(correct_pin) else print("LOCKED")
