.PHONY: clean
clean:
	$(MAKE) -C proto clean
	$(MAKE) -C go clean
	$(MAKE) -C python clean
	$(MAKE) -C java clean
	$(MAKE) -C plugin clean
	$(MAKE) -C presentation clean

.PHONY: snippets
snippets:
	$(MAKE) -C proto all
	$(MAKE) -C go all
	$(MAKE) -C python all
	$(MAKE) -C java all
	$(MAKE) -C plugin all

.PHONY: presentation
presentation:
	$(MAKE) -C presentation all

.PHONY: all
all: snippets presentation
