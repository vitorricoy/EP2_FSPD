
run_cli_pares: build_grpc
	python3 client_pares.py $(arg)

run_serv_pares_1: build_grpc
	python3 server_pares.py $(arg)

run_serv_pares_2: build_grpc
	python3 server_pares.py $(arg) 1

run_serv_central: build_grpc
	python3 server_centralizador.py $(arg)

run_cli_central: build_grpc
	python3 client_centralizador.py $(arg)

build_grpc:
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. servicos.proto

clean: 
	rm -f servicos_pb2.py servicos_pb2_grpc.py
