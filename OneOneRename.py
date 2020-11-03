import re
s = ('1.der','10.sgs','5.rsts','4dasf')
new = sorted(s,key = lambda i:int(re.match(r'(\d+)',i).group()))
print(new)