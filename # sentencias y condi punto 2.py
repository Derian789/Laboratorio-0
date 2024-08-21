# Entrada de datos
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

# Cálculo del BMI
bmi = peso / (altura ** 2)

# Mostrar el BMI
print(f"Su BMI es: {bmi:.2f}")

# Clasificación del BMI
if bmi < 18.5:
    print("Usted está en la categoría de bajo peso.")
elif 18.5 <= bmi < 24.9:
    print("Usted está en la categoría de peso normal.")
elif 25.0 <= bmi < 29.9:
    print("Usted está en la categoría de sobrepeso.")
else:
    print("Usted está en la categoría de obesidad.")
