import re
from collections import Counter


f = open('access.log', 'r')
file = f.read()
f.close()
rule = re.compile("[0-9]{1,3}[\.][0-9]{1,3}[\.][0-9]{1,3}[\.][0-9]{1,3}")
IPs = list(re.findall(rule, file))
IPs.sort()
c = Counter(IPs)
print(c)
IPs[0].partition('*.*.*.')
