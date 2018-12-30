

class MiddleBorrow:
    _borrowid = ''
    _userid = ''
    _bookid = ''
    _borrowdate = ''
    _presretdate = ''
    _actretdate = ''
    #定义set方法
    def set_borrowid(self,borrowid):
        self._borrowid = borrowid
    def set_userid(self,userid):
        self._userid = userid
    def set_bookid(self,bookid):
        self._bookid = bookid
    def set_borrowdate(self,borrowdate):
        self._borrowdate = borrowdate
    def set_presretdate(self,presretdate):
        self._presretdate = presretdate
    def set_actretdate(self,actretdate):
        self._actretdate = actretdate


    #get
    def get_borrowid(self):
        return self._borrowid
    def get_userid(self):
        return self._userid
    def get_bookid(self):
        return self._bookid
    def get_borrowdate(self):
        return self._borrowdate
    def get_presretdate(self):
        return self._presretdate
    def get_actretdate(self):
        return self._actretdate





# obj = MiddleBorrow()
# obj.set_userid('100000')
# obj.set_bookid('30000')
# obj.BookToDict()
