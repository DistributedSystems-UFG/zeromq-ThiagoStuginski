import zmq
import time
import random

def publisher():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://0.0.0.0:12345")
    print("Publicador iniciado na porta 12345...")

    # Nova Funcionalidade: Publica múltiplos tópicos (TIME e TELEMETRY)
    while True:
        time.sleep(2)
        
        # Tópico TIME
        t_msg = f"TIME {time.asctime()}"
        socket.send(t_msg.encode())
        
        # Tópico TELEMETRY (Nova funcionalidade simulada)
        temp = random.randint(20, 35)
        m_msg = f"TELEMETRY Temperatura atual: {temp}°C"
        socket.send(m_msg.encode())
        
        print(f"Publicado: {t_msg} | {m_msg}")

if __name__ == "__main__":
    publisher()
