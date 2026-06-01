import zmq
import pickle
import time
from const_pipeline import IP_ESTAGIO_2, PORT_2

def consumidor():
    context = zmq.Context()
    socket = context.socket(zmq.PULL)
    
    # Conecta no intermediário (Estágio 2)
    socket.connect(f"tcp://{IP_ESTAGIO_2}:{PORT_2}")
    print(f"Estágio 3 (Consumidor Final) conectado ao Estágio 2 ({IP_ESTAGIO_2}:{PORT_2})...")

    while True:
        dados_finais = socket.recv()
        resultado = pickle.loads(dados_finais)
        print(f"[Consumidor Final] Resultado processado recebido do Pipeline: {resultado}")
        # Simula o tempo de armazenamento ou exibição final
        time.sleep(0.5)

if __name__ == "__main__":
    consumidor()
