#!/bin/sh
pytest . --cov=. --cov-report term-missing
if [ ${ERROR_CODE} == 0 ]; then
    all_badge -c brightgreen -o media/build.svg -f -t 'build' -v success -s flat
else
    all_badge -c red -o media/build.svg -f -t 'build' -v fail -s flat
fi
all_badge -f -cov -s flat -o media/coverage.svg
