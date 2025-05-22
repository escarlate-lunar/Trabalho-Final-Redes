import socket

# Configurações do servidor
IP = '0.0.0.0'  # Escuta todas as interfaces
PORTA = 8080    # Porta padrão pra testes
BUFFER = 4096   # Tamanho do buffer pra receber dados

# Cria o socket TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
    servidor.bind((IP, PORTA))
    servidor.listen(1)
    print(f"[*] Servidor aguardando conexões em {IP}:{PORTA}...")

    # Aceita conexão com cliente
    cliente, endereco = servidor.accept() # Novo socket secundário pra comunicação com cliente
    print(f"[+] Conexão estabelecida com {endereco}")   

    # Recebe nome do arquivo
    nome_arquivo = cliente.recv(BUFFER).decode()
    print(f"[*] Recebendo arquivo: {nome_arquivo}")

    # Recebe dados do arquivo
    with open(nome_arquivo, 'wb') as arquivo:
        while True: # Permanece em loop até que todo o arquivo tenha sido reescrito
            dados = cliente.recv(BUFFER)
            if not dados:
                break
            arquivo.write(dados)

    print(f"[+] Arquivo '{nome_arquivo}' recebido com sucesso!")