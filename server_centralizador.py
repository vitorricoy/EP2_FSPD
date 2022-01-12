import sys
import grpc
import threading
from concurrent import futures
from servicos_pb2_grpc import ServerCentralizadorServicer, add_ServerCentralizadorServicer_to_server
from servicos_pb2 import RespostaRegistro, RespostaMapeamento, RespostaTermino

class ServerCentralizador(ServerCentralizadorServicer):

    def __init__(self, eventoTermino):
        self.eventoTermino = eventoTermino
        self.dicionario = {}

    def Registrar(self, request, context):
        chavesProcessadas = 0
        for chave in request.listaChaves:
            self.dicionario[chave] = request.servico
            chavesProcessadas+=1
        return RespostaRegistro(chavesProcessadas=chavesProcessadas)

    def Mapear(self, request, context):
        if request.chave in self.dicionario:
            return RespostaMapeamento(servico=self.dicionario[request.chave])
        return RespostaMapeamento(servico='')

    def Termina(self, request, context):
        self.eventoTermino.set()
        return RespostaTermino(chavesRegistradas=len(self.dicionario))

if __name__ == '__main__':
    porta = sys.argv[1]
    eventoTermino = threading.Event()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_ServerCentralizadorServicer_to_server(ServerCentralizador(eventoTermino), server)
    server.add_insecure_port('localhost:%s' % porta)
    server.start()
    eventoTermino.wait()
    server.stop(0)