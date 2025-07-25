# build html from tex files and tikz figures

# set final output file
TARGET= lecture8.html

# list figure svg files
DEPS= fig8_1.svg fig8_2.svg fig8_3.svg fig8_4.svg fig8_5.svg fig8_6.svg

CSS=../style/style.css

OPTIONS= -s -t html --toc=true --css=$(CSS) -V lang=en --embed-resources --mathml

.SECONDARY: # prevent removal of intermediate files

all: $(TARGET)

%.dvi: %.tikz
	latex $<

%.svg: %.dvi
	dvisvgm --font-format=woff -p1 --output=$@ $<

%.html: %.tex $(DEPS) $(CSS)
	pandoc $(OPTIONS) $< -o $@

view: $(TARGET)
	open $<

clean:
	$(RM) *.log *.aux *.dvi

realclean: clean
	$(RM) *.svg *.html




