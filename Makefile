.PHONY: clean
clean:
	$(MAKE) -C proto clean
	$(MAKE) -C go clean
	$(MAKE) -C python clean
	$(MAKE) -C java clean
	$(MAKE) -C presentation clean

.PHONY: all
all:
	$(MAKE) -C proto all
	$(MAKE) -C go all
	$(MAKE) -C python all
	$(MAKE) -C java all
	$(MAKE) -C presentation all