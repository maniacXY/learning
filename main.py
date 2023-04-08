#from programm.zzzFiles import *
from programm.Mapping import *
from programm.Converter import *
from programm.Indexer import *

mapping = Mapper()
conv = Converter()
indexer = Indexer()
#mapping.printDict()


# print(mapping.getMDFiles())


# print(mapping.getMDFiles() == mapping.getHTMLFiles())

# print(mapping.getHTMLFiles())
# print(mapping.getMDFiles())
folder = mapping.getDirs()
print(folder)
print(mapping.getFolderFiles(folder[-1],"html"))

for path in mapping.getMDFiles():
    conv.MDtoHTML(path)

indexer.compose()
