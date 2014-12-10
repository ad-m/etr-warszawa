#!/bin/sh
rev=$(date +"%Y-%M-%d %H:%m");
python etr-warszawa-grab.py >> "revs/$rev.html";
ln "revs/$rev.html" "revs/current.html";

git add "revs/$rev.html" "revs/current.html";
git commit -m "Added rev $rev" "revs/$rev.html" "revs/current.html";
git push origin;
