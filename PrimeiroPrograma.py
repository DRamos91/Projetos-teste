# -*- coding: utf-8 -*-

qtde_pepsi = 130
qtde_coca = 150
preco_coca = 1.50
preco_pepsi = 1.50
custo_loja = 2500

print(qtde_coca)
print(qtde_pepsi)
print(preco_coca)
print(preco_pepsi)
print(custo_loja)

"""1. Qual foi o faturamento de Pepsi da Loja?"""
fat_pepsi = qtde_pepsi * preco_pepsi
print(fat_pepsi)

"""2. Qual foi o faturamento de Coca da Loja?"""
fat_coca = qtde_coca * preco_coca
print(fat_coca)

"""3. Qual foi o Lucro da loja?"""
lucro = (custo_loja - (fat_coca + fat_pepsi))
print(lucro)

"""4. Qual foi a Margem da Loja? (Lembre-se, margem = Lucro / Faturamento). Não precisa formatar em percentual"""
fat_total = fat_coca + fat_pepsi
margem = (lucro / fat_total)
print(margem)

"""### Parte 2 - Inputs e Strings

Crie um programa de consulta de bebida que, dado um código qualquer, identifique se a bebida é alcóolica. O programa deve responder True para bebidas alcóolicas e False para bebidas não alcóolicas. Para inserir um código, use um input.

Dica: Lembre-se do comando in para strings e sempre insira os códigos com letra maiúscula para facilitar.
"""
'''Coca -> Código: BEB1300543<br>
Pepsi -> Código: BEB1300545<br>
Vinho Primitivo Lucarelli -> Código: BAC1546001<br>
Vodka Smirnoff -> Código: BAC17675002<br>
'''
confere = input('Digite um produto: ')
print('BEB' in confere)