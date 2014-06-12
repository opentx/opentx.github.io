import os
f = open('_data/icons-taranis.yml', 'w')
for file in os.listdir("assets/images/icons-taranis"):
  s = '- name: "{}"'.format(file)
  print s
  f.write(s) 
  f.write('\n') 

f = open('_data/screens-taranis.yml', 'w')
for file in os.listdir("assets/images/screens-taranis"):
  s = '- name: "{}"'.format(file)
  print s
  f.write(s) 
  f.write('\n') 

f = open('_data/screens-9x.yml', 'w')
for file in os.listdir("assets/images/screens-9x"):
  s = '- name: "{}"'.format(file)
  print s
  f.write(s) 
  f.write('\n') 
  
