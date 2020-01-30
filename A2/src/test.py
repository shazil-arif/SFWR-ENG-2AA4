from ChemTypes import ElementT
from ElmSet import ElemSet

e = ElementT.Og
print(e)

p = ElemSet([ElementT.H,ElementT.He])
for i in p:
    print(i)

