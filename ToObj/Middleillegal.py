

class Middleillegal:
    _illegalid = ''
    _userid = ''
    _bookid = ''
    _amount = ''
    _isprocessed = ''
    _illegaldate = ''
    _illegaltype = ''
    #定义set方法
    def set_illegalid(self,illegalid):
        self._illegalid = illegalid
    def set_userid(self,userid):
        self._userid = userid
    def set_bookid(self,bookid):
        self._bookid = bookid
    def set_amount(self,amount):
        self._amount = amount
    def set_isprocessed(self,isprocessed):
        self._isprocessed = isprocessed
    def set_illegaldate(self,illegaldate):
        self._illegaldate = illegaldate
    def set_illegaltype(self,illegaltype):
        self._illegaltype = illegaltype

    #get
    def get_illegalid(self):
        return self._illegalid
    def get_userid(self):
        return self._userid
    def get_bookid(self):
        return self._bookid
    def get_amount(self):
        return self._amount
    def get_isprocessed(self):
        return self._isprocessed
    def get_illegaldate(self):
        return self._illegaldate
    def get_illegaltype(self):
        return self._illegaltype

