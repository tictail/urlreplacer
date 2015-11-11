# -*- coding: utf-8 -*-

from messageparse import urls
from messageparse.tlds import TLDs


def test_parse_multiple():
    text = u'\n'.join([
        u'abc.test2.com/yes/fil.html',
        u'https://www.google.com, http://abc.se or håkan.com/hej',
        u'http://foo.bar/?q=Test%20URL-encoded%20stuff',
        u'example.com/foo/?bar=baz&inga=42&quux'
    ])

    parsed_text = urls(text)

    assert parsed_text.split('\n') == [
        u'<http://abc.test2.com/yes/fil.html>',
        u'<https://www.google.com>, <http://abc.se> or <http://håkan.com/hej>',
        u'<http://foo.bar/?q=Test%20URL-encoded%20stuff>',
        u'<http://example.com/foo/?bar=baz&inga=42&quux>'
    ]


def test_add_http():
    assert urls('example.com/test.html') == '<http://example.com/test.html>'


def test_keep_http():
    assert urls('http://example.com') == '<http://example.com>'
    assert urls('https://example.com') == '<https://example.com>'


def test_must_start_with_word_character():
    assert urls('.example.com') == '.example.com'


def test_different_marker_func():
    assert urls(
        'example.com',
        lambda a, b: u'<{}|{}>'.format(a, b)
    ) == '<http://example.com|example.com>'

    assert urls(
        'https://example.com',
        lambda a, b: u'<{}|{}>'.format(a, b)
    ) == '<https://example.com|https://example.com>'


def test_querystring():
    assert urls('example.com/test?a=b&g=1') == '<http://example.com/test?a=b&g=1>'


def test_unicode():
    assert urls(u'example.com/åäö/') == u'<http://example.com/åäö/>'
    assert urls(u'кто.рф') == u'<http://кто.рф>'


def test_exclude_punctuation():
    assert urls('example.com/test.html?') == '<http://example.com/test.html>?'
    assert urls('example.com/test.html.') == '<http://example.com/test.html>.'
    assert urls('example.com/test.html,') == '<http://example.com/test.html>,'
    assert urls('example.com/test.html!') == '<http://example.com/test.html>!'


def test_co_uk():
    assert urls('example.co.uk') == '<http://example.co.uk>'
    assert urls('example.co.uk/test.html?y=1') == '<http://example.co.uk/test.html?y=1>'


def test_not_known_tlds():
    assert urls('example.adf') == 'example.adf'


def test_tlds():
    for tld in TLDs():
        assert urls(u'example.{}'.format(tld)) == u'<http://example.{}>'.format(tld)


def test_email_vs_url():
    assert urls('example.com') == '<http://example.com>'
    assert urls('test@example.com') == 'test@example.com'


def test_whole_message():
    text = u"""Hey!

Here is the address: test.com which should give
you what you want,
there is also abc.test2.com/yes/fil.html and test3.co.uk if you need.

We can also try https://www.google.com, http://abc.se or håkan.com/hej?
Another option is Gootle.com?q=test or example.com/foo/?bar=baz&inga=42&quux!
"""

    new_text = urls(text)

    expected_text = u"""Hey!

Here is the address: <http://test.com> which should give
you what you want,
there is also <http://abc.test2.com/yes/fil.html> and <http://test3.co.uk> if you need.

We can also try <https://www.google.com>, <http://abc.se> or <http://håkan.com/hej>?
Another option is <http://Gootle.com?q=test> or <http://example.com/foo/?bar=baz&inga=42&quux>!
"""

    assert new_text == expected_text
