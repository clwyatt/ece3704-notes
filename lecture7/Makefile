# build html from tex files and tikz figures

# set final output file
TARGET= lecture7.html

# list figure svg files
DEPS= 

CSS=../style/style.css

OPTIONS= -s -t html --toc=true --css=$(CSS) -V lang=en --embed-resources --mathml

.SECONDARY: # prevent removal of intermediate files

all: $(TARGET)

%.dvi: %.tikz
	latex $<

%.svg: %.dvi
	dvisvgm -p1 --output=$@ $<

%.html: %.tex $(DEPS) $(CSS)
	pandoc $(OPTIONS) $< -o $@

view: $(TARGET)
	open $<

clean:
	$(RM) *.log *.aux *.dvi

realclean: clean
	$(RM) *.svg *.html




