#! /usr/bin/python
# #! python3.4

import os

print('Updating icons-taranis')
f = open('_data/icons-taranis.yml', 'w')
dlist = os.listdir("assets/images/icons-taranis")
dlist.sort()
for dname in dlist:
  s = '- name: "{}"'.format(dname)
  print(s)
  f.write(s)
  f.write('\n')
  s = '  type: title'
  print(s)
  f.write(s)
  f.write('\n')
  flist = os.listdir('assets/images/icons-taranis/{}'.format(dname))
  flist.sort()
  for fname in flist:
    s = '- name: "{}"'.format(fname)
    print(s)
    f.write(s)
    f.write('\n')
    s = '  type: image'
    print(s)
    f.write(s)
    f.write('\n')
    s = '  url: assets/images/icons-taranis/{}/{}'.format(dname, fname)
    print(s)
    f.write(s)
    f.write('\n')

print('Updating screens-taranis')
f = open('_data/screens-taranis.yml', 'w')
l = os.listdir("assets/images/screens-taranis")
l.sort()
for file in l:
  s = '- name: "{}"'.format(file)
  print(s)
  f.write(s)
  f.write('\n')

print('Updating screens-9x')
f = open('_data/screens-9x.yml', 'w')
l = os.listdir("assets/images/screens-9x")
l.sort()
for file in l:
  s = '- name: "{}"'.format(file)
  print(s)
  f.write(s)
  f.write('\n')
