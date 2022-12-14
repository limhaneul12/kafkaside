from seleniumUtil import GoogleUtilityDriver
from bs4 import BeautifulSoup
import collections


if not hasattr(collections, 'Callable'):
    collections.Callable = collections.abc.Callable

tlc_url = GoogleUtilityDriver().page()
bs = BeautifulSoup(tlc_url, "html.parser")

