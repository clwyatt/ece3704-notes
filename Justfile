
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
  cd index && make clean && cd ..;

render: build-all
  rm -rf docs/*
  for dir in `find ./ -name "lecture*" -type d -print`; do \
    cp ${dir}/${dir}.html docs; \
  done
  cd index && make && cd ..;
  cp index/index.html docs

deploy: render
  git add docs
  git commit -m "publish site"
  git push

