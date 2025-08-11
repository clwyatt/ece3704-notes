# build pdf, svg, and png versions of tikz figures

SOURCES=$(wildcard fig*.tikz)
PDFTARGETS= $(SOURCES:%.tikz=%.pdf)
SVGTARGETS= $(SOURCES:%.tikz=%.svg)
PNGTARGETS= $(SOURCES:%.tikz=%.png)

.SECONDARY: # prevent removal of intermediate files

all: $(PDFTARGETS) $(SVGTARGETS) $(PNGTARGETS) 

%.dvi: %.tikz
	latex -interaction=batchmode --shell-escape $<

%.svg: %.dvi
	@echo Converting to $@
	dvisvgm --font-format=woff -p1 --output=$@ $<

%.pdf: %.tikz
	@echo Converting to $@
	pdflatex -interaction=batchmode --shell-escape $<

%.png: %.pdf
	@echo Converting to $@
	pdftocairo -png -transp -r 300 -singlefile -transp $< 

clean:
	$(RM) *.aux *.log *.dvi *.dat *.script *.table

realclean: clean
	$(RM) *.svg *.pdf *.png
