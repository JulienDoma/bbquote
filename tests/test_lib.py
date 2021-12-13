from requests.api import get
from bbquote.lib import get_quote

def test_len():
    assert len(get_quote()) == 2

def test_list():
    assert type(get_quote()) == tuple