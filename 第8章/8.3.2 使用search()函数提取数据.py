import re
str = '**8!123**?Qwe!_@#你我他'
result = re.search('\w', str)
value = result.group()
location = result.span()
print(value)
print(location)
