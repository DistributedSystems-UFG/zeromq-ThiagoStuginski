import zmq
import pickle
from const_pipeline import IP_ESTAGIO_1, PORT_1, PORT_2

def intermediario():
    context = zmq.Context()
    
    # Lado PULL: Conecta ao gerador (Estágio 1)
    receptor = context.socket(zmq.PULL)
    receptor.connect(f"tcp://{IP_ESTAGIO_1}:{PORT_1}")
    
    # Lado PUSH: Vincula para o consumidor final se conectar (Estágio 3)
    emissor = context.socket(zmq.PUSH)
    emissor.bind(f"tcp://0.0.0.0:{PORT_2}")
    
    print(f"Estágio 2 conectado ao Estágio 1 ({IP_ESTAGIO_1}:{PORT_1}) e aguardando Estágio 3 na porta {PORT_2}...")

    while True:
        # Recebe o dado bruto
        dados_brutos = receptor.recv()
        valor = pickle.loads(dados_brutos)
        print(f"[Intermediário] Recebido do estágio 1: {valor}")
        
        # Nova Funcionalidade / Transformação: Eleva o número ao quadrado
        valor_transformado = valor ** 2
        print(f"[Intermediário] Transformado para: {valor_transformado} (enviando ao estágio 3...) ")
        
        # Envia para a frente no pipeline
        emissor.send(pickle.dumps(valor_transformado))

if __name__ == "__main__":
    intermediario()
