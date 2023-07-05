dias = float(input("Digite a quantidade de dias que o funcionário quer tirar de férias: "))

if dias > 4 and dias in [5,10,15,20,30]:
    print("O funcionário tirará:", dias, " dias!")
else:
    print("Quantidade inválida de dias!")