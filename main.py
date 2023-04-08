#from programm.zzzFiles import *
from programm.Mapping import *
from programm.Converter import *
from programm.Indexer import *
from programm.Markdownfinisher import *

from pprint import pprint

mapping = Mapper()
conv = Converter()
indexer = Indexer()
#markdown = MarkdownFinisher("./programm/", "templateHeader", "templateFooter")
markdown = MarkdownFinisher()


#mapping.printDict()


# print(mapping.getMDFiles())


# print(mapping.getMDFiles() == mapping.getHTMLFiles())

# print(mapping.getHTMLFiles())
# print(mapping.getMDFiles())
#folder = mapping.getDirs()
#print(folder)
#print(mapping.getFolderFiles(folder[-1],"html"))
#markdown.inhaltsangabeTopButtons()
for path in mapping.getMDFiles():
    conv.MDtoHTML(path)

indexer.compose()
