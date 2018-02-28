#!/usr/bin/env python

import sys
import re
import fileinput

def main():
    pats = []
    for line in fileinput.input():
        line = line.strip()
        if line.startswith('||'):
            pat = line[2:].split('/')[0]
            pats += [pat, '*.' + pat]
        elif line.startswith('|http'):
            pats += [line.split('/')[2]]
        elif line.startswith('.'):
            pats += ['*' + line.split('/')[0]]
        elif re.match('^[0-9a-z_\-\.]+$', line):
            if '.' not in line:
                continue
            pats += [line]
        else:
            pass
    pats = sorted(set(pats))
    print '[SwitchyOmega Conditions]\n' + '\n'.join(pats)

if __name__ == '__main__':
    main()

