# build html from tex files and tikz figures

# set final output file
TARGET= lecture3.html

# list figure svg files
DEPS= fig3_1.svg fig3_2.svg fig3_3.svg fig3_4.svg fig3_5.svg fig3_6.svg fig3_7.svg fig3_8.svg fig3_9.svg

CSS=../style/style.css
HEADER=../style/header.html
FOOTER=../style/footer.html

OPTIONS= -s -t html --toc=true --shift-heading-level-by=1 --css=$(CSS) --include-before $(HEADER) --include-after $(FOOTER) -V lang=en --embed-resources --mathjax

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




