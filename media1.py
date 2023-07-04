nota1 = float(input("Informe a 1° nota: "))
nota2 = float(input("Informe a 2° nota: "))

media = (nota1 + nota2) / 2

situacao = media

print("A media do aluno foi: \n", situacao)

if (situacao) >=7:
    print("Parabéns, você passou")
    
else:
    print("Você foi reprovado!")
