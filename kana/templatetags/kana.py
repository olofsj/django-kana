from django import template

from ..util import to_romaji, romaji_to_hiragana, romaji_to_katakana
from ..util import is_japanese, hiragana_to_katakana, katakana_to_hiragana

register = template.Library()

@register.filter
def romaji(value):
    return to_romaji(value)

@register.filter
def katakana(value):
    if is_japanese(value):
        return hiragana_to_katakana(value)
    else:
        return romaji_to_katakana(value)

@register.filter
def hiragana(value):
    if is_japanese(value):
        return katakana_to_hiragana(value)
    else:
        return romaji_to_hiragana(value)

