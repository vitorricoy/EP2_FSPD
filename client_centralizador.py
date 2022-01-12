
import grpc
import sys
from servicos_pb2_grpc import ServerCentralizadorStub, ServerParesStub
from servicos_pb2 import RequisicaoMapeamento, RequisicaoTermino, RequisicaoConsulta

if __name__ == '__main__':
    enderecoServidor = sys.argv[1]
    with grpc.insecure_channel(enderecoServidor) as canalCentralizador:  
        stub = ServerCentralizadorStub(canalCentralizador)
        while True:
            linha = input()
            if len(linha) == 0: # Ignora linha vazia
                continue
            comandos = linha.split(',')
            if comandos[0] == 'C':
                resposta = stub.Mapear(RequisicaoMapeamento(chave=int(comandos[1])))
                if resposta.servico:
                    print(resposta.servico,':', end='', sep='')
                    with grpc.insecure_channel(resposta.servico) as canalPares:  
                        stub = ServerParesStub(canalPares)
                        resposta = stub.Consulta(RequisicaoConsulta(chave=int(comandos[1])))
                        print(resposta.resultado)
            elif comandos[0] == 'T':
                resposta = stub.Termina(RequisicaoTermino())
                print(resposta)
                exit(0)
            else:
                continue # Ignora mensagem invalida
