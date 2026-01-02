import re


exp = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$%^&+=]).+$'
if re.match(exp, "Parashu8050@"):
    print(True)
else:
    print(False)