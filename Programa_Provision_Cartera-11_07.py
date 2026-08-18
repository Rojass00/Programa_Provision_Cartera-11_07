def calcular_provision_general(dias, valor):
  # Tabla de referencia (similar a la de Excel de mayor a menor)
  # (Días mínimos para aplicar el porcentaje, Porcentaje)
  rangos = [(366, 0.15), (181, 0.10), (90, 0.05), (0, 0.00)]

  porcentaje_aplicado = 0.0

  # Busca el rango correspondiente (equivalente a BUSCARV con VERDADERO)
  for limite_inferior, porcentaje in rangos:
    if dias >= limite_inferior:
      porcentaje_aplicado = porcentaje
      break

  # Calcula el valor de la provisión
  valor_provision = valor * porcentaje_aplicado
  return porcentaje_aplicado, valor_provision


if __name__ == "__main__":
  print("=== CALCULADORA DE PROVISIÓN DE CARTERA ===")
  try:
    dias_mora = int(input("Ingrese los días de mora: "))
    valor_deuda = float(input("Ingrese el valor de la deuda: "))

    porcentaje, resultado = calcular_provision_general(dias_mora, valor_deuda)

    print("\n--- Resultados ---")
    print(f"Porcentaje aplicado: {porcentaje * 100:.0f}%")
    print(f"Valor a provisionar: ${resultado:,.2f}")

  except ValueError:
    print("Error: Por favor ingrese números válidos para los días y el valor.")