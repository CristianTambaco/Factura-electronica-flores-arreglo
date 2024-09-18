



#solicitar datos
nombre=input("Ingresa tu nombre: ")
correo=input("Ingresa tu correo: ")
cedula=input("Ingresa tu cedula: ")

print("Ingresa el número de flores para el arreglo")
floresRojas=int(input("Rojas: "))
girasoles=int(input("Girasoles: "))
claveles=int(input("Claveles: "))
dalias=int(input("Dalias: "))


#Realizar el proceso
cantidadRojas=floresRojas*0.75
cantidadGirasoles=girasoles*0.5
cantidadClaveles=claveles*1.25
cantidadDalias=dalias*0.95

total=cantidadRojas+cantidadGirasoles+cantidadClaveles+cantidadDalias

pagoConIVA=total*(1.15)

#Imprimir resultados
print("------------Factura Electronica------------")
print(f"USUARIO {nombre}")
print(f"El subtotal es de {round(total,2)}")
print(f"El total es de {round(pagoConIVA, 2)}")
print(f"La factura se enviará a su correo electronico: {correo}")
print(f"----------Muchas gracias-----------")




