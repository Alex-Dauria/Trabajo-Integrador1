# Importamos la biblioteca 'random'
import random

# Definimos la función
def d_o_f():
    while True:
        # Pedimos al usuario que elija en cada iteración:
        decimal_o_binario = input("Escribe '1' para Decimal, '2' para Binario, '3' para salir: ")

        # Si el usuario ingresa 3, salimos del loop
        if decimal_o_binario == "3":
            print("Nos vemos!")
            break

        # Si el usuario ingresa 1, damos un número decimal y pedimos su equivalente en binario
        elif decimal_o_binario == "1":
            # Damos un valor aleatorio decimal
            numeroDecimal = random.randint (1, 500)
            # Transformamos el decimal a binario
            numeroBinario = bin(numeroDecimal)[2:] # Usamos [2:] para eliminar el prefijo "0b" y obtener solo los dígitos binarios

            adivinanza = input(f"Adivina qué número sería {numeroDecimal} en binario: ")
            if adivinanza == numeroBinario:
                print(f"Correcto! {numeroDecimal} es equivalente a {numeroBinario} en binario.")
            else:
                print(f"Incorrecto! {numeroDecimal} es equivalente a {numeroBinario} en binario.")

        # Si el usuario ingresa 2, damos un número binario y pedimos su equivalente en decimal
        elif decimal_o_binario == "2":
            # Damos un valor aleatorio decimal
            numeroDecimal = random.randint (1, 500)
            # Transformamos el decimal a binario
            numeroBinario = bin(numeroDecimal)[2:] # Usamos [2:] para eliminar el prefijo "0b" y obtener solo los dígitos binarios

            adivinanza = input(f"Adivina qué número sería {numeroBinario} en decimal: ")
            if adivinanza == str(numeroDecimal):
                print(f"Correcto! {numeroBinario} es equivalente a {numeroDecimal} en decimal.")
            else:
                print(f"Incorrecto! {numeroBinario} es equivalente a {numeroDecimal} en decimal.")
        
        # Si el usuario ingresa otra cosa le recordamos las opciones
        else:
            print("Entrada invalida!")

# Llamamos a la función
d_o_f()
