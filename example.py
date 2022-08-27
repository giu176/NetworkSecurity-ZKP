import sys

from pysnark.runtime import snark, PrivVal

@snark
def calculate(x):
    return x*x*x+x+5

print("output:", calculate(int(sys.argv[1])))
