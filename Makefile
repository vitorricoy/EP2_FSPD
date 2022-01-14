
run_cli_pares: build_grpc
	python3 client_pares.py $(ARGS)

run_serv_pares_1: build_grpc
	python3 server_pares.py $(ARGS)

run_serv_pares_2: build_grpc
	python3 server_pares.py $(ARGS) 1

run_serv_central: build_grpc
	python3 server_central.py $(ARGS)

run_cli_central: build_grpc
	python3 client_central.py $(ARGS)

build_grpc:
	python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. servicos.proto

clean: 
	rm -f servicos_pb2.py servicos_pb2_grpc.py