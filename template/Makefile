# build html from tex files and tikz figures

# set final output file
TARGET= lectureN.html

# list figure svg files
DEPS= figN_1.svg

CSS=../style/style.css

OPTIONS= -s -t html --toc=true --css=$(CSS) -V lang=en --embed-resources --mathml

.SECONDARY: # prevent removal of intermediate files

all: $(TARGET)

%.pdf: %.tikz
	pdflatex $<

%.svg: %.pdf
	pdf2svg $< $@

%.html: %.tex $(DEPS) $(CSS)
	pandoc $(OPTIONS) $< -o $@

view: $(TARGET)
	open $<

clean:
	$(RM) *.log *.aux *.pdf

realclean: clean
	$(RM) *.svg *.html




