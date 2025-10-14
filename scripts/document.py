#!/usr/bin/env python
import os
import sys

from markdown import markdown

template = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
</head>
<body>

{content}

</body>
</html>'''

def get_title(path):
    with open(path) as file:
        return file.readline().strip()

def get_content(path):
    with open(path) as file:
        return markdown(
            file.read()
        )

def write_htmldoc(src, dest):
    if os.path.isfile(src):
        with open(dest, 'w') as file:
            file.write(
                template.format(
                    title = get_title(src),
                    content = get_content(src)
                )
            )

if __name__ == '__main__':
    destdir = os.environ['DESTDIR']
    for src in sys.argv[1:]:
        if not os.path.isfile(src):
            continue
        name = os.path.basename(src)
        dest = os.path.join(destdir, name + '.html')
        write_htmldoc(src, dest)
