## Library for parsing emails and urls from strings.

To parse some text use `messageparse.urls` or/and `messageparse.emails` which parses emails and urls respectivly. It will only find urls and emails which has a known TLD; meaning example.com will match but example.ujh will not.

### Example:

```
from messageparse import urls, emails

message = """Hi!
Please try example.com/one.html, test.com or test.com/a/?b=1.
Or email me john@example.com! Bye.
"""

# This will only parse for urls, emails will be left alone.
parsed_message = urls(message)

print(parsed_message)
>>> Hi!
>>> Please try <example.com/one.html>, <test.com> or <test.com/a/?b=1>.
>>> Or email me john@example.com! Bye.

# Now parse for emails, urls will be left alone.
parsed_message = emails(parsed_message)

print(parsed_message)
>>> Hi!
>>> Please try <example.com/one.html>, <test.com> or <test.com/a/?b=1>.
>>> Or email me <john@example.com>! Bye.
```

### Custom marker function

By default it will surround all urls and emails with `<>`. But you can also supply your own marker function to both `urls()` and `emails()`.

Example:

```
def marker(parsed, original):
    return u'<a href="{}">{}</a>'.format(a, b)

parsed_message = urls('Is this the website: example.com?', marker)
print(parsed_message)
# Is this the website: <a href="http://example.com">example.com</a>?
```

### Contributing

There is a makefile setup:

- `$ make install` - installs all requirements.
- `$ make test` - runs all tests under coverage
- `$ make clean` - cleans caches/.pyc etc.

There is also a script for updating the list with known TLDs.

- `make update_tlds`

This will update the `messageparse/tlds.py` file with the latest list.

### LICENCE

TODO
