# @cikey f8a3d76c7a6f58f18a695f0148380a0a
# @sid 20251174010003
# @aid V5.3


#begin_inputs

 
#end_inputs
ceara_mirim = 73000
parnamirim = 250000
taipu = 12000

crescimento_ceara_mirim = 1.03
crescimento_taipu = 1.10
crescimento_parnamirim = 1.01

ano = 2018

while parnamirim >= ceara_mirim or parnamirim >= taipu:
    ceara_mirim = round(ceara_mirim * crescimento_ceara_mirim)
    taipu = round(taipu * crescimento_taipu)
    parnamirim = round(parnamirim * crescimento_parnamirim)
    ano += 1

print(f"Parnamirim sera a terceira cidade em: {ano}")
print(f"Populacao Parnamirim: {parnamirim}")
print(f"Populacao Ceara mirim: {ceara_mirim}")
print(f"Populacao Taipu: {taipu}")