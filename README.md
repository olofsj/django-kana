django-kana
==================

django-kana is a reusable Django helper app that includes
different functions and template tags for handling Japanese
text, such as converting between kana and romaji.

Usage
-----

To use django-kana in your Django project, install it using 
pip like this:

    pip install -e git://github.com/olofsj/django-kana.git#egg=django-kana

Then you need to add `kana` to `INSTALLED_APPS` in `settings.py` in your project.

The bundled utility functions can then be used like so:

    from kana.util import is_japanese, romaji_to_hiragana, hiragana_to_katakana, to_romaji

    romaji = 'nihongodesu'
    print is_japanese(romaji)   # False

    hiragana = romaji_to_hiragana(romaji)
    print hiragana              # にほんごです
    print is_japanese(hiragana) # True

    katakana = hiragana_to_katakana(hiragana)
    print katakana              # ニホンゴデス
    romaji_again = to_romaji(katakana)
    print romaji_again          # nihongodesu


There are also a number of template filters that can be used in your templates.
Here's an example of their usage:

    {% load kana %}
    {{ string_in_japanese|romaji }}
    {{ string_in_romaji|hiragana }}
    {{ string_in_hiragana|katakana }}


Credits
-------

Romaji conversions is based on
[romkan](https://code.google.com/p/mhagiwara/source/browse/trunk/nltk/jpbook/romkan.py)
