import re
str = '123Qwe!_@#你我他'
result = re.finditer('\w', str)
for i in result:
    value = i.group()
    print(value)

