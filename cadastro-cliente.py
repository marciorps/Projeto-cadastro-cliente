
from datetime import datetime
import random


print('-----------Bem vindo a nossa empresa-----------')
nome = input('Digite seu nome:')
idade = input('Digite seu idade:')
data_de_registro = datetime.now().date()
data_nascimento = input('digite nascimento:')

data_aniversario_formatado = datetime.strptime(data_nascimento, '%d/%m/%Y')

cartoes = ['R$50,00', 'R$250,00', 'R$120,00']


print(f'''Olá {nome}, seu registro foi concluído com sucesso no dia {data_de_registro.strftime('%d/%m/%Y')}.
Parabéns, houve um sorteio e você ganhou cartão de compras no valor de {random.choice(cartoes)}''')