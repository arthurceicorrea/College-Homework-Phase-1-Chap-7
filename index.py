# Minha equipe é composta somente por mim.
# Nome: Arthur Cei Corrêa
#RM: 97781

# Saving relevant information.
anos = float(input("Tempo como fumante (em anos).....: ")) * 360

# Pedindo o valor do maço que o sujeito compra.
valorMaco = int(input("Valor do maço.....: "))

# Armazenando a quantidade de maços fumados por dia.
qntMacoDia = float(input("Quantidade de maços por dia......: "))

# Calculando o total gasto em anos e armazenando a informação.
total = float((valorMaco * qntMacoDia) * anos)

# Encaixando o resultado de acordo com as informações armazenadas, através de condicionais.
if total < 20000:
    print(f"Com o valor R${float(total):.2f}, você poderia ter dado entrada em um carro.")
elif total > 20000 and total < 50000:
    print(f"Com o valor R${float(total):.2f}, você poderia ter comprado um carro popular usado.")
else:
    print(f"Com o valor R${float(total):.2f}, você poderia ter comprado um carro zero.")