
status:
   git status . -- ':!docs'

build target:
  @echo 'Building {{target}}…'
  cd {{target}} && make

build-all:
  for dir in `find ./ -name "lecture*" -type d -print`; do \
    cd $dir && make && cd ..; \
  done

clean:
  for dir in `find ./ -name "lecture*" -type d -print`; do \
    cd $dir && make realclean && cd ..; \
  done
  cd about && make clean && cd ..;
  cd index && make clean && cd ..;

render: build-all
  rm -rf docs/*
  cp style/style.css docs
  for dir in `find ./ -name "lecture*" -type d -print`; do \
    cp ${dir}/${dir}.html docs; \
  done
  cd about && make && cd ..;
  cp about/about.html docs
  cd index && make && cd ..;
  cp index/index.html docs

preview: render
   cd docs && python3 -m http.server 8000
   open http://0.0.0.0:8000

# Note: this may result in source out of sync with the site
# Check that `just status` shows no desired modifications before running
deploy: render
  git add docs
  git commit -m "publish site"
  git push

