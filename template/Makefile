# build html from tex files and tikz figures

# set final output file
TARGET= lectureN.html

# list figure svg files
DEPS= figN_1.svg

CSS=../style/style.css
HEADER=../style/header.html
FOOTER=../style/footer.html

OPTIONS= -s -t html --toc=true --css=$(CSS) --include-before $(HEADER) --include-after $(FOOTER) -V lang=en --embed-resources --mathml

.SECONDARY: # prevent removal of intermediate files

all: $(TARGET)

%.dvi: %.tikz
	latex $<

%.svg: %.dvi
	dvisvgm --font-format=woff -p1 --output=$@ $<

%.html: %.tex $(DEPS) $(CSS) $(HEADER) $(FOOTER)
	pandoc $(OPTIONS) $< -o $@

view: $(TARGET)
	open $<

clean:
	$(RM) *.log *.aux *.dvi

realclean: clean
	$(RM) $(DEPS) $(TARGET)




