#0x02-python-import_modules/1-calculation.py

from calculator_1 import add , sub , mul , div 

a = 10 
b = 5 


print("{} + {} = {}".format(a,b,add(a,b)))
print("{} - {} = {}".format(a,b,sub(a,b)))
print("{} * {} = {}".format(a,b,mul(a,b)))
print("{} / {} = {}".format(a,b,div(a,b)))
