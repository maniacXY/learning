import os
from glob import glob

class Indexer:
    def __init__(self) -> None:
        self.htmlstring =""
    def __str__(self) -> str:
        return "index.html wird erstellt"
    def compose(self):
        folder = glob("./*/", recursive=True)
        # setting file up
        self.htmlstring = self.ueberschrift()
        for dir in folder:
            files = os.listdir(f"./{dir}")
            filelist = []
            for file in files:
                if "html" in file[-4:]:
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
    print("\nIndexfile wurde geschrieben")



