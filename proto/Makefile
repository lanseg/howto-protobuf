SHELL = /bin/sh
OUT = "./"

schema.pb.go:
	protoc -I=. --go_out=$(OUT) --go_opt=paths=source_relative schema.proto

schema_pb2.py:
	protoc -I=. --python_out=$(OUT) schema.proto

Schema.java:
	protoc -I=. --java_out=$(OUT) schema.proto

schema_cpp:
	mkdir schema_cpp
	protoc -I=. --cpp_out=$(OUT)/schema_cpp schema.proto

all: schema.pb.go Schema.java schema_pb2.py Schema.java schema_cpp

clean:
	rm -rfv org schema.pb.go schema_pb2.py Schema.java schema_cpp
