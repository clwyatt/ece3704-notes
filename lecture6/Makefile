# build html from tex files and tikz figures

# set final output file
TARGET= lecture6.html

# list figure svg files
DEPS= fig6_1.svg fig6_2.svg fig6_3.svg fig6_4.svg fig6_5.svg fig6_6.svg fig6_7.svg fig6_8.svg fig6_9.svg fig6_10.svg fig6_11.svg

CSS=../style/style.css
HEADER=../style/header.html
FOOTER=../style/footer.html

OPTIONS= -s -t html --toc=true --shift-heading-level-by=1 --css=$(CSS) --include-before $(HEADER) --include-after $(FOOTER) -V lang=en --embed-resources --mathml

.SECONDARY: # prevent removal of intermediate files

all: $(TARGET)

%.dvi: %.tikz
	latex --shell-escape $<

%.svg: %.dvi
	dvisvgm --font-format=woff -p1 --output=$@ $<

%.html: %.tex $(DEPS) $(CSS) $(HEADER) $(FOOTER)
	pandoc $(OPTIONS) $< -o $@

view: $(TARGET)
	open $<

clean:
	$(RM) *.log *.aux *.dvi *.dat *.table *.script

realclean: clean
	$(RM) $(DEPS) $(TARGET)




