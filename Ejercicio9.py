inv = float(input("Cuánto desea invertir?: "))
interes = float(input("Indique el interés anual en porcentaje (%): "))
interes = interes/100

años = int(input("Durante cuántos años?: "))

capital = (inv*((interes+1)**años))
obtenido = capital - inv

print ("El total de ganancias en la inversión sería de:",obtenido)