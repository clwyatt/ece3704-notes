
OPTIONS= -s -t html -V lang=en --embed-resources --mathml

all: lecture2

lecture2: lecture2.tex fig2_1.tikz
	pdflatex fig2_1.tikz
	pdf2svg fig2_1.pdf fig2_1.svg 
	pandoc $(OPTIONS) lecture2.tex -o lecture2.html
#latexmk -shell-escape lecture2.tex

clean:
	$(RM) *.log *.aux *.pdf

realclean: clean
	$(RM) *.svg *.html




