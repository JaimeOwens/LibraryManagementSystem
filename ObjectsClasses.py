# -*- coding: UTF-8 -*-

class User:
    userid = ""
    name = ""
    passwd = ""
    connecttion = ""
    gender = ""
    age = 0
    status = ""
    identity = ""
    maxborrow = 0
    maxrecom = 0
    borrowtime = 0

    def __init__(self, userid, name, passwd, connecttion, gender, age, status):
        self.userid = userid
        self.name = name
        self.connection = connecttion
        self.gender = gender
        self.age = age
        self.status = status

    def getType(self, identity, maxborrow, maxrecom, borrowtime):
        self.identity = identity
        self.maxborrow = maxborrow
        self.maxrecom = maxrecom
        self.borrowtime = borrowtime

class Admin:
    adminid = ""
    passwd = ""
    connecttion = ""
    permission = 0

    def __init__(self, adminid, passwd, connecttion, permission):
        self.adminid = adminid
        self.passwd = passwd
        self.connecttion = connecttion
        self.permission = permission


