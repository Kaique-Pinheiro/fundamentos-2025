distancia = int(input("digite a distancia em km: "))

if distancia <= 200:
     custo = distancia * 0.5
else:
     custo = distancia * 0.45

print("o custo da viagem é de R$ %.2f" % custo)