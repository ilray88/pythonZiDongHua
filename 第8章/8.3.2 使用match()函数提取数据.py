import re
str = '123**?Qwe!_@#你我他'
result = re.match('\w', str)
value = result.group()
print(value)
