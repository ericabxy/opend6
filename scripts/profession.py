#!/usr/bin/env python
import os
import sys

from bs4 import BeautifulSoup
from markdown import markdown

template = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
</head>
<body vocab="https://schema.org/" typeof="Occupation">

{content}

</body>
</html>'''

def set_description(soup):
    for ptag in soup.find_all('p'):
        if not ptag.strong:
            continue
        if ptag.strong.string == 'Role:':
            ptag['property'] = 'description'

def set_name(soup):
    if soup.h2:
        soup.h2['property'] = 'name'
        return soup.h2

def set_skills(soup):
    for ptag in soup.find_all('p'):
        if not ptag.strong:
            continue
        if ptag.strong.string == 'Usual Skills:':
            ptag['property'] = 'skills'

def main():
    with open(sys.argv[1]) as file:
        src = file.read()
    html = markdown(src)
    soup = BeautifulSoup(html, 'html.parser')
    title = set_name(soup)
    set_skills(soup)
    set_description(soup)
    content = soup
    print(template.format(title = title, content = content))

if __name__ == '__main__':
    if len(sys.argv) > 0:
        main()
