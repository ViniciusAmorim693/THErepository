name = input ('Qual o seu nome, ser misterioso? ')
caum= ''

print (f'Então você é o {name}. É um prazer recebê-lo em nosso parque ')

start = input ('Você já foi na nossa montanha russa do infinito? ')

if start == 'sim':
    print('Certo. Vamos pular para o polvo maluco então. ')
    caum = input ('Você quer continuar seguindo o guia ou abandonar o parque ? ')
else:
    print('Tudo bem, vamos conhecer a montanha russa do infinito então ')

if caum == 'abandonar':
    print ('Você está prestes a sair do parque sorrateiramente, quando um segurança o vê ')
else:
    quit()

desf1 = input ('Você corre do segurança ou bate nele? ')

if desf1 == 'corro':
    print ('Você foi rápido o suficiente para despistar o segurança e escapar do parque ')
else:
    print ('Você bateu no segurança e acabou sendo preso. Aproveite o tempo na cadeia. ')


print ('Você está na cadeia, cheio de homens musculosos e sarados ao seu redor, loucos para encontrarem um lugar para depositar dinheiro e não tem nenhum segurança por perto. Um homem tatuado e careca se aproxima')
cov = input ('Você espera o homem se aproximar ou lhe dá um soco de direita antes que ele consiga chegar perto de você?')
if cov == 'espero':
    print ("O homem chega, se aproxima, e pergunta se tem algum bebedouro por perto")
else:
    print ("O homem se enfurece ao levar o soco e tenta te atacar, mas por sorte um segurança chega bem na hora e separa vocês")


















