import sys
import grpc
import threading
from concurrent import futures
from server_pares_pb2_grpc import ServerParesServicer, add_ServerParesServicer_to_server
from server_pares_pb2 import RespostaInsercao, RespostaAtivacao, RespostaConsulta, RespostaTermino

class ServerPares(ServerParesServicer):

    def __init__(self, ativacao, eventoTermino):
        self.ativacao = ativacao
        self.eventoTermino = eventoTermino
        self.dicionario = {}

    def Insere(self, request, context):
        if request.chave in self.dicionario:
            return RespostaInsercao(status=1)
        self.dicionario[request.chave] = request.valor
        return RespostaInsercao(status=0)

    def Consulta(self, request, context):
        if request.chave in self.dicionario:
            return RespostaConsulta(resultado=self.dicionario[request.chave])
        return RespostaConsulta(resultado=None)

    def Ativa(self, request, context):
        if self.ativacao:
            pass
        else:
            return RespostaAtivacao(status=0)

    def Termina(self, request, context):
        self.eventoTermino.set()
        return RespostaTermino(status=0)

if __name__ == '__main__':
    porta = sys.argv[1]
    ativacao = False
    if len(sys.argv) > 2:
        ativacao = True
    eventoTermino = threading.Event()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_ServerParesServicer_to_server(ServerPares(ativacao, eventoTermino), server)
    server.add_insecure_port('localhost:%s' % porta)
    server.start()
    eventoTermino.wait()
    server.stop(0)