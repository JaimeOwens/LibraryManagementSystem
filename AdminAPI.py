# -*- coding: UTF-8 -*-
from Admin import *
from MiddleLayer import MiddleLayer
from SQLFactories import Mysql

class AdminAPI:
    def matchIsAdmin(self, adminid, passwd):
        '''
        :param adminid:
        :param passwd:
        根据id、passwd字段查询admin表，匹配管理员成功返回adminid
        '''
        mysql = Mysql()
        sql = "select * from admin where adminid = '" + adminid + "' and passwd = '" + passwd + "'"
        if (mysql.getOne(sql) != False):
            print("login success!")
            adminpermission = self.GetAdminPermission(adminid)
            return [adminid, adminpermission]

    def GetAdminPermission(self, adminid):
        '''
        :param adminid:
        :return: 管理员权限编号
        '''
        mysql = Mysql()
        sql = "select adminpri from admin where adminid ='" + adminid + "'"
        adminpermission = mysql.getOne(sql)
        return list(adminpermission)

    def GetAllAdminRecord(self):
        '''
        :param Dict:
        输出admin表所有字段
        '''
        mysql = Mysql()
        sqlAll = "select * from admin"
        result = mysql.getAll(sqlAll)
        mysql.dispose()
        show = MiddleLayer()
        tums = show.ShowAdmin(result)
        return tums