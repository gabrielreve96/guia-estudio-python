import typing

mi_nombre:str = "gabriel dominguez"
mi_edad:int =  27
mi_peso:float = 69.34

list_favorite_game:typing.List[str]=["Warzone", "FiFA" , "AGE OF "]

def game_date():
  for i in list_favorite_game:
   print(f"hola me llamo {mi_nombre}  y tnego  {mi_edad}  y peso unos {mi_peso}  mis juegos favoritos son {i} ")


game_date()

password_card_cvc:typing.Tuple[int ,int ,int]=(12,11,24)
practices_sport=typing.Dict=[str,str]={"futbool":"succes" , "basketbol":"succes"}
set_of_numbers: typing.Set[int] = {1, 2, 3}
print(type(password_card_cvc))
print(password_card_cvc)
print(practices_sport)
print(set_of_numbers)




import typing

mi_nombre:str = "gabriel dominguez"
mi_edad:int =  27
mi_peso:float = 69.34

list_favorite_game:typing.List[str]=["Warzone", "FiFA" , "AGE OF EMPARIES"]

def game_date():
  for i in list_favorite_game:
   print(f"hola me llamo {mi_nombre}  y tnego  {mi_edad}  y peso unos {mi_peso}  mis juegos favoritos son {i} ")


game_date()

password_card_cvc:typing.Tuple[int ,int ,int]=(12,11,24)
practices_sport=typing.Dict=[str,str]={"futbool":"succes" , "basketbol":"succes"}
set_of_numbers: typing.Set[int] = {1, 2, 3}
print(type(password_card_cvc))
print(password_card_cvc)
print(practices_sport)
print(set_of_numbers)



import typing
def entradas(edad):
  if edad <=18:
    return "No es mayor de edad , entrada denegada"
  return "Entrada valida"

entradas(17)




# Pensión según la edad
def pensiones_abuelos(edad):
    rango_edad_pension: typing.Dict[int, float] = {67: 1234.67, 70: 2300.67}
    if (edad in rango_edad_pension)  and   (edad < 69):
        print("Su sueldo, según la edad, es de ", rango_edad_pension[67])
    elif edad >= max(rango_edad_pension.keys()):
        print("Su sueldo, según la edad, es de ", rango_edad_pension[max(rango_edad_pension.keys())])
    else:
        print("Aun no le toca la pensión")

pensiones_abuelos(122)