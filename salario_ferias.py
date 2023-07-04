salario = float(input("Informe o salario que o funcionário recebe: "))
meses = float(input("Informe quantos meses o funcionário trabalhou: "))

if (meses) >= 12:
    salario = (salario * meses) / 12
    salarioFerias = (salario / 3) + salario
    print("O funcionário receberá: R$ {:.2f}".format(salarioFerias), "pelas férias")

else:
    print("O funcionário não terá direito à férias porque não trabalhou os 12 meses mínimos")