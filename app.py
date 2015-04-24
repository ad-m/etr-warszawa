import os
import subprocess
from itertools import islice, groupby
from flask import Flask, request, render_template, url_for
from flask import safe_join, send_file, current_app
from flask import abort
import gzip
app = Flask(__name__)
directory = 'revs'
per_page = 500


def url_for_other_page(page):
    args = request.args.copy()
    args['page'] = page
    return url_for(request.endpoint, **args)
app.jinja_env.globals['url_for_other_page'] = url_for_other_page


def zgrep(query):
    ps = subprocess.Popen(('find', 'revs/2015', '-type', 'f', '-print0'), stdout=subprocess.PIPE)
    output = subprocess.Popen(('xargs', '-0', 'zgrep', '-i', '-C 20', query), stdin=ps.stdout, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
    row = {}
    for x in output.stdout:
        row['filename'], row['content'] = x.decode('utf-8').split(':', 1)
        yield row


def uncompress_and_send_from_directory(directory, filename, **options):
    filename = safe_join(directory, filename)
    if not os.path.isabs(filename):
        filename = os.path.join(current_app.root_path, filename)
    if not os.path.isfile(filename):
        abort(404)
    options.setdefault('conditional', True)
    print filename
    if filename.endswith('.gz'):
        fp = gzip.GzipFile(filename)
    else:
        fp = open(filename)
    return send_file(fp, **options)

@app.route('/')
def home():
    return render_template('home.html', entries=())


@app.route('/search')
def search():
    query = request.args.get('query') or 'Minister'
    query = query.strip()
    page = request.args.get('page', '1')
    page = int(page) if page.isdigit() else 1
    context = {}
    qs = zgrep(query)
    qs = islice(qs, page*per_page, page*per_page+per_page)
    qs = groupby(qs, lambda x: x['filename'])
    context['query'] = query
    context['entries'] = qs
    context['page'] = page

    return render_template('search.html', **context)


@app.route('/revs/<path:filename>')
def send_foo(filename):
     return uncompress_and_send_from_directory('revs', filename)

if __name__ == "__main__":
    app.run(debug=True)
