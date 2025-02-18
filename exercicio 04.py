taxa = float(input("digite o calor da hora de trabalho: "))
horas = int(input("digite a quantidade de horas trabalhadas no mes: "))

print()

salario_bruto = (taxa * horas)
print("+ salario bruto: R$ %.2f" % salario_bruto)
imposto_renda = salario_bruto * (11/100)
print("- imposto de renda: R$ (11%%) R$ %.2f" % imposto_renda)
inss = salario_bruto * (8/100)
print("- inss: (8%%): R$ %.2f" % inss)
sindicato = salario_bruto * (5/100)
print("- sindicato: (5%%): R$ %.2f" % sindicato)
salario_liquido = salario_bruto - imposto_renda - inss - sindicato
print("= salario liquido: R$ %.2f" % salario_liquido)