import streamlit as st

from bbquote.lib import get_quote

quote, author = get_quote()

f"{quote}, {author} "