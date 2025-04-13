# Importamos la biblioteca 'random'
import random
print("\n¡Bienvenido a nuestro juego de adivinanzas!\n")
# Definimos la función
def d_o_f():
    while True:
        # Pedimos al usuario que elija una opción en cada iteración:
        print("Ingrese una de las siguientes opciónes: ")
        decimal_o_binario = input("'1' De decimal a binario\n'2' De binario a decimal\n'3' para salir: ")

        # Si el usuario ingresa 3, salimos del loop
        if decimal_o_binario == "3":
            print("\nNos vemos!")
            break
        
        # Si el usuario ingresa 1, damos un número decimal y pedimos su equivalente en binario
        elif decimal_o_binario == "1":
            # Damos un valor aleatorio decimal
            numeroDecimal = random.randint (1, 500)
            # Transformamos el decimal a binario. bin() es una función para transformar un número a binario
            numeroBinario = bin(numeroDecimal)[2:] # Usamos [2:] para eliminar el prefijo "0b" y obtener solo los dígitos binarios

            adivinanza = input(f"\nAdivina qué número es {numeroDecimal} en binario: ")
            if adivinanza == numeroBinario:
                print(f"\nCorrecto! {numeroDecimal} es equivalente a {numeroBinario} en binario.\n")
            else:
                print(f"\nIncorrecto! {numeroDecimal} es equivalente a {numeroBinario} en binario.\n")

        # Si el usuario ingresa 2, damos un número binario y pedimos su equivalente en decimal
        elif decimal_o_binario == "2":
            # Damos un valor aleatorio decimal
            numeroDecimal = random.randint (1, 500)
            # Transformamos el decimal a binario
            numeroBinario = bin(numeroDecimal)[2:] # Usamos [2:] para eliminar el prefijo "0b" y obtener solo los dígitos binarios

            adivinanza = input(f"\nAdivina qué número es {numeroBinario} en decimal: ")
            if adivinanza == str(numeroDecimal):
                print(f"\nCorrecto! {numeroBinario} es equivalente a {numeroDecimal} en decimal.\n")
            else:
                print(f"\nIncorrecto! {numeroBinario} es equivalente a {numeroDecimal} en decimal.\n")
        
        # Si el usuario ingresa otra cosa le recordamos las opciones
        else:
            print("\nEntrada invalida!\n")

# Llamamos a la función
d_o_f()
