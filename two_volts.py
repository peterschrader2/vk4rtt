import SM24b8vin
import math
sm24b = SM24b8vin.SM24b8vin(1)
val = round((sm24b.get_u_in(1) + 2.0), 2)
print(val)
