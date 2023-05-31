nino = 5500
joven = 7000
adulto = 9000

while True:
    bt1=True
    bt2=True
    try:
        print("==========")
        print("Bienvenido al Cine Moro.")
        print("==========")
        bt1=False

        vedad = int(input("Ingresa tu edad: "))
        while bt2==True:
            
            try:
                if vedad >= 0 and vedad <= 13:
                    cantnino = int(input("Ingresa la cantidad de entrdas deseada: "))
                    bt2=False
            except:
                print("Dato erróneo.")
                bt2=True
            if cantnino > 0:
                totalnino = cantnino*nino
                entradasnino =+ cantnino
                print("Categoria niño.")
                print("====================")
                print(f"Cantidad de entradas: {cantnino}")
                print(f"Total a pagar: {totalnino}")
        elif vedad > 13 and vedad <= 21:
            cantjoven = int(input("Ingresa la cantidad de entradas deseada: "))
        if cantjoven > 0:
            totaljoven = cantjoven * joven
            entradasjoven =+ cantjoven
            print("Categoria joven.")
            print("=====================")
            print(f"Cantidad de entradas: {cantjoven}")
            print(f"Total a pagar: {totaljoven}")
        elif vedad > 22:
            cantadulto = int(input("Ingresa la cantidad de entradas deseada: "))
            if cantadulto > 0:
                totaladulto = cantadulto * adulto
                entradasadulto =+ cantadulto
                print("Categoria adulto.")
                print("=============================")
                print(f"Cantidad de entradas: {cantadulto}")
                print(f"Total a pagar: {totaladulto}")
        else:
            print("Debes ingresar un numero entero. ")
            continue
    except:
        print("intentalo de nuevo")
        bt1=True