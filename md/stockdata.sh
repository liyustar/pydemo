#!/bin/bash

if [ -z "$1" ]; then
    echo "usage: $0 <stock>"
    exit -1
fi

SYMBOL=$1

OUTFILE=st.${SYMBOL}.csv
wget "http://table.finance.yahoo.com/table.csv?s=${SYMBOL}" -O $OUTFILE
if [ ! -s $OUTFILE ]; then
    rm $OUTFILE
fi
