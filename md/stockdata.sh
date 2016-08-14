#!/bin/bash

SYMBOL="001979.sz"
OUTFILE=st.${SYMBOL}.data
wget "http://table.finance.yahoo.com/table.csv?s=${SYMBOL}" -O $OUTFILE
if [ ! -s $OUTFILE ]; then
    rm $OUTFILE
fi
