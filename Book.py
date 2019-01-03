class Book:
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

    # 定义set方法
    def set_bookid(self, bookid):
        self._bookid = bookid

    def set_bookname(self, bookname):
        self._bookname = bookname

    def set_author(self, author):
        self._author = author

    def set_pages(self, pages):
        self._pages = pages

    def set_collecttime(self, collecttime):
        self._collecttime = collecttime

    def set_version(self, version):
        self._version = version

    def set_major(self, major):
        self._major = major

    def set_discipline(self, discipline):
        self._discipline = discipline

    def set_isbn(self, isbn):
        self._isbn = isbn

    def set_booklanguage(self, language):
        self._booklanguage = language

    def set_publisher(self, publisher):
        self._publisher = publisher

    def set_status(self, status):
        self._status = status

    def set_abstract(self, abstract):
        self._abstract = abstract

    def set_stack(self, stack):
        self._stack = stack

    def set_shelf(self, shelf):
        self._shelf = shelf

    def set_floor(self, floor):
        self._floor = floor

    def set_bookvalue(self, bookvalue):
        self._bookvalue = bookvalue

    # get
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

