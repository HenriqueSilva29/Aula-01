# como mostrar algo na tela para o usuário
print("hello")
print('hello')

# declaração de variáveis em python
nome = "eiaa"
numeroInteiro = 2
numeroDecimal = 2.45678645
palavraCaracteresSimples = 'henrique'
palavraCaractereDupla = "henrique" 
verdadeiroFalso = True
#mostrando na tela o tipo de dado que a variável armazena
print (numeroInteiro)
print(numeroDecimal)
print(palavraCaracteresSimples)
print(palavraCaractereDupla)
print(verdadeiroFalso)
#mostrando na tela o tipo de dado que a variável armazena
print(type(numeroInteiro))
print(type(numeroDecimal))
print(type(palavraCaracteresSimples))
print(type(palavraCaractereDupla))
print(type(verdadeiroFalso))

#Recursos para usar com dados do tipo String
#Funçãp len = contar a quantidade de caractere de uma variável do tipo String
print(len(palavraCaractereDupla))
#Repetir valor da variável, usar * e colocar a quantidade de vezes que gostaria de repetir
print((numeroInteiro,)*3)
#Concatenando strings
print((nome + " ", verdadeiroFalso))

#Recursos para usar com dados do tipo float
print(numeroDecimal)

# A funçãp round serve para arredondar  e defibir a quantidade de casas depois da vírgula
print(round(numeroDecimal))
#Outra forma de arredondar e definir a quantidade de casas decimais.
print('%.4f' % (numeroDecimal))

#trucar
print("{:.3f}".format(numeroDecimal))

