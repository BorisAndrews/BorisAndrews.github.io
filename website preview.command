#!/bin/zsh
#
# Double-click in Finder to preview the website at http://localhost:4000.
# Opens the browser once the site is up; close this window (or Ctrl-C) to stop.
# If a preview is already running, it just opens the browser.

URL=http://localhost:4000/
HERE="$(cd "$(dirname "$0")" && pwd)"

if curl -s -o /dev/null "$URL"; then
    echo "Preview already running: opening $URL"
    open "$URL"
    exit 0
fi

(
    for i in {1..90}; do
        sleep 2
        if curl -s -o /dev/null "$URL"; then open "$URL"; break; fi
    done
) &

exec "$HERE/../../../Software/site-check" --serve
