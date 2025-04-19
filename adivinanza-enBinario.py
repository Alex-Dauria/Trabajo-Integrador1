import random  # Importamos la librería 'random' para generar números aleatorios.

print("¡Adivina el Número en Binario o Decimal segun corresponda!")  # Mostramos un mensaje de bienvenida al usuario.

while True:  # de esta manera iniciamos un bucle infinito, hasta que el usuario decida salir seleccionando la opcion correspondiente.
    opcion = input("Elige una opcion: '1' (Decimal a Binario), '2' (Binario a Decimal), '3' (Salir): ")  # Pedimos al usuario que ingrese una opción

    if opcion == '3':  # si elije la opción 3.
        print("¡Nos vemos!")  # Muestra un mensaje de despedida.
        break  # de esta manera se  sale del bucle, terminando la ejecución del programa.
    elif opcion == '1' or opcion == '2':  # Si la opción ingresada es '1' o '2'.
        numero_decimal = random.randint(1, 500)  # Generamos de esta manera, un número entero aleatorio entre 1 y 500 (inclusive)
        # y lo asignamos a la variable 'numero_decimal'.
       
        numero_binario = ""  # Inicializamos la cadena binaria vacía.
        decimal = numero_decimal  # Guarda el decimal original para calcular el binario sin alterarlo.
        while decimal > 0:  # Repite hasta que el decimal se reduzca a cero.
            residuo = decimal % 2  # Obtiene el bit menos significativo (0 o 1).
            numero_binario = str(residuo) + numero_binario  # Agrega el bit al inicio de la cadena binaria.
            decimal //= 2  # Divide el decimal por 2 (división entera) para el siguiente bit.

        if opcion == '1':  # Si la opción elegida fue '1' (convertir de Decimal a Binario).
            pregunta = f"Adivina el binario de {numero_decimal}: "  # Creamos una cadena de pregunta con 'f-string',
            # mostrando el número decimal a convertir.
            respuesta_correcta = numero_binario  # Creamos variabe 'respuesta correcta' y le asignamos el valor binario correcto
            # (calculado previamente).
        else:  # Si la opción elegida fue '2' (convertir de Binario a Decimal).
            pregunta = f"Adivina el decimal de {numero_binario}: "  # Creamos otra cadena de pregunta
            # mostrando el número binario a convertir.
            respuesta_correcta = str(numero_decimal)  # Asignamos el valor decimal correcto (como string para comparar con input) a la variable 'respuesta_correcta'.

        while True:
            adivinanza = input(pregunta)  # Mostramos la pregunta al usuario y guardamos su respuesta en la variable 'adivinanza'.
            if adivinanza == respuesta_correcta:  # Comparamos la respuesta del usuario con la respuesta correcta.
                print(f"¡Correcto! es equivalente a {respuesta_correcta}.")  # Si la respuesta es correcta, mostramos un mensaje de felicitación.
                break # Salimos del bucle de adivinanzas si la respuesta es correcta
            else:  # Si la respuesta del usuario es incorrecta.
                print("¡Incorrecto! Intenta de nuevo o escribe 'rendirme' para ver la respuesta.")  # Mostramos un mensaje indicando que la respuesta es incorrecta.
                accion = input("¿Qué deseas hacer? (intentar de nuevo/rendirme): ").lower()
                if accion == 'rendirme':
                    print(f"La respuesta correcta era: {respuesta_correcta}.")  # Mostramos la respuesta correcta.
                    break # Salimos del bucle de adivinanzas si el usuario se rinde
                elif accion != 'intentar de nuevo':
                    print("Opción inválida. Intenta de nuevo.") # Si la entrada no es válida, se le pide intentar de nuevo
    else:  # Si la opción ingresada por el usuario no es '1', '2' o '3'.
        print("Entrada inválida!")  # Muestra un mensaje de error indicando que la entrada del usuario no es válida.
