#########################################################
# Alessandro Miranda Gonçalves                          #
# Linkedin: www.linkedin.com/alessandromirandagoncalves #
# Março/2022                                            #
#########################################################
# Estabelece conexão com host/ip informado pelo usuário
# na porta especificada

import socket
import sys
import re       #Biblioteca que checa strings com expressões regulares

def main():
    host = ' '
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
    except socket.error as e:
        print('Erro de conexão: {}\n'.format(e))
        sys.exit()
    print ("socket iniciado")

    # aguarda_host_porta()
    while ip_host_valido(host) == False and host != '':
        host = input('Digite o host/ip a ser conectado ou vazio para sair: \n')
        if ip_host_valido(host) == False:
            print('Host/IP inválido\n')
    # Se informou host vazio, para a execução
    if host == '':
        sys.exit()
    porta = int(input('Digite a porta a ser conectada:\n'))

    try:
        print('Status: conectando...\n')
        s.connect((host,int(porta)))
        print('Cliente TCP conectado no host/ip ' + host + '\n')
        s.shutdown(2)
    except socket.error as e:
        print('A conexão falhou\n')
        print('Erro: {}'.format(e))
        sys.exit()


#Verifica se o IP ou Host é válido através de expressões regulares
def ip_host_valido(host):
    # Verifica formato IP válido. Ex: 192.0.0.1
    sintaxe_ip = re.search(
        '^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})$', host)
    ##Verifica formato HOST válido. Ex: www.seati.ma.gov.br
    sintaxe_host = re.search(
        '^(http[s]?://|ftp://)?(www\.)?[a-zA-Z0-9-\.]+\.(com|org|net|mil|edu|ca|co.uk|com.au|gov|br)$', host)
    if sintaxe_ip == None and sintaxe_host == None:
        return False
    else:
        return True

if __name__ == "__main__":
    main()