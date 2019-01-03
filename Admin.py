class Admin:
    _adminid = ""
    _passwd = ""
    _connecttion = ""
    _permission = 0

    def set_adminid(self, adminid):
        self._adminid = adminid

    def set_passwd(self, passwd):
        self._passwd = passwd

    def set_connection(self, connection):
        self._connecttion = connection

    def set_permission(self, permission):
        self._permission = permission

    def get_adminid(self):
        return self._adminid

    def get_passwd(self):
        return self._passwd

    def get_connection(self):
        return self._connecttion

    def get_permission(self):
        return self._permission
