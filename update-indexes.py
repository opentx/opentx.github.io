import os

print 'Updating icons-taranis' 
f = open('_data/icons-taranis.yml', 'w')
l = os.listdir("assets/images/icons-taranis")
l.sort()
for file in l:
  s = '- name: "{}"'.format(file)
  print s
  f.write(s) 
  f.write('\n') 

print 'Updating screens-taranis' 
f = open('_data/screens-taranis.yml', 'w')
l = os.listdir("assets/images/screens-taranis")
l.sort()
for file in l:
  s = '- name: "{}"'.format(file)
  print s
  f.write(s) 
  f.write('\n') 

print 'Updating screens-9x' 
f = open('_data/screens-9x.yml', 'w')
l = os.listdir("assets/images/screens-9x")
l.sort()
for file in l:
  s = '- name: "{}"'.format(file)
  print s
  f.write(s) 
  f.write('\n') 
  
