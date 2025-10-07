# build html from tex files and tikz/asy/ipe figures

.PHONY: dir figures

CSS=style.css
HEADER=pandoc/header.html
FOOTER=pandoc/footer.html

OPTIONS= -s -t html --shift-heading-level-by=1 --css=$(CSS) --include-before $(HEADER) --include-after $(FOOTER) -V lang=en --mathjax

SOURCES=$(wildcard lecture*.tex)
SOURCES+=appendix.tex
TARGETS= $(SOURCES:%.tex=docs/%.html)

all: dir figures html docs/about.html docs/index.html
	cp style.css docs
	cp -r images docs
	cp -r raw docs

html: $(TARGETS)

dir:
	mkdir -p docs/figures

figures:
	make -C figures -j 4 -f Makefile_tikz
	make -C figures -f Makefile_ipe
	cp figures/*.svg docs/figures

docs/about.html: about.md $(CSS) $(HEADER) $(FOOTER)
	pandoc $(OPTIONS) $< -o $@

docs/index.html: index.md $(CSS) $(HEADER) $(FOOTER)
	pandoc $(OPTIONS) $< -o $@

docs/%.html: %.tex $(CSS) $(HEADER) $(FOOTER)
	pandoc $(OPTIONS) --toc=true $< -o $@

clean:
	make -C figures -f Makefile_tikz clean
	make -C figures -f Makefile_ipe clean
	$(RM) *.log *.aux *.dvi

realclean: clean
	make -C figures -f Makefile_tikz realclean
	$(RM) -rf docs/*




