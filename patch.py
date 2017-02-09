#!/usr/bin/env python3

if input('This patch only for version 1.6.1! Continue? [y]/n: ') == 'n':
    exit(0)

fbcore_diff = {'fb_interpret': 'isc_interprete',
               '512, ': '',
               'isc_info_firebird_version': 'isc_info_version'}
ibase_diff = {'fbclient.dll': 'gds32.dll',
              'Firebird Project\Firebird Server\Instances': 'Embarcadero\InterBase\Servers',
              'DefaultInstance': 'RootDirectory',
              "'fbclient'": "'gdb'",
              'libfbclient': 'libgds',
              'self.fb_interpret': '#self.fb_interpret'}

with open('fbcore.py', 'r') as f:
    fbcore = f.readlines()
with open('ibase.py', 'r') as f:
    ibase = f.readlines()

for i in fbcore_diff.keys():
    fbcore = [line.replace(i, fbcore_diff[i]) for line in fbcore]
for i in ibase_diff.keys():
    ibase = [line.replace(i, ibase_diff[i]) for line in ibase]

with open('fbcore.py', 'w') as f:
    f.writelines(fbcore)
with open('ibase.py', 'w') as f:
    f.writelines(ibase)

print('Success!')
