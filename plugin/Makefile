.PHONY: clean
clean:
	rm -rfv schema.proto generated poetry.lock __pycache__

deps:
	cp -rfv ../proto/schema.proto ./

all: deps
	poetry install
	poetry lock
