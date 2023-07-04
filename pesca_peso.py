p = float(input("Escreva a quantidade em quilos da pesca de hoje: "))

if (p) > 50:
    e = p - 50
    m = e * 4
    print("A quantidade de quilos de peixe está fora do estabelecido!")
    print("O peso excedente é: \n Kg", e)
    print("A multa que terá que pagar pelo peso excedente é: \n R$ {:.2f}".format(m))
else:
    e = 0
    m = 0
    print("A quantidade de quilos de peixe está dentro do estabelecido!")
    print("O peso excedente é: \n Kg", e)
    print("A multa que terá que pagar pelo peso excedente é: \n R$ {:.2f}".format(m))