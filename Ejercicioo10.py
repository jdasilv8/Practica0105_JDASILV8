p1payaso = 112
p1muneca = 75

munecas = int(input("Introduzca el nº de muñecas de este pedido: "))
payasos = int(input("Introduzca el nº de payasos de este pedido: "))

ppayasos = p1payaso * payasos
pmunecas = p1muneca * munecas
ptotal = ppayasos + pmunecas

print ("El peso de este paquete será de:",ptotal,"g")