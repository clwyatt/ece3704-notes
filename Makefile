# build html and pdf from tex files and tikz/asy/ipe figures

.PHONY: dir figures examples

CSS=style.css
HEADER=pandoc/header.html
FOOTER=pandoc/footer.html

OPTIONS= -s -t html --shift-heading-level-by=1 --default-image-extension=svg --css=$(CSS) --include-before $(HEADER) --include-after $(FOOTER) -V lang=en --mathjax

SOURCES=$(wildcard lecture*.tex)
SOURCES+=appendix.tex
HTML_TARGETS=$(SOURCES:%.tex=docs/%.html)
PDF_TARGETS=$(SOURCES:%.tex=docs/%.pdf)

all: dir figures examples html pdf docs/about.html docs/index.html
	rsync -avz style.css docs
	rsync -avz figures/*.svg docs/figures
	rsync -avz examples/*.svg docs/examples

html: $(HTML_TARGETS)

pdf: $(PDF_TARGETS)

dir:
	mkdir -p docs/figures docs/examples

figures:
	make -C figures -j 4 -f Makefile_tikz
	make -C figures -f Makefile_ipe

examples:
	make -C examples

docs/about.html: about.md $(CSS) $(HEADER) $(FOOTER)
	pandoc $(OPTIONS) $< -o $@

docs/index.html: index.md $(CSS) $(HEADER) $(FOOTER)
	pandoc $(OPTIONS) $< -o $@

docs/%.html: %.tex $(CSS) $(HEADER) $(FOOTER)
	pandoc $(OPTIONS) --toc=true $< -o $@

docs/%.pdf: %.tex
	pandoc -s -t latex --default-image-extension=pdf $< --template=template.tex -o $@

preview: all
# this does not reload
# cd docs && python3 -m http.server

# this does not seem to work either
	cd docs; browser-sync start --server --files "*.html, figures/*"

clean:
	make -C figures -f Makefile_tikz clean
	make -C figures -f Makefile_ipe clean
	$(RM) *.log *.aux *.dvi

realclean: clean
	make -C figures -f Makefile_tikz realclean
	$(RM) -rf docs/*




