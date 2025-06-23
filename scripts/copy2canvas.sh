#!/bin/sh

if [ "$#" -ne 1 ]; then
  echo "Error: This script requires exactly one argument." >&2
  echo "Usage: $0 <argument>" >&2
  exit 1
fi

pandoc -t html --mathml --shift-heading-level-by=1 "$1" | xclip -selection clipboard

