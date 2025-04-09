# NAME

Lingua::LO::NLP - Various Lao text processing functions

# SYNOPSIS

```python
from lib.Lingua.LO.NLP import LaoNLP

lao = LaoNLP()

syllables = lao.split_to_syllables("ສະບາຍດີ")  # ['ສະ', 'ບາຍ', 'ດີ']
print(syllables)

for syl in syllables:
    analysis = lao.analyze_syllable(syl)
    print(f"{analysis.syllable}: {analysis.tone}")
    # ສະ: TONE_HIGH_STOP
    # ບາຍ: TONE_LOW
    # ດີ: TONE_LOW

print(lao.romanize("ສະບາຍດີ", variant='PCGN', hyphen="\u2010"))  # sa‐bay‐di
print(lao.romanize("ສະບາຍດີ", variant='IPA'))  # saʔ baːj diː
```

# DESCRIPTION

This module provides various functions for processing Lao text. Currently it can

- split Lao text (usually written without blanks between words) into syllables
- analyze syllables with regards to core and end consonants, vowels, tone and
other properties
- romanize Lao text according to the PCGN standard or to IPA (experimental)

These functions are basically just shortcuts to the functionality of some
specialized modules: `lib.Lingua.LO.NLP.Syllabify`, `lib.Lingua.LO.NLP.Analyze`, and `lib.Lingua.LO.NLP.Romanize`. If
you need only one of them, you can shave off a little overhead by using those
directly.

# METHODS

## new

```python
new(option=value, ...)
```

The object constructor currently does nothing; there are no options. However,
it is likely that there will be in future versions, therefore it is highly
recommended to call methods as object methods so your code won't break when I
introduce them.

## split\_to\_syllables

```python
syllables = object.split_to_syllables(text, **options)
```

Split Lao text into its syllables using a regexp modelled after PHISSAMAY,
DALALOY and DURRANI: _Syllabification of Lao Script for Line Breaking_. Takes
as its only mandatory parameter a character string to split and optionally a
number of named options; see `lib.Lingua.LO.NLP.Syllabify` for those.
Returns a list of syllables.

## analyze\_syllable

```python
classified = object.analyze_syllable(syllable, **options)
```

Returns a `lib.Lingua.LO.NLP.Analyze` object that allows you to query
various syllable properties such as core consonant, tone mark, vowel length and
tone. See there for details.

## romanize

```python
object.romanize(lao, **options)
```

Returns a romanized version of the text passed in as `lao`. See
`lib.Lingua.LO.NLP.Romanize` for options. If you don't pass in _any_
options, the default is `variant='PCGN'`.

# SEE ALSO

`lib.Lingua.LO.Romanize` is the module that inspired this one. It has some
issues with ambiguous syllable boundaries as in "ໃນວົງ" though.

# AUTHOR

Matthias Bethke, <matthias@towiski.de>

# COPYRIGHT AND LICENSE

Copyright (C) 2016 by Matthias Bethke

This library is free software; you can redistribute it and/or modify it under
the same terms as Perl itself, either Perl version 5.14.2 or, at your option,
any later version of Perl 5 you may have available. Significant portions of the
code are (C) PostgreSQL Global Development Group and The Regents of the
University of California. All modified versions must retain the file COPYRIGHT
included in the distribution.
