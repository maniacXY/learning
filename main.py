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

#for path in mapping.getMDFiles():
#   conv.MDtoHTML(path)

#indexer.compose()


dirs =  markdown.getDirs()
files = markdown.getMDFiles()
# print(files[0])
# pprint(markdown.readFile(files[0]))

link = "tEASDADSFestwort hallo welt"


#print(markdown.replaceHash("# Hallo Welt oder nicht tesat \n"))
print()
#pprint(markdown.inhaltsangabeTopButtons("./testfile.md"))
pprint(markdown.inhaltsangabeTopButtons("./testfile.md"))