import mod1_test
from mod1_test import *
import mod2_test
import 패키지.echo

print(mod1_test.add(3,4))
print(__name__)

a = mod2_test.Math()
print(a.solv(2))
print(mod2_test.add(mod2_test.PI,4.4))