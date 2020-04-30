import math


def calcSinCosTan(x):
    sine = math.sin(x)
    cos = math.cos(x)
    tan = math.tan(x)
    return [sine, cos, tan]


print(calcSinCosTan(0))
print("Sine", calcSinCosTan(-1))
print("cosine", calcSinCosTan(0))
print("tan", calcSinCosTan(1))
