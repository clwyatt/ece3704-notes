# build html from md file

# set final output file
TARGET=index.html

CSS=../style/style.css

OPTIONS= -s -t html --css=$(CSS) -V lang=en --embed-resources --mathml

.SECONDARY: # prevent removal of intermediate files

all: $(TARGET)

%.html: %.md $(CSS)
	pandoc $(OPTIONS) $< -o $@

view: $(TARGET)
	open $<

clean:
	$(RM) $(TARGET)




