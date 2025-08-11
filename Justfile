
status:
   git status . -- ':!docs'

build:
   make
   
clean:
   make realclean
   
# Note: this may result in source out of sync with the site
# Check that `just status` shows no desired modifications before running
deploy: build
  git add docs
  git commit -m "publish site"
  git push

