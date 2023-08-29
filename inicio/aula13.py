# Aula 12


nome = 'Jessica Cristina'
altura = 1.60
peso = 50


imc = peso / (altura ** 2)


# f'  -> formatacao de string
# .2f  -> 2 casas decimais apos a virgula

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} Kg e seu IMC é:'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

