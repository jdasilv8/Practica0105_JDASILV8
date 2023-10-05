Kg = float(input("Cuánto pesas?(KG): "))
Est = float(input("Cuánto mides)(m): "))

IMC = (Kg/(Est**2))
IMC = round(IMC,2)

print ("Tu índice de masa corporal es de",IMC)