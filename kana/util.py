#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re
import romkan

K2H_DICT = {
    u'アー': u'ああ', u'イー': u'いい', u'ウー': u'うう', u'エー': u'ええ', u'オー': u'おう',
    u'カー': u'かあ', u'ガー': u'があ', u'キー': u'きい', u'ギー': u'ぎい', u'クー': u'くう',
    u'グー': u'ぐう', u'ケー': u'けえ', u'ゲー': u'げえ', u'コー': u'こう', u'ゴー': u'ごう',
    u'サー': u'さあ', u'ザー': u'ざあ', u'シー': u'しい', u'ジー': u'じい', u'スー': u'すう',
    u'ズー': u'ずう', u'セー': u'せえ', u'ゼー': u'ぜえ', u'ソー': u'そう', u'ゾー': u'ぞう',
    u'ター': u'たあ', u'ダー': u'だあ', u'チー': u'ちい', u'ヂー': u'ぢい', u'ツー': u'つう',
    u'ヅー': u'づう', u'テー': u'てえ', u'デー': u'でえ', u'トー': u'とう', u'ドー': u'どう',
    u'ナー': u'なあ', u'ニー': u'にい', u'ヌー': u'ぬう', u'ネー': u'ねえ', u'ノー': u'のう',
    u'ハー': u'はあ', u'バー': u'ばあ', u'パー': u'ぱあ', u'ヒー': u'ひい', u'ビー': u'びい',
    u'ピー': u'ぴい', u'フー': u'ふう', u'ブー': u'ぶう', u'プー': u'ぷう', u'ヘー': u'へえ',
    u'ベー': u'べえ', u'ペー': u'ぺえ', u'ホー': u'ほう', u'ボー': u'ぼう', u'ポー': u'ぽう',
    u'マー': u'まあ', u'ミー': u'みい', u'ムー': u'むう', u'メー': u'めえ', u'モー': u'もう',
    u'ヤー': u'やあ', u'ユー': u'ゆう', u'ヨー': u'よう', u'ラー': u'らあ', u'リー': u'りい',
    u'ルー': u'るう', u'レー': u'れえ', u'ロー': u'ろう', u'ワー': u'わあ', u'ヰー': u'ゐい',
    u'ヱー': u'ゑえ', u'ァー': u'ぁあ', u'ィー': u'ぃい', u'ゥー': u'ぅう', u'ェー': u'ぇえ',
    u'ォー': u'ぉう', u'ャー': u'ゃあ', u'ュー': u'ゅう', u'ョー': u'ょう',
}
H2K_DICT = dict((v,k) for k, v in K2H_DICT.iteritems())
H2K_PAT = re.compile("|".join(sorted(H2K_DICT.keys())) )
K2H_PAT = re.compile("|".join(sorted(K2H_DICT.keys())) )

IS_JAPANESE_RE = re.compile(u'[\u4E00-\u9FBF\u3040-\u309F\u30A0-\u30FF]',
        re.UNICODE)

def is_japanese(string):
    """Check if a string contains any Japanese character"""
    if IS_JAPANESE_RE.match(string):
        return True
    else:
        return False

def h2k(char):
    """Convert a hiragana character to katakana."""
    if ord(char) > 0x3040 and ord(char) < 0x3097:
        return unichr(ord(char) + 0x60)
    else:
        return char

def k2h(char):
    """Convert a katakana character to hiragana."""
    if ord(char) > 0x30A0 and ord(char) < 0x30F7:
        return unichr(ord(char) - 0x60)
    else:
        return char

def hiragana_to_katakana(word, katakana_long_vowels=False):
    """Convert all hiragana in a string into katakana. """
    if katakana_long_vowels:
        word = H2K_PAT.sub(lambda x: H2K_DICT[x.group(0)], word)
    word = u''.join([h2k(c) for c in word])
    return word

def katakana_to_hiragana(word):
    """Convert all katakana in a string into hiragana. """
    word = K2H_PAT.sub(lambda x: K2H_DICT[x.group(0)], word)
    word = u''.join([k2h(c) for c in word])
    return word

def romaji_to_katakana(word):
    """Convert a word from romaji to katakana. """
    return romkan.to_kana(word)

def romaji_to_hiragana(word):
    """Convert a word from romaji to hiragana. """
    katakana = romaji_to_katakana(word)
    return katakana_to_hiragana(katakana)

def to_romaji(word):
    """Convert a Japanese word in hiragana or katakana to romaji. """
    return romkan.to_roma(hiragana_to_katakana(word))

