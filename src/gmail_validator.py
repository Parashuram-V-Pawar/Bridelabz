# Program to validate Gmail addresses with exceptions
import re
def validate_gmail_address(email):
  try:
    pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
    if re.match(pattern, email):
        return True
    else:
        raise ValueError("Invalid Gmail address format.")
  except Exception as e:
    print(f"An error occurred: {e}")
    return False
  
email = input("Enter email: ")
result = validate_gmail_address(email)
print(result)