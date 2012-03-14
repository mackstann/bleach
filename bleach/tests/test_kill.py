import html5lib
from nose.tools import eq_

import bleach


def test_kill_tag():
    html = '<script>foo <a href="bar">blah</a><br /></script>'
    eq_('', bleach.clean(html, kill_tags=['script']))


def test_do_not_kill_nonkilled_tags():
    html = '<script>foo <a href="bar">blah</a><br /></script>'
    eq_('&lt;script&gt;foo <a href="bar">blah</a>&lt;br/&gt;&lt;/script&gt;', bleach.clean(html, kill_tags=['style']))


def test_do_not_kill_allowed_tags():
    html = '<script>foo <a href="bar">blah</a><br /></script>'
    eq_('<script>foo <a href="bar">blah</a><br /></script>', bleach.clean(html, tags=['script', 'a', 'br'], kill_tags=['style']))


def test_kill_tag_inside_others():
    html = '<div><h1>hi</h1><p><script>foo <a href="bar">blah</a><br /></script></p></div>'
    eq_('<div><h1>hi</h1><p></p></div>', bleach.clean(html, tags=['div', 'h1', 'p'], kill_tags=['script']))


def test_kill_even_allowed_tags_inside_killed_tag():
    html = '<script>foo <a href="bar">blah</a><br /></script>'
    eq_('', bleach.clean(html, tags=['a', 'br'], kill_tags=['script']))
