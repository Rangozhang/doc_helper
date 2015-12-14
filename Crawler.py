import os, sys
import argparse
import re
import urllib2 as url

def replace(m_str, frm, to):
    first, second, third = m_str.rpartition(frm)
    return ''.join([first, to])

def getSave(arg):
    http = arg.http
    target = arg.target
    fd = url.urlopen(http)
    items = re.findall('<a href="(.*pdf)">', fd.read())
    for item in items:
        print item
        out_file = open(os.path.join(target, item), 'wb')
        out_file.write(url.urlopen(replace(http.strip(),'handouts.html',item)).read())
        out_file.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s','--http')
    parser.add_argument('-t','--target')
    arg = parser.parse_args()
    getSave(arg)
