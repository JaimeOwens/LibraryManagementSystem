from User import UserAPI

class UserInterface(object):

    id = 0
    type = ''

    # 用于登陆，先查询admin表，非管理员再查询user表，管理员匹配成功，返回id字段为当前adminid，type为‘admin’，普通用户匹配成功，返回id字段为当前userid，type为user
    def login(self):
        user = UserAPI()
        id = input("请输入登陆id：")
        passwd = input("请输入密码：")
        if(user.matchIsAdmin(id, passwd) == True):
            print("登陆成功")
            self.id = id
            self.type = 'admin'
        else:
            if(user.matchIsUser(id, passwd) == True):
                print("登陆成功")
                self.id = id
                self.type = 'user'
            else:
                print("login error!")


    # 用于注册，仅限于普通用户
    def register(self):
        user=UserAPI()
        print("请依次输入学号（或教工号）、用户名、密码、学院、专业、年龄、性别（male或者female）、学位、联系方式，各项之间用空格隔开")
        list = input("：")
        list = list + ' 正常'
        list = list.split()
        list2 = tuple(list)
        list3 = []
        list3.append(list2)
        is_insert = user.InsertUserRecord(list3)
        if(is_insert):
            print("register success!")
        else:
            print("register failed!")
        self.Menu()

    # login or register
    def Menu(self):
        print("****** welcome ******")
        print("1. login")
        print("2. register")
        option = input("请输入：")
        if (option == '1'):
            self.login()
        elif (option == '2'):
            self.register()
        else:
            print("再见")

    def UserMenu(self):
        print("****** user *******")
        print("1. 个人信息") #修改查看个人资料、查看借阅记录、查看违章记录、
        print("2. 图书板块") #查询book、添加借阅记录（先查询有否有违章）、添加推荐记录
        option = input("请输入序号:")
        if(option == '1'):
            self.InforMenu()
        elif(option == '2'):
            self.BookMenu()
        else:
            print("输入错误")
            self.Menu()

    def InforMenu(self):
        print("****** 个人信息 ******")
        print("1. 查看个人资料")
        print("2. 修改个人资料")
        print("3. 查看借阅记录")
        print("4. 查看违章记录")
        option = input("请输入序号:")
        if(option == '1'):
            self.UserInfor()
        elif(option == '2'):
            self.UserInforAlter()
        elif(option == '3'):
            self.GetBorrow()
        elif(option == '4'):
            self.GetIllegal()
        else:
            print("输入错误")
            self.Menu()

    def BookMenu(self):
        print("****** 图书板块 ******")
        print("1. 查询书籍")
        print("2. 借阅书籍")
        print("3. 推荐书籍")
        option = input(":")

    def AdminMenu(self):
        print("****** admin ******")
        #五个模块

    def UserInfor(self):
        user = UserAPI()
        user.GetUserShow(self.id)
        user.GetUserType(self.id)

    def UserInforAlter(self):
        user = UserAPI()
        print("1.用户名")
        print("2.密码")
        print("3.学院")
        print("4.专业")
        print("5.年龄")
        print("6.性别")
        print("7.学位")
        print("8.联系方式")
        options = {'1': 'username', '2': 'password', '3': 'faculty', '4': 'department', '5': 'age', '6': 'gender',
                   '7': 'useridentity', '8': 'userconnection'}
        keys = input("请依次输入修改项，并用空格隔开：")
        keys = keys.split()
        keys1 = []
        for i in range(len(keys)):
            keys1.append(options[keys[i]])
        values = input("请输入修改值：")
        values = values.split()
        alterdict = dict(zip(keys1, values))
        for key in alterdict:
            user.UpdateRecord('user', key, alterdict[key], 'userid', self.id)

    def GetBorrow(self):
        print("****** borrow ******")
        # 查借阅表

    def GetIllegal(self):
        print("****** illegal ******")
        # 查违章表


test = UserInterface()
test.Menu()
if(test.type=='user'):
    print("welcome user")
    test.UserMenu()
elif(test.type=='admin'):
    print("welcome admin")
    test.AdminMenu()
else:
    #print("error!")
    test.Menu()
