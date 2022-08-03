#Entrada
quant_c = int(input())
candidatos = []
num_votos = []
for i in range(quant_c):
    candidatos.append(input())
for i in range((quant_c + 2)):
    num_votos.append(int(input()))

#Leitura dos dados
total_v = sum(num_votos)
votos_inv = sum(num_votos[-2:])
votos_val = num_votos[:-2]
quant_vv = total_v - votos_inv
seg_turno = sorted(votos_val)
a = votos_val.index(seg_turno[-1])
b = votos_val.index(seg_turno[-2])

vencedor = []
if seg_turno[-1] > (sum(votos_val)/2):
    p = votos_val.index(max(votos_val))
    vencedor.append(candidatos[p])

if len(vencedor) != 0:
    print(vencedor[0], "foi o vencedor da eleição")
else:
    print("Haverá segundo turno entre:")
    print(candidatos[a])
    print(candidatos[b])

#Saída
print("Total de votos:", total_v)
print("Votos válidos:", sum(votos_val))
