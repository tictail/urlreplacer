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

The MIT License (MIT)

Copyright (c) [2015] [Tictail]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
