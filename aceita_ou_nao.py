nome = (input("Digite o seu nome: "))
sexo = (input("Informe o seu sexo, sendo ele M ou F: "))
idade = float(input("Informe a sua idade: "))

if (sexo == "F" or sexo == "f") and idade < 25:
    situacao = "ACEITA"

else:
    situacao = "NÂO ACEITA"

print(nome,situacao)