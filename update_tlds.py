# -*- coding: utf-8 -*-

import codecs
import urllib2

template = u"""# -*- coding: utf-8 -*-

# Downloaded from: http://data.iana.org/TLD/tlds-alpha-by-domain.txt
# Use `make update_tlds` to update this list.
{}


def TLDs():
    for tld in [
        {}
    ]:
        yield tld
"""


def download():
    response = urllib2.urlopen('http://data.iana.org/TLD/tlds-alpha-by-domain.txt')
    return unicode(response.read(), 'utf-8').split(u'\n')


def build_file(data):
    last_updated = data[0]

    tlds = []

    for line in data[1:]:
        if not line:
            continue

        tld = line.lower().decode('idna')

        tlds.append(u"u'{}',".format(tld))

    return template.format(
        last_updated,
        u'\n        '.join(tlds)
    )


def write_file(new_file):
    with codecs.open('messageparse/tlds.py', 'w', 'utf-8') as outfile:
        outfile.write(new_file)


if __name__ == '__main__':
    data = download()
    new_file = build_file(data)
    write_file(new_file)
