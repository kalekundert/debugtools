#!/usr/bin/env python

from debugtools import p, pp, pv

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
    assert_phrases_in_stdout(capsys, "'a': 1", "'b': 2")
