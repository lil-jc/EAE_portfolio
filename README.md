# EAE_portfolio

(bash script is used to write code.html)

#!/usr/bin/env bash

{ echo "<h1>files</h1><p>"
for l in $(find); do
    fname=$(basename $l)
    [[ $(echo $fname | cut -c1) == '.' ]] && continue
    [[ $(echo $fname | grep '\.' | wc -l) == 0 ]] && continue
    echo "$(dirname $l)/<a href='$l'>$fname</a></br>"
done
echo "</p>"
} > index.html
