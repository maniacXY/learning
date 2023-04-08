#from programm.zzzFiles import *
from programm.Mapping import *
from programm.Converter import *
from programm.Indexer import *
from programm.mdHTMLFinisher import *

from pprint import pprint

mapping = Mapper()
indexer = Indexer("./programm/templateHeader.txt", "<PLACEHOLDER>")
markdown = MarkdownFinisher()

markdown.inhaltsangabeTopButtons()
for path in markdown.getMDFiles():
    markdown.MDtoHTML(path)

# indexer.compose()


html = HTMLFinisher("./programm/", "templateHeader.txt", "templateFooter.txt", "<PLACEHOLDER>")

#pprint(html.__dict__)
html.headerFooterCompose()