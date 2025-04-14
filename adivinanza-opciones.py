import random  # Importamos la librería 'random' para generar números aleatorios.

print("¡Adivina el Número en Binario o Decimal según corresponda!")  # Mostramos un mensaje de bienvenida al usuario.

while True: # De esta manera iniciamos un bucle infinito, hasta que el usuario decida salir seleccionando la opcion correspondiente.
    opcion = input("'1' De decimal a binario\n'2' De binario a decimal\n'3' para salir: ")  # Pedimos al usuario que ingrese una opción 
    
    if opcion == '3':  # Si elije la opción 3.
        print("\nNos vemos!")  # Muestra un mensaje de despedida.
        break  # De esta manera se  sale del bucle, terminando la ejecución del programa.
    
    elif opcion in ('1', '2'):   # Si la opción ingresada es '1' o '2'.
        numero_decimal = random.randint(1, 500)  # Número aleatorio entre 1 y 500.
        numero_binario = bin(numero_decimal)[2:]  # Usamos la función 'bin' para convertir el 'numero_decimal' a su representación
         #binaria y utilizamos el slicing [2:] para eliminar el prefijo "0b" que la función 'bin()' añade.

        if opcion == '1':   # Si la opción elegida fue '1' (convertir de Decimal a Binario).
            pregunta = f"\nAdivina el binario de {numero_decimal}:\n" # Creamos una cadena de pregunta con 'f-string', mostrando el número decimal a convertir.
            respuesta_correcta = numero_binario # Creamos variabe 'respuesta correcta' y le asignamos el valor binario correcto 
            #(calculado previamente).
            opciones = [ # Creamos una lista con tres opciones para que el usuario elija.
                f"a) {respuesta_correcta}",  # Opción correcta: el binario correspondiente.
                f"b) {bin(random.randint(1, 500))[2:]}",  # Incorrecta 1.
                f"c) {bin(random.randint(1, 500))[2:]}"   # Incorrecta 2.
            ]
        else:  # Si la opción elegida fue '2' (convertir de Binario a Decimal).
            pregunta = f"\nAdivina el decimal de {numero_binario}:\n" # Creamos otra cadena de pregunta mostrando el número binario a convertir.
            respuesta_correcta = str(numero_decimal) # Asignamos el valor decimal correcto a la variable 'respuesta_correcta' (como string para comparar).
            opciones = [ # Creamos una lista con tres opciones para que el usuario elija.
                f"a) {respuesta_correcta}",  # Correcta.
                f"b) {random.randint(1, 500)}",  # Incorrecta 1.
                f"c) {random.randint(1, 500)}"   # Incorrecta 2.
            ]

        # Mostramos pregunta y opciones.
        print(f"\n{pregunta}")
        for opcion_texto in opciones:
            print(opcion_texto)

        # Pedimos al usuario que elija una letra.
        seleccion = input("\nElige la letra de tu respuesta (a, b, c): ").lower()

        # Validamos y comprobamos la respuesta.
        if seleccion in ('a', 'b', 'c'):
            if seleccion == 'a':  # Comparamos si la letra elegida corresponde a la opción correcta (fija en 'a').
                # Si la respuesta es correcta, mostramos un mensaje de felicitación. 
                print(f"\n¡Correcto! Es equivalente a {respuesta_correcta}.\n")
            else:
                # Si la letra elegida no es 'a'.
                print(f"\n¡Incorrecto! Es equivalente a {respuesta_correcta}.\n") 
        else:
            # Si la entrada no es 'a', 'b' o 'c'.
            print("\n¡Entrada inválida! Elige a, b o c.")
    else:  # Si la opción no es '1', '2' o '3'.
        print("\nEntrada inválida!\n")  # Muestra un mensaje de error indicando que la entrada del usuario no es válida.