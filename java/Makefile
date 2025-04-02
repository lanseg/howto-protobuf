.PHONY: clean
clean:
	rm -rfv src/main/java/org/lanseg/demo/proto
	mvn clean

deps:
	cp -rfv ../proto/org ./src/main/java/

build: deps
	mvn clean compile assembly:single

all: build