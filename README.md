# Protobuf talks

That is a source code for a basic 10-minute introduction about the protocol buffers: basic syntax, how the code generation works and how a binary proto is structured.

## Structure

* Protocol buffers code
  * proto/
  * plugin/
* Code snippets
  * go/
  * java/
  * python/
* presentation/

## Building everything

Simple ```make all``` (```make presentation``` or ```make snippets```) will do the thing, but it requires installing some packages for code (compilers, protobuf compiler) or presentation (latex).

### Ubuntu

```bash
# For code examples
apt install git make protobuf-compiler python3 python3-poetry golang maven protoc-gen-go

# For presentation (an overkill, but should have everything needed)
apt install texlive-full
```

### Arch Linux

```bash
# For code examples (without protoc-gen-go)
pacman -S git make protobuf python poetry go maven

# For presentation (an overkill, but should have everything needed)
pacman -S texlive texlive-pictures texlive-latexextra
```

#### Installing protoc-gen-go

Installing protoc-gen-go is a bit more tricky: it could be found only in AUR, so you should either use yay, manual PKGBUILD or install it from go.

Using go:

1. Install binary: ```go install google.golang.org/protobuf/cmd/protoc-gen-go@latest```.
2. Add it to PATH: ```export PATH=$PATH:$HOME/go/bin/```

### MacOS

```bash
# For code examples
brew install git make protobuf python3 poetry go maven protoc-gen-go

# For presentation (an overkill, but should have everything needed)
brew install MacTeX
```
