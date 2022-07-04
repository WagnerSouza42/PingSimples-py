## Importar o módulo ou biblioteca OS (integra os programas e
#recursos do S.O
import os

##Imprime "#" 60 vezes
print("#" *60)

## Criei uma variavel que vai receber do usuario um IP
ip_ou_host = input("Digite o ip host a ser verificado: ")
print("-" * 60)##Imprime "-" 60 vezes

##Chamando System da biblioteca OS - comando ping
# -n -num de pacotes que serão 6 {}
os.system('ping -n 6 {}'.format(ip_ou_host))
print("-" * 60)##Imprime "-" 60 vezes
