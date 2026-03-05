# run python scripts to create pdf, svg, and png versions of example figures
# use a virtual enviroment to make more reproducible
VENV_DIR = .venv
PYTHON = $(VENV_DIR)/bin/python3

SOURCES=$(wildcard *.py)
SVGTARGETS= $(SOURCES:%.py=%.svg) # pdf and png created at same time
PDFTARGETS= $(SOURCES:%.py=%.pdf)
PNGTARGETS= $(SOURCES:%.py=%.png)

all: $(SVGTARGETS)

%.svg: %.py
	$(PYTHON) $<

clean:
	$(RM) $(SVGTARGETS)  $(PDFTARGETS)  $(PNGTARGETS)
