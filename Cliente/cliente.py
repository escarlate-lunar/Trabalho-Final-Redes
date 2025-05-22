import socket
import sys

# Configurações do cliente
IP = sys.argv[1]            # IP do cliente (localhost)
PORTA = 8080                # Porta padrão pra testes
BUFFER = 4096               # Tamanho do buffer pra enviar os dados
NOME_ARQUIVO = sys.argv[2]  # Nome do arquivo (fornecido em args)

# Cria o socket TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.connect((IP, PORTA))
    print(f"[*] Conectado ao servidor {IP}:{PORTA}")

    # Envia o nome do arquivo primeiro
    cliente.send(NOME_ARQUIVO.encode())

    # Abre o arquivo e envia seu conteúdo
    with open(NOME_ARQUIVO, 'rb') as arquivo:
        while True: # Permanece em loop até fornecer cada pedaço do arquivo
            dados = arquivo.read(BUFFER)
            if not dados:
                break
            cliente.send(dados)

    print(f"[+] Arquivo '{NOME_ARQUIVO}' enviado com sucesso!")