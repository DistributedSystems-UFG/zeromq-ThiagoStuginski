import zmq
import sys

def subscriber(server_ip):
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect(f"tcp://{server_ip}:12345")
    
    # Nova Funcionalidade: Escolher via argumento qual tópico assinar
    topico = sys.argv[2] if len(sys.argv) > 2 else "TIME"
    socket.setsockopt(zmq.SUBSCRIBE, topico.encode())
    print(f"Inscrito no tópico: [{topico}] escutando de {server_ip}...")

    # Escuta 5 atualizações do tópico escolhido
    for _ in range(5):
        msg = socket.recv()
        print(f"Recebido: {msg.decode()}")

if __name__ == "__main__":
    ip = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    subscriber(ip)
