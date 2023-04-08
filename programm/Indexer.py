from programm.Mapping import Mapper

class Indexer:
    def __init__(self) -> None:
        self.htmlstring =""
        self.mapper = Mapper()

    def __str__(self) -> str:
        return "index.html wird erstellt"
    def compose(self):
        # setting file up
        self.htmlstring = self.ueberschrift()
        for dir in self.mapper.getDirs():
            filelist = []
            for file in self.mapper.getFolderFiles(dir, "html"):
                filelist.append(file)
            self.htmlstring += self.chapter(dir, filelist)
        self.writeFile()
        
    def ueberschrift(self):
        return '<h1 id="alle-seiten">Alle Seiten</h1>'

    def chapter(self, Überschrift:str, Files:list):
        retString = ""
        retString += f'<h2 id="{Überschrift.lower()}">{Überschrift}</h2><ul>'
        for file in Files:
            retString+=f'<li><a href="{Überschrift}{file}">{file}</a></li>'
        retString += '</ul>'
        return retString
    def writeFile(self):
        with open("index.html", "w") as file:
            file.write(self.htmlstring)

if __name__ == "__main__":
    indexer = Indexer()
    indexer.compose()
    print("\nIndexfile wurde geschrieben\n")



