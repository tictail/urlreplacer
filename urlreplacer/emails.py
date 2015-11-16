# -*- coding: utf-8 -*-

# Using pypi/regex instead because of http://bugs.python.org/issue1693050
import regex

from .tlds import TLDs

regex = regex.compile(
    ur'(?<=^|\s)\b(mailto:)?([^/\s@]+)@([^/\s@]+)\.({})\b'.format(
        ur'|'.join(TLDs())
    ),
    regex.IGNORECASE | regex.UNICODE | regex.MULTILINE
)


def make_replacer(marker_func):

    def replacer(matchobj):
        email = matchobj.group(0)

        if not matchobj.group(1):
            email = u'mailto:' + email

        return marker_func(email, matchobj.group(0))

    return replacer


def emails(text, marker_func=None):
    if marker_func is None:
        marker_func = lambda a, b: u'<{}>'.format(a)

    replacer = make_replacer(marker_func)

    return regex.sub(replacer, text)
