#!/bin/sh
flake8 djcourses
ERROR_CODE=$?
if [ ${ERROR_CODE} == 0 ]; then
    all_badge -c brightgreen -o media/flake.svg -f -t 'flake' -v success -s flat
else
    all_badge -c red -o media/flake.svg -f -t 'flake' -v fail -s flat
fi