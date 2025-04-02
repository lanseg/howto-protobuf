.PHONY: clean
clean:
	rm -rfv schema_pb2.py poetry.lock __pycache__

deps:
	cp -rfv ../proto/schema_pb2.py ./

all: deps
	poetry install
	poetry lock
# PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python
