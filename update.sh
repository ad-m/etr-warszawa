#!/bin/bash
URL="http://ad-m.github.io/etr-warszawa/";
function update_revs {
	rev=$(date +"%Y-%m-%d %T");
	(cat page/head.html; python etr-warszawa-grab.py; cat page/footer.html;) | tee "revs/$rev.html" > "revs/current.html";
	git add "revs/$rev.html" "revs/current.html";
	git commit -m "Added rev $rev" "revs/$rev.html" "revs/current.html";
};
function update_index {
	(cat page/head.html; echo "<ul>";
	find revs -type f | while read line; do 
		echo "<li><a href='$line'>`basename "$line"`</a></li>";
	done;
	echo "</ul>";
	cat page/footer.html;) > "index.html";
	git add "index.html";
	git commit -m "Update index" "index.html";

};
function generate_sitemap {
	echo '<urlset>'
	find revs -type f | while read line; do 
		echo "<url><loc>$URL$line</loc></url>";
	done;
	echo '</urlset>';
}
function update_sitemap {
	generate_sitemap > sitemap.xml;
	git add "sitemap.xml";
	git commit -m "Update sitemap" "sitemap.xml";
};
function update {
	update_revs;
	update_index;
	update_sitemap;
	git push origin;
}
update;
