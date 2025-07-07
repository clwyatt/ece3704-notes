# build html from tex files and tikz figures

# set final output file
TARGET= lecture6.html

# list figure svg files
DEPS= fig6_1.svg fig6_2.svg fig6_3.svg fig6_4.svg fig6_5.svg fig6_6.svg fig6_7.svg fig6_8.svg fig6_9.svg fig6_10.svg fig6_11.svg

CSS=../style/style.css

OPTIONS= -s -t html --toc=true --css=$(CSS) -V lang=en --embed-resources --mathml

.SECONDARY: # prevent removal of intermediate files

all: $(TARGET)

%.pdf: %.tikz
	pdflatex --shell-escape $<

%.svg: %.pdf
	pdf2svg $< $@

%.html: %.tex $(DEPS) $(CSS)
	pandoc $(OPTIONS) $< -o $@

view: $(TARGET)
	open $<

clean:
	$(RM) *.log *.aux *.pdf *.dat *.table *.script

realclean: clean
	$(RM) *.svg *.html




