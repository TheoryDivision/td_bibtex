#!/bin/python

import os

sort = 'year'

def readentries(f, newline):
  buf = ""
  while True:
    while newline in buf:
        pos = buf.index(newline)
        yield buf[:pos]
        buf = buf[pos + len(newline):]
    chunk = f.read(4096)
    if not chunk:
        yield buf
        break
    buf += chunk

entries = []
with open('../td.bib') as f:
  for entry in readentries(f, '\n\n'):
    entries.append(entry)
# f = open("../td.bib", "r")

e_sort = {}
for e in entries:
    begin = e.find('{', e.find(sort))
    end = e.find('}', e.find(sort))
    key = e[begin + 1 : end]
    if key not in e_sort:
        e_sort[key] = list()
    e_sort[key].append(e)

if not os.path.isdir('split_bib'): os.mkdir('split_bib')
for f in os.listdir('split_bib'):
    os.remove(os.path.join('split_bib', f))

for key in e_sort:
    with open('split_bib/' + key + '.bib', "w") as f:
        for e in e_sort[key]:
            f.write('%s\n\n' % e)

