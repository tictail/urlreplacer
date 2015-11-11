# -*- coding: utf-8 -*-

from urlparse import urlsplit

# Using pypi/regex instead because of http://bugs.python.org/issue1693050
import regex

from .tlds import TLDs

regex = regex.compile(
    ur'(?<=^|\s)(http(?:s)?://)?([^/\s@]+)\.({})(\b)(\S*?)(?=$|\s|[,!\.\?]([\s]|$))'.format(
        ur'|'.join(TLDs())
    ),
    regex.IGNORECASE | regex.UNICODE | regex.MULTILINE
)


def make_replacer(use_labels):

    def replacer(matchobj):
        url = matchobj.group(0)
        parts = list(urlsplit(url))

        # Add the ? before the query
        if parts[3]:
            parts[3] = u'?' + parts[3]

        label = u''

        if use_labels:
            label = u'|' + url

        url = u'<{}://{}{}>'.format(
            parts[0] or 'http',
            u''.join(parts[1:]),
            label
        )

        return url

    return replacer


def urls(text, use_labels=False):
    replacer = make_replacer(
        use_labels=use_labels
    )

    return regex.sub(replacer, text)
