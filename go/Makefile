.PHONY: clean
clean:
	rm -rfv go.mod go.sum proto main_go

deps:
	mkdir -p proto
	cp -rfv ../proto/schema.pb.go proto/

all: deps
	go mod init demo
	go mod tidy
	go build -o main_go main.go