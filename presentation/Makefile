.PHONY: clean
clean:
	@rm -rfv main.aux main.log main.nav main.out main.pdf main.snm main.toc main.vrb

main.pdf:
	@pdflatex main.tex 2>&1 > /dev/null

.PHONY: all
all: main.pdf