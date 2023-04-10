# Conversão de dados
prova1 = input('Informe o valor da primeira nota: ')
prova2 = input('Informe o valor da segunda nota: ')

try:
    prova1 = int(prova1)
    prova2 = int(prova2)
except:
    print('Error: Invalid')
    
media = (prova1 + prova2) / 2

if media >=6: 
    print(f'Parabéns! Você foi aprovado.\nMedia {media} ')
elif media >=4:
    print(f'Você está de recuperação.\nMedia {media} ')
else:
    print(f'Você foi reprovado.\nMedia {media} ')
    


# For -> Quando se sabe a quantidade de repetição
numero = int(input('Informe um número:')) 
for i in range(0,11):
    print(f'{numero} x {i} = {numero * i}')


# While -> Não sabe a quantidade de repetição
flag = ''
while flag != 'sim':
    flag = input('Deseja sair? ').lower()