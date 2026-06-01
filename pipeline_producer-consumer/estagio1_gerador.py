import zmq
import time
import random
import pickle
from const_pipeline import PORT_1

def gerador():
    context = zmq.Context()
    socket = context.socket(zmq.PUSH)
    # Vincula o socket para que o estágio intermediário possa se conectar
    socket.bind(f"tcp://0.0.0.0:{PORT_1}")
    print(f"Estágio 1 (Gerador) pronto na porta {PORT_1}...")

    while True:
        time.sleep(1)
        # Gera uma carga de trabalho (ex: tamanho de um processamento)
        workload = random.randint(1, 10)
        print(f"[Gerador] Criando item com valor: {workload}")
        socket.send(pickle.dumps(workload))

if __name__ == "__main__":
    gerador()
