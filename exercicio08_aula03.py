import math

# Constantes
PI = 3.1415
COBERTURA_POR_LITRO = 3  # m² por litro
LITROS_POR_LATA = 5  # Litros por lata

# Preços das latas de tinta
PRECO_1_LATA = 50.00
PRECO_2_LATAS = 48.00
PRECO_3_LATAS = 46.00
PRECO_4_OU_MAIS = 45.00

# Entrada do usuário
try:
    raio = float(input("Digite o raio do cilindro (m): "))
    altura = float(input("Digite a altura do cilindro (m): "))

    if raio <= 0 or altura <= 0:
        print("O raio e a altura devem ser valores positivos.")
    else:
        # Cálculo das áreas
        area_base = PI * (raio * raio)  # π * r²
        perimetro = 2 * PI * raio  # 2πr
        area_lateral = altura * perimetro  # Altura * perímetro
        area_total = (2 * area_base) + area_lateral  # Duas bases + lateral

        # Cálculo da quantidade de tinta necessária
        litros_necessarios = area_total / COBERTURA_POR_LITRO
        latas_necessarias = math.ceil(litros_necessarios / LITROS_POR_LATA)  # Arredonda para cima

        # Cálculo do custo total com base na quantidade de latas
        if latas_necessarias == 1:
            custo_total = latas_necessarias * PRECO_1_LATA
        elif latas_necessarias == 2:
            custo_total = latas_necessarias * PRECO_2_LATAS
        elif latas_necessarias == 3:
            custo_total = latas_necessarias * PRECO_3_LATAS
        else:
            custo_total = latas_necessarias * PRECO_4_OU_MAIS

        # Exibição dos resultados
        print(f"\nÁrea total a ser pintada: {area_total:.2f} m²")
        print(f"Litros de tinta necessários: {litros_necessarios:.2f} L")
        print(f"Latas de tinta necessárias: {latas_necessarias}")
        print(f"Custo total: R$ {custo_total:.2f}")

except ValueError:
    print("Por favor, insira valores numéricos válidos.")
    