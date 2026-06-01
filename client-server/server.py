import zmq

def server():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    # Vincula a todas as interfaces de rede da máquina na porta 12345
    socket.bind("tcp://0.0.0.0:12345")
    print("Servidor aguardando requisições na porta 12345...")

    while True:
        message = socket.recv()
        message_str = message.decode()
        print(f"Recebido: {message_str}")
        
        if "STOP" in message_str:
            print("Encerrando servidor...")
            break
            
        # Nova Funcionalidade: Retorna o texto em maiúsculas com o sufixo '*'
        reply = message_str.upper() + '*'
        socket.send(reply.encode())

if __name__ == "__main__":
    server()
