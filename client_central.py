
import grpc
import sys
from pares_pb2_grpc import ServerParesStub
from pares_pb2 import RequisicaoConsulta
from central_pb2_grpc import ServerCentralizadorStub
from central_pb2 import RequisicaoMapeamento, RequisicaoTerminoCentralizador

''' Cliente que se conecta ao servidor centralizador e faz consultas nele 
e nos servidores de pares retornados pelo servidor centralizador '''
if __name__ == '__main__':
    enderecoServidor = sys.argv[1]
    # Inicializa o canal de conexão entre o cliente e o servidor centralizador
    with grpc.insecure_channel(enderecoServidor) as canalCentralizador:  
        # Declara o Stub do servidor centralizador usado pelo cliente
        stub = ServerCentralizadorStub(canalCentralizador)
        # Possibilita o encerramento do cliente com uma mensagem de erro mais amigável, apesar de ser mais simples
        try:
            # Le linhas da entrada padrão até que um 'T' seja recebido
            while True:
                linha = input()
                # Se a linha está vazia ele é ignorada
                if len(linha) == 0:
                    continue
                # Divide o comando e seus argumentos pelo separador
                comandos = linha.split(',')
                # Se o comando foi de consulta
                if comandos[0] == 'C':
                    # Chama a função de mapear do servidor com a chave recebida
                    resposta = stub.Mapear(RequisicaoMapeamento(chave=int(comandos[1])))
                    # Se o mapeamento respondeu um serivço
                    if resposta.servico:
                        # Imprime o serviço recebido
                        print(resposta.servico,':', end='', sep='')
                        # Se conecta ao serviço de pares
                        with grpc.insecure_channel(resposta.servico) as canalPares:  
                            # Declara o Stub dos servidores de pares
                            paresStub = ServerParesStub(canalPares)
                            # Consulta pela chave no servidor de pares
                            resposta = paresStub.Consulta(RequisicaoConsulta(chave=int(comandos[1])))
                            # Imprime o numero de chaves registradas pelo servidor centralizador
                            print(resposta.resultado)
                    else:
                        # Imprime uma linha vazia no caso da chave não estar registrada no servidor centralizador
                        print()
                    
                # Se o comando foi de término
                elif comandos[0] == 'T':
                    # Envia o comando de término para o servidor centralizador
                    resposta = stub.Termina(RequisicaoTerminoCentralizador())
                    # Imprime a resposta recebida
                    print(resposta)
                    # Encerra o cliente
                    exit(0)
                else:
                    # Ignora mensagem inválida
                    continue
        except grpc.RpcError as erro:
            # Imprime o status code do erro que levou o cliente a ser encerrado
            print('Cliente encerrado com o erro: %s' % erro.code())
