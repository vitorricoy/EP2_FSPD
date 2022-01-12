
import grpc
import sys
from servicos_pb2_grpc import ServerParesStub
from servicos_pb2 import RequisicaoInsercao, RequisicaoAtivacao, RequisicaoConsulta, RequisicaoTermino

if __name__ == '__main__':
    enderecoServidor = sys.argv[1]
    with grpc.insecure_channel(enderecoServidor) as channel:  
        stub = ServerParesStub(channel)
        while True:
            linha = input()
            if len(linha) == 0: # Ignora linha vazia
                continue
            comandos = linha.split(',')
            if comandos[0] == 'I':
                resposta = stub.Insere(RequisicaoInsercao(chave=int(comandos[1]), valor=comandos[2]))
                print(resposta.status)
            elif comandos[0] == 'C':
                resposta = stub.Consulta(RequisicaoInsercao(chave=int(comandos[1])))
                print(resposta.resultado)
            elif comandos[0] == 'A':
                resposta = stub.Ativa(RequisicaoAtivacao())
                print(resposta.status)
            elif comandos[0] == 'T':
                resposta = stub.Termina(RequisicaoTermino())
                print(resposta.status)
                exit(0)
            else:
                continue # Ignora mensagem invalida
