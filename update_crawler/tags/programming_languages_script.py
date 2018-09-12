import requests
import re
from bs4 import BeautifulSoup
from .models import ProgrammingLanguage

page = requests.get("https://en.wikipedia.org/wiki/List_of_programming_languages")


def run_script():

    soup = BeautifulSoup(page.content, 'html.parser')
    anchors = soup.select('div.div-col li a')
    programming_languages = [ProgrammingLanguage(
        code=(re.sub(r'\([^)]*\)', '',
                     anchor.get_text().lower())).strip().replace(' ', '_'),
        description=anchor.get('title') if anchor.get('title') is not None else 'UNKNOWN') for index, anchor in enumerate(anchors)]
    return programming_languages
