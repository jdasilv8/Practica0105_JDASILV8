dinerocuenta = float(input("Dinero introducido en la cuenta: "))
año1 = dinerocuenta * 1.04
año2 = año1 * 1.04
año3 = año2 * 1.04

año1 = round(año1,2)
año2 = round(año2,2)
año3 = round(año3,2)

print ("Tras el primer año tendrías en tu cuenta unos ahorros de:",año1)
print ("Tras el segundo año tendrías en tu cuenta unos ahorros de:",año2)   
print ("Tras el tercer año tendrías en tu cuenta unos ahorros de:" ,año3)   