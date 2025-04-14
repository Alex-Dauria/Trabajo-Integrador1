import random  # Importamos la librería 'random' para generar números aleatorios.

print("¡Adivina el Número en Binario o Decimal segun corresponda!")  # Mostramos un mensaje de bienvenida al usuario.

while True:  # de esta manera iniciamos un bucle infinito, hasta que el usuario decida salir seleccionando la opcion correspondiente.
    opcion = input("Elige una opcion: '1' (Decimal a Binario), '2' (Binario a Decimal), '3' (Salir): ")  # Pedimos al usuario que ingrese una opción 
    
    if opcion == '3':  # si elije la opción 3.
        print("¡Nos vemos!")  # Muestra un mensaje de despedida.
        break  #de esta manera se  sale del bucle, terminando la ejecución del programa.
    elif opcion in ('1', '2'):  # Si la opción ingresada es '1' o '2'.
        numero_decimal = random.randint(1, 500)  # Generamos de esta manera, un número entero aleatorio entre 1 y 500 (inclusive) 
        #y lo asignamos a la variable 'numero_decimal'.
        numero_binario = bin(numero_decimal)[2:]  # usamos la función 'bin' para convertir el 'numero_decimal' a su representación
        #binaria y utilizamos el slicing [2:] para eliminar el prefijo "0b" que la función 'bin()' añade.

        if opcion == '1':  # Si la opción elegida fue '1' (convertir de Decimal a Binario).
            pregunta = f"Adivina el binario de {numero_decimal}: "  # Creamos una cadena de pregunta con 'f-string', 
            # mostrando el número decimal a convertir.
            respuesta_correcta = numero_binario  # Creamos variabe 'respuesta correcta' y le asignamos el valor binario correcto 
                                                 #(calculado previamente).
        else: # Si la opción elegida fue '2' (convertir de Binario a Decimal).
            pregunta = f"Adivina el decimal de {numero_binario}: "  # Creamos otra cadena de pregunta
                                                                    # mostrando el número binario a convertir.
            respuesta_correcta = numero_decimal  # Asignamos el valor decimal correcto a la variable 'respuesta_correcta'.

        adivinanza = input(pregunta)  # Mostramos la pregunta al usuario y guardamos su respuesta en la variable 'adivinanza'.
        if adivinanza == respuesta_correcta:  # Comparamos la respuesta del usuario con la respuesta correcta.
            print(f"¡Correcto! es equivalente a {respuesta_correcta}.")  # Si la respuesta es correcta, mostramos un mensaje de felicitación. 
        else:  # Si la respuesta del usuario es incorrecta.
            print(f"¡Incorrecto! es equivalente a {respuesta_correcta}.")  # Mostramos un mensaje indicando que la respuesta es incorrecta y damos la respuesta correcta.
    else:  # Si la opción ingresada por el usuario no es '1', '2' o '3'.
        print("Entrada inválida!")  # Muestra un mensaje de error indicando que la entrada del usuario no es válida.