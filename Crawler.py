import os, sys
import argparse
import re
import urllib2 as url

def replace(m_str, frm, to):
    first, second, third = m_str.rpartition(frm)
    return ''.join([first, to])

def getSave(http):
    fd = url.urlopen(http)
    items = re.findall('<a href="(.*pdf)">', fd.read())
    for item in items:
        print item
        out_file = open(item, 'wb')
        out_file.write(url.urlopen(replace(http.strip(),'handouts.html',item)).read())
        out_file.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('http')
    arg = parser.parse_args()
    getSave(arg.http)
