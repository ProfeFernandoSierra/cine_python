import os, time
os.system("cls")
DESCUENTO_NINO = 0.50      # menores de 12 años
DESCUENTO_ADULTO_MAYOR = 0.30  # 60 años o más
DESCUENTO_MARTES = 0.20
RECARGO_FIN_SEMANA = 0.15
IVA = 0.19
disponible_valores_numericos = False
disponible_dia = False
try:
    nombre = input("ingrese su nombre\n").upper()
    edad = int(input("ingrese su edad\n"))
    cantidad_entrada = int(input("ingrese cantidad de entradas\n"))
    precio_base = float(input("ingrese precio base\n"))
    dia_semana = input("ingrese dia de la semana\n").lower()
    
    if edad > 0 and cantidad_entrada > 0 and precio_base > 0:
        disponible_valores_numericos = True
    if dia_semana != "miercoles" or dia_semana != "jueves":
        disponible_dia = True

    if disponible_valores_numericos and disponible_dia:
        # Cálculos
        # 1.	Calcular subtotal: 
        subtotal = cantidad_entrada * precio_base 
        # 2.	Aplicar descuento según edad: 
        if edad < 12:
            descuento_edad = subtotal * DESCUENTO_NINO 
            tipo_cliente = "niño(a)"
        # o	< 12 años → 50% descuento
        elif edad >= 60:
            descuento_edad = subtotal * DESCUENTO_ADULTO_MAYOR 
            tipo_cliente = "adulto(a) mayor"
        else:
            descuento_edad = subtotal * 0
            tipo_cliente = "adulto(a)" 
        print("descuento por edad", descuento_edad)
        subtotal_con_descuento = subtotal - descuento_edad 
        if dia_semana == "martes":
            descuento_dia = DESCUENTO_MARTES * subtotal_con_descuento
            total_provisorio = subtotal_con_descuento - descuento_dia
        elif dia_semana == "sabado" or dia_semana == "domingo":
            descuento_dia = RECARGO_FIN_SEMANA * subtotal_con_descuento
            total_provisorio = subtotal_con_descuento + descuento_dia 
        else:
            descuento_dia = 0 * subtotal_con_descuento
            total_provisorio = subtotal_con_descuento + descuento_dia 
        recargo_iva = total_provisorio * IVA
        total_con_iva = total_provisorio + recargo_iva
        print("recargo iva", recargo_iva)
        print("total final", total_con_iva)
        time.sleep(60)
        total_final = round(total_con_iva, 2)
        if total_con_iva <= 10000:
            clasificacion = "Compra económica"
        elif total_con_iva > 10000 and total_con_iva < 30000:
            clasificacion = "Compra normal"
        else:
            clasificacion = "Compra alta"
        
        os.system("cls")
        print(f"Nombre del cliente: {nombre}") 
        print(f"Edad: {edad}") 
        print(f"Tipo de cliente: {tipo_cliente}") 
        print(f"Total a pagar: ${total_final} ") 
        print(f"Clasificación de la compra: {clasificacion}")    
    else:
        os.system("cls")
        print("uno de tus datos viene incorrecto")
    
except:
    print("el valor debe ser numerico")
