import re
m = re.compile('<div>([0-9]{0,4})mm x ([0-9]{0,4})mm x ([0-9]{0,4})mm</div>')
find = m.match( '<div>125mm x 8mm x 1212mm</div>')
print(find.group(3))