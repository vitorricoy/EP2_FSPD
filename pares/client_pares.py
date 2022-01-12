
import grpc
import sys
from server_pares_pb2_grpc import ServerParesStub
from server_pares_pb2 import RequisicaoInsercao, RequisicaoAtivacao, RequisicaoConsulta, RequisicaoTermino

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
                if resposta.status == 0:
                    print('Chave', comandos[1], 'inserida')
                else:
                    print('Chave já existe')

            elif comandos[0] == 'C':
                resposta = stub.Consulta(RequisicaoInsercao(chave=int(comandos[1])))
                if resposta.resultado:
                    print('Chave', comandos[1], 'encontrada com valor', resposta.resultado)
                else:
                    print('Chave', comandos[1], 'não encontrada')
            elif comandos[0] == 'A':
                resposta = stub.Ativa(RequisicaoAtivacao())
                if resposta.status == 0:
                    print('Comando de ativação recebido pelo servidor')
                else:
                    raise Exception('Erro ao enviar o comando de ativação ao servidor')
            elif comandos[0] == 'T':
                resposta = stub.Termina(RequisicaoTermino())
                if resposta.status != 0:
                    raise Exception('Erro ao encerrar o servidor')
                exit(0)
            else:
                continue # Ignora mensagem invalida
