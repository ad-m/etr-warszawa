#!/bin/bash
function update_revs {
	rev=$(date +"%Y-%m-%d %T");
	(cat page/head.html; python etr-warszawa-grab.py; cat page/footer.html;) | tee "revs/$rev.html" > "revs/current.html";
	git add "revs/$rev.html" "revs/current.html";
	git commit -m "Added rev $rev" "revs/$rev.html" "revs/current.html";
	git push origin;
};
function update_index {
	(cat page/head.html; 
	find revs -type f | while read line; do 
		echo "<a href='$line'>`basename "$line"`</a>";
	done;
	cat page/footer.html;) > "index.html";
};
function update {
	update_revs;
	update_index;
}
update;
