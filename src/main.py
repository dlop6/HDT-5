from analisis import Analisis

analisis = Analisis()


while True:

    print("\nEscoja las estadísticas que quiere observar: \n1. Tiempo con distintos intervalos de instrucciones\n2. Tiempo de procesos con 200 de RAM\n3. Tiempo con doble CPU\n4. Salir.")
    opcion = input("Opción: ")
    if opcion == "1":
        analisis.stats_intervalos()
    elif opcion == "2":
        analisis.stats_RAM200()
    elif opcion == "3":
        analisis.stats_dobleCPU()
    else:
        print("Adiós")
        break

