class Recommand(object):
    bookname = ''
    author = ''
    publisher = ''
    version = ''
    recomreason = ''
    statue = ''

    def setbookname(self, bookname):
        self.bookname = bookname

    def setauthor(self, author):
        self.author = author

    def setpublisher(self, publisher):
        self.publisher = publisher

    def setversion(self, version):
        self.version = version

    def setrecomreason(self, recomreason):
        self.recomreason = recomreason

    def setstatue(self, statue):
        self.statue = statue

    def getbookname(self):
        return self.bookname

    def getauthor(self):
        return self.author

    def getpublisher(self):
        return self.publisher

    def getversion(self):
        return self.version

    def getrecomreason(self):
        return self.recomreason

    def getstatue(self):
        return self.statue
