import sys

from pysnark.runtime import snark, PrivVal

@snark
def equation(x):
    return x*x*x+x+5

print("output:", equation(int(sys.argv[1])))
