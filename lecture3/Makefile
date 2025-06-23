
OPTIONS= -s -t html -V lang=en --embed-resources --mathml

all: lecture3.html

lecture3.html: lecture3.tex
	pandoc $(OPTIONS) lecture3.tex -o lecture3.html

view: lecture3.html
	open lecture3.html

clean:
	$(RM) *.log *.aux *.pdf

realclean: clean
	$(RM) *.svg *.html




