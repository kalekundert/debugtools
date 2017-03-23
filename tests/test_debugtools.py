#!/usr/bin/env python

from debugtools import p, pp, pv
from textwrap import dedent

def assert_phrases_in_stdout(capsys, *phrases):
    out, err = capsys.readouterr()
    for x in phrases:
        assert x in out

def test_print(capsys):
    p()
    assert_phrases_in_stdout(capsys, 'test_print')
    p('hello')
    assert_phrases_in_stdout(capsys, 'test_print', 'hello')

def test_pprint(capsys):
    pp(dict(a=1, b=2))
    assert_phrases_in_stdout(capsys, "'a': 1", "'b': 2")

def test_pprint_vars(capsys):
    a = 1
    b = 2
    pv()
    assert_phrases_in_stdout(capsys, "a = 1", "b = 2")

def test_anglicize(capsys):
    p()
    out, err = capsys.readouterr()
    assert out == dedent('''
        DEBUG: test_debugtools.py:28, test_debugtools.test_anglicize().
    ''').lstrip()

def test_grouch(capsys):
    a = 0
    b = 'b'
    p('hey now!', a, b)
    out, err = capsys.readouterr()
    assert out == dedent('''
        DEBUG: test_debugtools.py:37, test_debugtools.test_grouch():
            hey now! 0 b
    ''').lstrip()

def test_salver(capsys):
    a = 0
    b = 'b'
    c = [a, b]
    d = {a, b}
    e = {a:b}
    pp('hey now!', a, b, c, d, e)
    out, err = capsys.readouterr()
    assert out == dedent('''
        DEBUG: test_debugtools.py:50, test_debugtools.test_salver():
            'hey now!'
            0
            'b'
            [0, 'b']
            {0, 'b'}
            {0: 'b'}
    ''').lstrip()

def test_daiquiri(capsys):
    a = 0
    b = 'b'
    c = [a, b]
    d = {a, b}
    e = {a:b}
    pp(s='hey now!', a=a, b=b, c=c, d=d, e=e)
    out, err = capsys.readouterr()
    assert out == dedent('''
        DEBUG: test_debugtools.py:68, test_debugtools.test_daiquiri():
            a = 0
            b = 'b'
            c = [0, 'b']
            d = {0, 'b'}
            e = {0: 'b'}
            s = 'hey now!'
    ''').lstrip()

def test_update(capsys):
    a = 0
    b = 'b'
    c = [a, b]
    d = {a, b}
    e = {a:b}
    pv()
    out, err = capsys.readouterr()
    out = '\n'.join(l for l in out.split('\n') if 'capsys' not in l)
    assert out == dedent('''
        DEBUG: test_debugtools.py:86, test_debugtools.test_update():
            a = 0
            b = 'b'
            c = [0, 'b']
            d = {0, 'b'}
            e = {0: 'b'}
    ''').lstrip()

def test_shear(capsys):
    a = 0
    b = 'b'
    c = [a, b]
    d = {a, b}
    e = {a:b}
    pv(a, b, c, d, e)
    out, err = capsys.readouterr()
    assert out == dedent('''
        DEBUG: test_debugtools.py:104, test_debugtools.test_shear():
            a = 0
            b = 'b'
            c = [0, 'b']
            d = {0, 'b'}
            e = {0: 'b'}
    ''').lstrip()
