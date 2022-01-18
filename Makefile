
run_cli_pares: build_grpc
	python3 client_pares.py $(arg)

run_serv_pares_1: build_grpc
	python3 server_pares.py $(arg)

run_serv_pares_2: build_grpc
	python3 server_pares.py $(arg) 1

run_serv_central: build_grpc
	python3 server_central.py $(arg)

run_cli_central: build_grpc
	python3 client_central.py $(arg)

build_grpc:
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. central.proto
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. pares.proto

clean: 
	rm -f central_pb2_grpc.py central_pb2.py pares_pb2_grpc.py pares_pb2.py
