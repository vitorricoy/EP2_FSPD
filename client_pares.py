
import grpc
import sys
from servicos_pb2_grpc import ServerParesStub
from servicos_pb2 import RequisicaoInsercao, RequisicaoAtivacao, RequisicaoConsulta, RequisicaoTermino

''' Cliente que se conecta a um servidor de pares e insere valores, faz consultas e envia ativação a ele. '''
if __name__ == '__main__':
    enderecoServidor = sys.argv[1]
    # Conecta no servidor de pares
    with grpc.insecure_channel(enderecoServidor) as channel:  
        # Declara o Stub do servidor de pares usado pelo cliente
        stub = ServerParesStub(channel)
        # Le linhas da entrada padrão até que um 'T' seja recebido
        while True:
            linha = input()
            # Se a linha está vazia ele é ignorada
            if len(linha) == 0:
                continue
            # Divide o comando e seus argumentos pelo separador
            comandos = linha.split(',')
            # Se o comando foi de inserção
            if comandos[0] == 'I':
                # Chama a função de inserir um novo par chave-valor no servidor de pares
                resposta = stub.Insere(RequisicaoInsercao(chave=int(comandos[1]), valor=comandos[2]))
                # Imprime o status da inserção
                print(resposta.status)
            # Se o comando foi de consulta
            elif comandos[0] == 'C':
                # Chama a função de consultar uma chave no servidor de pares
                resposta = stub.Consulta(RequisicaoConsulta(chave=int(comandos[1])))
                # Imprime o resultado da consulta
                print(resposta.resultado)
            # Se o comando foi de ativação
            elif comandos[0] == 'A':
                # Chama a função de ativação do servidor de pares
                resposta = stub.Ativa(RequisicaoAtivacao())
                # Imprime o número de chaves processadas pela ativação
                print(resposta.chavesProcessadas)
            # Se o comando foi de término
            elif comandos[0] == 'T':
                # Chama a função de terminar o servidor de pares
                resposta = stub.Termina(RequisicaoTermino())
                # Imprime o status do comando de término
                print(resposta.status)
                # Encerra o cliente
                exit(0)
            else:
                # Ignora mensagem invalida
                continue
