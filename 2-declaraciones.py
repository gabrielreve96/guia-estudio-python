import typing

email = input("Ingresa tu email: ")
dni = input("Ingresa tu DNI: ")

base_de_datos: typing.List[typing.Dict[str, str]] = [
    {"nombre": "gabriel", "dni": "y9938839r", "email": "gabriel@example.com"},
    {"nombre": "gonzalo", "dni": "3y9938839j", "email": "gonzalo@example.com"}
]

def bucles_validador(email, dni):
    if len(email) >= 8 and validar_dni(dni) == "pass":
        for objeto_nombre in base_de_datos:
            if objeto_nombre["email"].lower() == email and objeto_nombre["dni"].lower() == dni:
                return "Acceso concedido. Email: {}, DNI: {}".format(objeto_nombre["email"], objeto_nombre["dni"])
        return "Acceso denegado. Datos invalidos."
    return "Ingresa valores correctos."

def validar_dni(dni_dato):
    if dni_dato[-1].isdigit():
        return "pass"
    return "denegado"

resultado = bucles_validador(email, dni)
print(resultado)





ingresa_numero1=int(input("Numero1"))
ingresa_numero2=int(input("Numero2"))

def sumaDeNumeros(num1,num2):
  resultado_suma=num1+num2
  producto=num1*num2
  print(f"la suma de ambos numero es de {resultado_suma}")
  print(f"el producto de ambos numeros es de  {producto}")


sumaDeNumeros(ingresa_numero1,ingresa_numero2)




def numeroPirmos(num):
  if num / 2 == 0:
    print("es primo")
  else:
    print("no es primo")

numeroPirmos(22)
