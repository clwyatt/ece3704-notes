
OPTIONS= -s -t html -V lang=en --embed-resources --mathml

all: lecture3.html

%.pdf: %.tikz
	pdflatex $<

%.svg: %.pdf
	pdf2svg $< $@

lecture3.html: lecture3.tex fig3_1.svg fig3_2.svg fig3_3.svg fig3_4.svg fig3_5.svg fig3_6.svg
	pandoc $(OPTIONS) lecture3.tex -o lecture3.html

view: lecture3.html
	open lecture3.html

clean:
	$(RM) *.log *.aux *.pdf

realclean: clean
	$(RM) *.svg *.html




