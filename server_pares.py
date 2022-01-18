import sys
import grpc
import socket
import threading
from concurrent import futures
from pares_pb2_grpc import ServerParesServicer, add_ServerParesServicer_to_server
from pares_pb2 import RespostaInsercao, RespostaAtivacao, RespostaConsulta, RespostaTerminoPares
from central_pb2_grpc import ServerCentralizadorStub
from central_pb2 import RequisicaoRegistro

''' Servidor de pares responsável por registrar chaves, consultar chaves e enviar seu conjunto de chaves 
e sua indentificação a um servidor central '''
class ServerPares(ServerParesServicer):

    ''' Inicializa o dicionário das chaves guardadas, o evento de término do servidor, seu próprio endereço e
    uma flag que indica se ele deve se comunicar com um servidor central '''
    def __init__(self, ativacao, eventoTermino, endereco):
        self.ativacao = ativacao
        self.eventoTermino = eventoTermino
        self.dicionario = {}
        self.endereco = endereco

    ''' Insere uma nova chave no registro do servidor '''
    def Insere(self, request, context):
        # Se a chave está presente no dicionário
        if request.chave in self.dicionario:
            # Retorna um status indicando o fracasso em inserir o par chave-valor
            return RespostaInsercao(status=-1)
        # Senão, a insere com o valor indicado
        self.dicionario[request.chave] = request.valor
        # Retorna um status indicando sucesso
        return RespostaInsercao(status=0)

    ''' Consulta uma chave no registro do servidor '''
    def Consulta(self, request, context):
        # Se a chave está no dicionário
        if request.chave in self.dicionario:
            # Retorna o valor da chave
            return RespostaConsulta(resultado=self.dicionario[request.chave])
        # Senão, retorna um resultado vazio
        return RespostaConsulta(resultado='')

    ''' Envia o conjunto de chaves registrada e o endereço de serviço do servidor a um servidor central '''
    def Ativa(self, request, context):
        # Se a flag indica que esse servidor deve se comunicar com o servidor central
        if self.ativacao:
            # Se conecta a um servidor central enviado pela requisição
            with grpc.insecure_channel(request.servico) as channel:
                # Declara o Stub do servidor central
                stub = ServerCentralizadorStub(channel)
                # Associa todas as chaves ao endereço desse servidor no servidor central
                resposta = stub.Registrar(RequisicaoRegistro(servico=self.endereco, listaChaves=list(self.dicionario.keys())))
                # Se não foram processadas todas as chaves
                if resposta.chavesProcessadas != len(self.dicionario):
                    # Gera umm erro na execução do servidor, pois isso não pode acontecer
                    raise Exception('Erro ao registrar chaves no servidor centralizador')
                # Senão, retorna o número de chaves registradas
                return RespostaAtivacao(chavesProcessadas=resposta.chavesProcessadas)
        else:
            # Senão, apenas retorna que nenhuma chave foi processada
            return RespostaAtivacao(chavesProcessadas=0)

    ''' Encerra a execução do servidor '''
    def Termina(self, request, context):
        # Indica que o evento de término ocorreu
        self.eventoTermino.set()
        # Retorna um status indicando o sucesso
        return RespostaTerminoPares(status=0)

if __name__ == '__main__':
    # Constroi o endereço do servidor
    porta = sys.argv[1]
    endereco = '%s:%s' % (socket.INADDR_ANY, porta)
    # Verifica se a flag de ativação será verdadeira ou falsa
    ativacao = False
    if len(sys.argv) > 2:
        ativacao = True
    # Declara um evento para indicar o término do servidor
    eventoTermino = threading.Event()
    # Declara a instância do servidor de GRPC
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # Adiciona o servidor de pares à instância do servidor declarada
    add_ServerParesServicer_to_server(ServerPares(ativacao, eventoTermino, '%s:%s' % (socket.getfqdn(), porta)), server)
    # Inicializa o servidor no seu endereço com a porta indicada por parâmetro
    server.add_insecure_port(endereco)
    # Inicia o servidor
    server.start()
    # Espera pelo evento de término
    eventoTermino.wait()
    # Encerra o servidor, esperando 1 segundo para interrompar as tarefas já em andamento
    # Essa espera foi feita para evitar problemas causados por condições de corrida ao disparar o evento de término
    server.stop(1)
