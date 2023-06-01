import random
print('\033[7;31m \033[m'*44)
print('            GERADOR DE SENHAS')
print('\033[7;31m \033[m'*44)
car = int(input('\033[1;32mQuantos caracteres você quer nessa senha? \033[m'))
senha="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ012345678910@#+-[]*_;?"
print('\033[33mSua senha é:\033[m',end=' ')
for c in range(0,car):
	print(random.choice(senha),end='')
