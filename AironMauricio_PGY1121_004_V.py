from itertools import cycle

info_persona = []


def menu():
  print("\nBienvenidos al auto servicio de atencion rapida RENAPER.\n¿Como podemos ayudarle?:\n")
  print("-----Menu-----")
  print("1. Registrar usuario ")
  print("2. buscar usuario ")
  print("3. imprimir documentos ")
  print("4. eliminar usuario ")
  print("5. salir ")

def validar_digito_verificador(DNI_sin_vr):
    reversed_digits = map(int, reversed(str(DNI_sin_vr)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    if (-s) % 11 == 10:
        return "K"
    return (-s) % 11


def DNI_validado(DNI):
    DNI_sin_vr = str(DNI)
    digito_ingresado = DNI_sin_vr[-1]  # digito final
    calculado = str(validar_digito_verificador(DNI_sin_vr[:-1]))  # toma todo el DNI sin el numero final para validarlo
    DNI_completo = DNI_sin_vr[:-1] + "-" + calculado  # DNI completo con dígito verificador calculado

    if digito_ingresado == calculado:
        return DNI_completo
    else:
        return None




while True:

  menu()
  opcion=int(input("escoja la opcion que desee: "))

  match opcion:
    case 1:
            DNI = input("ingrese su DNI sin punto ni guion: ")

            validacion_DNI_final = DNI_validado(DNI)

            if validacion_DNI_final is None:
                print("el DNI que ingreso es invalido. el programa finalizara ")
                break

            nombre = input("ingrese su nombre (su nombre debe contar con almenos 8 caracteres): ").upper()
            if len(nombre) < 8:
              print("el nombre debe tener almenos 8 caracteres ")
              continue

            edad = int(input("ingrese su edad: "))
            if edad <= 0 :
              print("tu edad no puede ser 0")
              continue
            pais_nacimiento = input("ingrese su pais de nacimiento: ").upper()
            ciudad_nacimiento = input("ingrese su ciudad de nacimiento: ").upper()
            
            estado_civ=int(input("seleccione su estado civil actual: \n1.Soltero\n2.Casado \n: " ))
            if estado_civ == 1:
              estado_civil= "SOLTERO"
            elif estado_civ == 2:
              estado_civil = "CASADO"
            else:
              print("dato incorrecto")
              continue

            DNI = validacion_DNI_final
            info_persona.extend([DNI, nombre, edad, pais_nacimiento, ciudad_nacimiento,estado_civil])
            print(f"Sus datos han sido registrados con éxito.\nBienvenido: {info_persona}\n")



      #para agregar varios elementos utilizar el metodo "extend()."


    case 2:
      consulta=input("ingrese el DNI del usuario que desea buscar con guion en su digito verificador: ")
      if consulta in info_persona:
        print(f"\nEl DNI {DNI} esta asociado al nombre de {nombre} con {edad} años de edad\nnacido en {pais_nacimiento} en la ciudad de {ciudad_nacimiento} y su estado civil es {estado_civil}.")
        if pais_nacimiento == "ARGENTINA":
          print(f"\n{nombre} pertenece al pais de ARGENTINA\n")
        else:
            print("este usuario no pertenece al pais de ARGENTINA\n")




    case 3:
      consulta=input("ingrese el DNI del usuario que desea buscar con guion en su digito verificador: ")
      if consulta in info_persona:
          consulta_cont=int(input(f"\n ¿Usted desea imprimir el documento de {nombre}?:\n1. si \n2. no \n"))
          if consulta_cont == 1:
              print("----------------- DOCUMENTO ----------------- ")
              print(f"nombre : {nombre}                            ")
              print(f"su DNI es: {DNI}                             ")
              print(f"estado civil: {estado_civil}                 ")
              print(f"pais de nacimiento: {pais_nacimiento}        ")
              print(f"ciudad de nacimiento: {ciudad_nacimiento}    ")
              print( "\nSISTEMA DE ATENCION RAPIDA RENAPER           ")
              print( "---------------------------------------------")
          else:
              print("dato incorrecto")
              continue  


    case 4:
      consulta=input("ingrese el DNI del usuario que desea buscar con guion en su digito verificador: ")
      if consulta in info_persona:
        info_persona= []
        print("se borro el registro con exito ")


    case 5:
      print("muchas gracias por preferirnos\n\n\nAiron Saez vers. 1.0")
      break
