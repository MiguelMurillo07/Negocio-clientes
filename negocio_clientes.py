# Caso No. 9: Ingresar el monto de la compra para obtener ya sea el monto de descuento o de recargo y el total a pagar en el negocio.


print("--------------------------")
print("----Negocio de Compras----")
print("--------------------------")

# input

k = input("Ingrese el tipo de cliente que es: G para General y A para Afiliado: ")
print(" ")
m = input("Ingrese el medio de pago que desea hacer: C para pago de Contado y P para pago a Plazos: ")
print(" ")
z = (float(input("Digite el valor de la compra en total: ")))
print(" ")

#processing and output
if k == 'G'and m == 'C':
    t=z-(z*0.15)
    print("Cliente General, con metodo de pago de contado, descuento de 15%. Valor total a pagar: $ " + str(t))
    print(" ")
else:
    if k == 'G' and m == 'P':
        t=z+(z*0.10)
        print("Cliente General, metodo de pago a plazos, recargo de 10% parcial. Valor total a pagar: $ " + str(t))
        print(" ")
    else:
        if k == 'A' and m == 'C':
            t=z-(z*0.2)
            print("Cliente Afiliado, metodo de pago de contado, descuento de 20%. Valor total a pagar: $ " + str(t))
            print(" ")
        else:
            if k == 'A' and m == 'P':
                t=z+(z*0.05)
                print("Cliente Afiliado, metodo de pago a plazos, recargo de 5% parcial. Valor total a pagar: $ " + str(t))
                print(" ")
            else: 
                print("Las opciones registradas son incorrectas. Por favor verifique de nuevo e intente otra vez. ")