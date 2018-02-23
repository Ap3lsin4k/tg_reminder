import g
from g import var as var
var = 1
print(var)

def out():
    var = 2
    print(var)

out()
print(var)
g.data_output()
