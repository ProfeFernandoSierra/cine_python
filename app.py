import os
os.system("cls")

DESCUENTO_NINO = 0.50      # menores de 12 años
DESCUENTO_ADULTO_MAYOR = 0.30  # 60 años o más
DESCUENTO_MARTES = 0.20
RECARGO_FIN_SEMANA = 0.15
IVA = 0.19

bandera_acceso_numericos = False
bandera_acceso_dia = False

try:
    nombre = input("ingrese su nombre\n").title()
    edad = int(input("ingrese su edad\n"))
    cantidad_entrada = int(input("ingrese cantidad de entradas\n"))
    precio_base = float(input("ingrese precio\n"))
    dia = input("ingrese dia de asistencia\n").lower()
    
    if edad > 0 and cantidad_entrada > 0 and precio_base > 0:
        bandera_acceso_numericos = True
    if dia != "miercoles" and dia != "jueves":
        bandera_acceso_dia = True
    
    
    if bandera_acceso_numericos and bandera_acceso_dia :
        subtotal = cantidad_entrada * precio_base
        if edad < 12 :
            valor_descuento_edad = subtotal * DESCUENTO_NINO
            tipo_cliente = "niño(a)"
        elif edad >= 60:
            valor_descuento_edad = subtotal * DESCUENTO_ADULTO_MAYOR
            tipo_cliente = "adulto(a) mayor"
        else:
            valor_descuento_edad = 0
            tipo_cliente = "adulto(a)"
        valor_provisorio = subtotal - valor_descuento_edad
        if dia == "martes":
            valor_descuento_dia = valor_provisorio * DESCUENTO_MARTES
            valor_provisorio2 = valor_provisorio - valor_descuento_dia
             
        elif dia == "sabado" or dia == "domingo":
            valor_recargo = valor_provisorio * RECARGO_FIN_SEMANA
            valor_provisorio2 = valor_provisorio + valor_recargo
        else:
            valor_provisorio2 = valor_provisorio    
        
        valor_iva = valor_provisorio2 * IVA
        valor_final = valor_provisorio2 + valor_iva
        valor_final_redondeado = round(valor_final, 2)
        
        if valor_final_redondeado <= 10000:
            clasificacion = "Compra economica"
        elif valor_final_redondeado > 10000 and valor_final_redondeado <= 30000:
            clasificacion = "Compra normal"
        else:
            clasificacion = "Compra alta"
        
        os.system("cls")
        print(f"Nombre: {nombre}")
        print(f"Edad: {edad} años")
        print(f"Tipo Cliente: {tipo_cliente}")
        print(f"Total a pagar: ${valor_final_redondeado}")
        print(f"Clasificacion: {clasificacion}")
        
    else:
        os.system("cls")
        print("uno de tus datos es incorrecto")
    
except:
    os.system("cls")
    print("el valor debe ser numerico")