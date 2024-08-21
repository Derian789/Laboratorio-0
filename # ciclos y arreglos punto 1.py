# Función para calcular el BMI
def calcular_bmi(peso, altura):
    return peso / (altura ** 2)

# Solicitar el número de personas
num_personas = int(input("Ingrese el número de personas: "))

# Listas para almacenar pesos, alturas y BMIs
pesos = []
alturas = []
bmis = []

# Recopilar datos para cada persona
for i in range(num_personas):
    print(f"\nPersona {i+1}:")
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    
    # Almacenar peso y altura
    pesos.append(peso)
    alturas.append(altura)
    
    # Calcular y almacenar el BMI
    bmi = calcular_bmi(peso, altura)
    bmis.append(bmi)

# Imprimir los resultados para cada persona
print("\nResultados de BMI:")
for i in range(num_personas):
    print(f"Persona {i+1}: Peso: {pesos[i]} kg, Altura: {alturas[i]} m, BMI: {bmis[i]:.2f}")
