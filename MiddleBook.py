

class MiddleBook:
    _bookid = ''
    _bookname = ''
    _author = ''
    _pages = ''
    _collecttime = ''
    _version = ''
    _major = ''
    _discipline = ''
    _isbn = ''
    _booklanguage = ''
    _publisher = ''
    _status = ''
    _abstract = ''
    _stack = ''
    _shelf = ''
    _floor = ''
    _bookvalue = ''
    #定义set方法
    def set_bookid(self,bookid):
        self._bookid = bookid
    def set_bookname(self,bookname):
        self._bookname = bookname
    def set_author(self,author):
        self._author = author
    def set_pages(self,pages):
        self._pages = pages
    def set_collecttime(self,collecttime):
        self._collecttime = collecttime
    def set_version(self,version):
        self._version = version
    def set_major(self,major):
        self._major = major
    def set_discipline(self,discipline):
        self._discipline = discipline
    def set_isbn(self,isbn):
        self._isbn = isbn
    def set_booklanguage(self,language):
        self._booklanguage = language
    def set_publisher(self,publisher):
        self._publisher = publisher
    def set_status(self,status):
        self._status = status
    def set_abstract(self,abstract):
        self._abstract = abstract
    def set_stack(self,stack):
        self._stack = stack
    def set_shelf(self,shelf):
        self._shelf = shelf
    def set_floor(self,floor):
        self._floor = float
    def set_bookvalue(self,bookvalue):
        self._bookvalue = bookvalue


    #get
    def get_bookid(self):
        return self._bookid
    def get_bookname(self):
        return self._bookname
    def get_author(self):
        return self._author
    def get_pages(self):
        return self._pages
    def get_collecttime(self):
        return self._collecttime
    def get_version(self):
        return self._version
    def get_major(self):
        return self._major
    def get_discipline(self):
        return self._discipline
    def get_isbn(self):
        return self._isbn
    def get_booklanguage(self):
        return self._booklanguage
    def get_publisher(self):
        return self._publisher
    def get_status(self):
        return self._status
    def get_abstract(self):
        return self._abstract
    def get_stack(self):
        return self._stack
    def get_shelf(self):
        return self._shelf
    def get_floor(self):
        return self._floor
    def get_bookvalue(self):
        return self._bookvalue

    #将上面不为空的属性转换成字典
    def BookToDict(self):
        #拼接成Dict函数
        #例：{'bookid': '100014', 'author': '韩强军'}
        Seq = []
        Val = []
        if self._bookid != '':
            Seq.append('bookid')
            Val.append(self._bookid)
        if self._bookname != '':
            Seq.append('bookname')
            Val.append(self._bookname)
        if self._author != '':
            Seq.append('author')
            Val.append(self._author)
        if self._pages != '':
            Seq.append('pages')
            Val.append(self._pages)
        if self._collecttime != '':
            Seq.append('collecttime')
            Val.append(self._collecttime)
        if self._version != '':
            Seq.append('version')
            Val.append(self._version)
        if self._major != '':
            Seq.append('major')
            Val.append(self._bookid)
        if self._discipline != '':
            Seq.append('discipline')
            Val.append(self._discipline)
        if self._isbn != '':
            Seq.append('isbn')
            Val.append(self._isbn)
        if self._booklanguage != '':
            Seq.append('booklanguage')
            Val.append(self._booklanguage)
        if self._publisher != '':
            Seq.append('publisher')
            Val.append(self._publisher)
        if self._status != '':
            Seq.append('status')
            Val.append(self._status)
        if self._abstract != '':
            Seq.append('abstract')
            Val.append(self._abstract)
        if self._stack != '':
            Seq.append('stack')
            Val.append(self._stack)
        if self._shelf != '':
            Seq.append('shelf')
            Val.append(self._shelf)
        if self._floor != '':
            Seq.append('floor')
            Val.append(self._floor)
        if self._bookvalue != '':
            Seq.append('bookvalue')
            Val.append(self._bookvalue)

        Dict = dict(zip(Seq,Val))
        return Dict

    #将所有属性转换成列表形式，便于插入
    def BookToList(self):
        List = [self._bookid,self._bookname,self._author,self._pages,self._collecttime,self._version,self._major,self._discipline,self._isbn,self._booklanguage,self._publisher,self._status,self._abstract,self._stack,self._shelf,self._floor,self._bookvalue]
        return List

obj = MiddleBook()
obj.set_bookname('数据库')
obj.set_author('崔晓辉')
print(obj.BookToDict())

# print(obj.BookToList())


