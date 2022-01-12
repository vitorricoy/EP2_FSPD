import sys
import grpc
import threading
from concurrent import futures
from servicos_pb2_grpc import ServerCentralizadorStub, ServerParesServicer, add_ServerParesServicer_to_server
from servicos_pb2 import RequisicaoRegistro, RespostaInsercao, RespostaAtivacao, RespostaConsulta, RespostaTermino

class ServerPares(ServerParesServicer):

    def __init__(self, ativacao, eventoTermino, endereco):
        self.ativacao = ativacao
        self.eventoTermino = eventoTermino
        self.dicionario = {}
        self.endereco = endereco

    def Insere(self, request, context):
        if request.chave in self.dicionario:
            return RespostaInsercao(status=1)
        self.dicionario[request.chave] = request.valor
        return RespostaInsercao(status=0)

    def Consulta(self, request, context):
        if request.chave in self.dicionario:
            return RespostaConsulta(resultado=self.dicionario[request.chave])
        return RespostaConsulta(resultado='')

    def Ativa(self, request, context):
        if self.ativacao:
            with grpc.insecure_channel(request.servico) as channel:  
                stub = ServerCentralizadorStub(channel)
                resposta = stub.Registrar(RequisicaoRegistro(servico=self.endereco, listaChaves=list(self.dicionario.keys())))
                if resposta.chavesProcessadas != len(self.dicionario):
                    raise Exception('Erro ao registrar chaves no servidor centralizador')
                return RespostaAtivacao(status=0)
        else:
            return RespostaAtivacao(status=0)

    def Termina(self, request, context):
        self.eventoTermino.set()
        return RespostaTermino(status=0)

if __name__ == '__main__':
    porta = sys.argv[1]
    endereco = 'localhost:%s' % porta
    ativacao = False
    if len(sys.argv) > 2:
        ativacao = True
    eventoTermino = threading.Event()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_ServerParesServicer_to_server(ServerPares(ativacao, eventoTermino, endereco), server)
    server.add_insecure_port(endereco)
    server.start()
    eventoTermino.wait()
    server.stop(0)