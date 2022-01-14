import sys
import grpc
import socket
import threading
from concurrent import futures
from servicos_pb2_grpc import ServerCentralizadorServicer, add_ServerCentralizadorServicer_to_server
from servicos_pb2 import RespostaRegistro, RespostaMapeamento, RespostaTerminoCentralizador

''' Servidor centralizador responsável por registrar chaves e quais serviços contém essas chaves '''
class ServerCentralizador(ServerCentralizadorServicer):

    ''' Inicializa o dicionário das chaves guardadas e o evento de término do servidor '''
    def __init__(self, eventoTermino):
        self.eventoTermino = eventoTermino
        self.dicionario = {}

    ''' Registra um novo conjunto de chaves de um serviço '''
    def Registrar(self, request, context):
        # Numero de chaves processadas
        chavesProcessadas = 0
        # Para cada chave na lista de chaves do serviço
        for chave in request.listaChaves:
            # Adiciona no dicionário essa chave e salva o serviço que a contém
            # Se ela já existia, ela é sobrescrita
            self.dicionario[chave] = request.servico
            # Indica que mais uma chave foi processada
            chavesProcessadas+=1
        # Retorna o número de chaves processadas
        return RespostaRegistro(chavesProcessadas=chavesProcessadas)

    ''' Recebe uma chave e retorna o serviço que a contém em seu registro '''
    def Mapear(self, request, context):
        # Se a chave está registrada
        if request.chave in self.dicionario:
            # Retorna o serviço que contém a chave
            return RespostaMapeamento(servico=self.dicionario[request.chave])
        # Senão retorna um serviço vazio
        return RespostaMapeamento(servico='')

    ''' Encerra a execução do servidor '''
    def Termina(self, request, context):
        # Indica que o evento de término ocorreu
        self.eventoTermino.set()
        # Retorna o número de chaves registradas no servidor
        return RespostaTerminoCentralizador(chavesRegistradas=len(self.dicionario))

if __name__ == '__main__':
    # Constroi o endereço do servidor
    porta = sys.argv[1]
    endereco = '%s:%s' % (socket.INADDR_ANY, porta)
    # Declara um evento para indicar o término do servidor
    eventoTermino = threading.Event()
    # Declara a instância do servidor de GRPC
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # Adiciona o servidor centralizador à instância do servidor declarada
    add_ServerCentralizadorServicer_to_server(ServerCentralizador(eventoTermino), server)
    # Inicializa o servidor no seu endereço com a porta indicada por parâmetro
    server.add_insecure_port(endereco)
    # Inicia o servidor
    server.start()
    # Espera pelo evento de término
    eventoTermino.wait()
    # Encerra o servidor, esperando 1 segundo para interrompar as tarefas já em andamento
    # Essa espera foi feita para evitar problemas causados por condições de corrida ao disparar o evento de término
    server.stop(1)
