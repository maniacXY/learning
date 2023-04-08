from programm.Files import *
from programm.Mapping import *
from programm.Converter import *

files = GetAllFiles()


#files.mapDirFiles()
##files.notIncluded.printNotIncluded()
#listofObjects = files.FileCollection
#
#
# 
# print("STUFF")



mapping = Mapper()
conv = Converter()
mapping.printDict()


print(mapping.getMDFiles())


print(mapping.getMDFiles() == mapping.getHTMLFiles())

print(mapping.getHTMLFiles())
print(mapping.getMDFiles())

for path in mapping.getMDFiles():
    conv.MDtoHTML(path)


