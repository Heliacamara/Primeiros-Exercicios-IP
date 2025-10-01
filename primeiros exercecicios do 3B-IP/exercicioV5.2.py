# @cikey f8a3d76c7a6f58f18a695f0148380a0a
# @sid 20251174010003
# @aid V5.2


#begin_inputs

minutos= 0
tartaruga= 1 * minutos +500
lebre=10 * minutos
#end_inputs

while tartaruga > lebre:
    tartaruga = round(tartaruga + 1)
    lebre = round(lebre + 10)
    minutos += 1
print("{}".format(minutos))

