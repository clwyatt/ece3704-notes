# build html from md file

# set final output file
TARGET=about.html

CSS=../style/style.css
HEADER=../style/header.html
FOOTER=../style/footer.html

OPTIONS= -s -t html --css=$(CSS) --include-before $(HEADER) --include-after $(FOOTER) -V lang=en --embed-resources --mathml

.SECONDARY: # prevent removal of intermediate files

all: $(TARGET)

%.html: %.md $(CSS) $(HEADER) $(FOOTER)
	pandoc $(OPTIONS) $< -o $@

view: $(TARGET)
	open $<

clean:
	$(RM) $(TARGET)




