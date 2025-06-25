
build target:
  @echo 'Building {{target}}…'
  cd {{target}} && make

build-all:
  for dir in `find ./ -name "lecture*" -type d -print`; do \
    cd $dir && make && cd ..; \
  done

clean-all:
  for dir in `find ./ -name "lecture*" -type d -print`; do \
    cd $dir && make clean && cd ..; \
  done

reset:
  for dir in `find ./ -name "lecture*" -type d -print`; do \
    cd $dir && make realclean && cd ..; \
  done

