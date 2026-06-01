import zmq
import sys

def client(server_ip):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)

    # Conecta ao IP da máquina onde o servidor está rodando
    print(f"Conectando ao servidor em {server_ip}:12345...")
    socket.connect(f"tcp://{server_ip}:12345")

    # Envia uma mensagem de teste
    texto = "ola mundo"
    print(f"Enviando: {texto}")
    socket.send(texto.encode())
    
    message = socket.recv()
    print(f"Resposta recebida: {message.decode()}")
    
    # Envia comando de parada
    print("Enviando comando STOP...")
    socket.send(b"STOP")

if __name__ == "__main__":
    # Permite passar o IP do servidor via linha de comando
    ip = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    client(ip)
