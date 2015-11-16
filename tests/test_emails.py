# -*- coding: utf-8 -*-

from urlreplacer import emails
from urlreplacer.tlds import TLDs


def test_different_marker_func():
    assert emails(
        'test@example.com',
        lambda a, b: u'<{}|{}>'.format(a, b)
    ) == '<mailto:test@example.com|test@example.com>'

    assert emails(
        'mailto:test@example.com',
        lambda a, b: u'<{}|{}>'.format(a, b)
    ) == '<mailto:test@example.com|mailto:test@example.com>'


def test_add_mailto():
    assert emails('test@example.com') == '<mailto:test@example.com>'


def test_keep_mailto():
    assert emails('mailto:test@example.com') == '<mailto:test@example.com>'


def test_must_start_with_word_character():
    assert emails('.test@example.com') == '.test@example.com'


def test_unicode():
    assert emails(u'рф@кто.рф') == u'<mailto:рф@кто.рф>'


def test_excludes_after_domain():
    assert emails('test@example.com?') == '<mailto:test@example.com>?'


def test_co_uk():
    assert emails('test@example.co.uk') == '<mailto:test@example.co.uk>'


def test_unknown_tld():
    assert emails('test@example.adf') == 'test@example.adf'


def test_tlds():
    for tld in TLDs():
        assert emails(u'test@example.{}'.format(tld)) == u'<mailto:test@example.{}>'.format(tld)


def test_email_vs_url():
    assert emails('example.com') == 'example.com'
    assert emails('test@example.com') == '<mailto:test@example.com>'


def test_whole_message():
    text = u"""Hey!

Here is the address: test.com which should give
you what you want,
there is also test@example.com and asdf@test3.co.uk if you need.

We can also try mailto:www@google.com, mailto:aa@abc.se or hej@håkan.com?
"""

    new_text = emails(text)

    expected_text = u"""Hey!

Here is the address: test.com which should give
you what you want,
there is also <mailto:test@example.com> and <mailto:asdf@test3.co.uk> if you need.

We can also try <mailto:www@google.com>, <mailto:aa@abc.se> or <mailto:hej@håkan.com>?
"""

    assert new_text == expected_text
