from UserType import UserTypeAPI
from Recommand import Recommand
from Recommand import Recommand

class User(object):

    id = ''
    username = ''
    password = ''
    faculty = ''
    department = ''
    age = ''
    gendar = ''
    useridentity = ''
    userconnection = ''
    status = '正常'
    list_join = []

    def setid(self, userid):
        self.id = userid
        self.list_join.append('0')

    def getid(self):
        return self.id

    def setusername(self, username):
        self.username = username
        self.list_join.append('1')

    def getusername(self):
        return self.username

    def setpassword(self, password):
        self.password = password
        self.list_join.append('2')

    def getpassword(self):
        return self.password

    def setfaculty(self, faculty):
        self.faculty = faculty
        self.list_join.append('3')

    def getfaculty(self):
        return self.faculty

    def setdepartment(self, department):
        self.department = department
        self.list_join.append('4')

    def getdepartment(self):
        return self.department

    def setage(self, age):
        self.age = age
        self.list_join.append('5')

    def getage(self):
        return self.age

    def setgendar(self, gendar):
        self.gendar = gendar
        self.list_join.append('6')

    def getgendar(self):
        return self.gendar

    def setuseridentity(self, useridentity):
        self.useridentity = useridentity
        self.list_join.append('7')

    def getuseridentity(self):
        return self.useridentity

    def setuserconnection(self, userconnection):
        self.userconnection = userconnection
        self.list_join.append('8')

    def getuserconnection(self):
        return self.userconnection

    def setstatus(self, status):
        self.status = status
        self.list_join.append('9')

    def getstatus(self):
        return self.status

    def getusertype(self):
        user = UserTypeAPI()
        user.GetUserType(self.id)

    def setRecommand(self, user):
        user.setrecommand(self.id)

    def getRecommand(self):
        user = Recommand()
        User = user.GetRecommandRecord({'userid': self.id})

