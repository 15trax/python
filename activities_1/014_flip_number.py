num = int(input("Ingrese un numero de dos cifras: "))

if 10 > num or num > 99 :
    print ("solo se permiten numeros de dos cifras")
elif num > 50 :
    primer_digito = int((num / 10) % 10)
    segundo_digito = num % 10
    print (f"{segundo_digito}{primer_digito}")
else :
    cifra_u = int(num % 10)
    print(cifra_u)
