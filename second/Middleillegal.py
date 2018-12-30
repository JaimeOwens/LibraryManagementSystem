

class MiddleBorrow:
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

    #将上面不为空的属性转换成字典
    def BookToDict(self):
        #拼接成Dict函数
        #例：{'bookid': '100014', 'author': '韩强军'}
        Seq = []
        Val = []
        if self._illegalid != '':
            Seq.append('illegalid')
            Val.append(self._illegalid)
        if self._userid != '':
            Seq.append('userid')
            Val.append(self._userid)
        if self._bookid != '':
            Seq.append('bookid')
            Val.append(self._bookid)
        if self._amount != '':
            Seq.append('amount')
            Val.append(self._amount)
        if self._isprocessed != '':
            Seq.append('isprocessed')
            Val.append(self._isprocessed)
        if self._illegaldate != '':
            Seq.append('illegaldate')
            Val.append(self._illegaldate)
        if self._illegaltype != '':
            Seq.append('illegaltype')
            Val.append(self._illegaltype)
        Dict = dict(zip(Seq,Val))
        print(Dict)



obj = MiddleBorrow()
obj.set_illegalid('100000')
obj.set_bookid('30000')
obj.BookToDict()
