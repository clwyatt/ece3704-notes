# build html from tex files and tikz figures

# set final output file
TARGET= lecture3.html

# list figure svg files
DEPS= fig3_1.svg fig3_2.svg fig3_3.svg fig3_4.svg fig3_5.svg fig3_6.svg fig3_7.svg fig3_8.svg fig3_9.svg

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




