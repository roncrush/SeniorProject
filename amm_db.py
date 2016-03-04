import _mysql


class AmmDB(object):
    def __init__(self):
        self.conn = _mysql.connect(host='127.0.0.1', port=3306, user='root', passwd='admin', db='mydb')

    @staticmethod
    def pack(data):
        rows = []
        row = data.fetch_row()

        while len(row) > 0:
            for record in row:
                rows.append(record)
            row = data.fetch_row()

        return rows

    def check_email_exist(self, email):
        if self.conn.closed:
            self.__init__()

        self.conn.query("SELECT email FROM user WHERE email = '" + email + "'")
        data = self.conn.store_result()
        row = data.fetch_row()

        if len(row) > 0:
            return True
        else:
            return False

    def check_uname_exist(self, uname):
        if self.conn.closed:
            self.__init__()

        self.conn.query("SELECT uname FROM user WHERE uname = '" + uname + "'")
        data = self.conn.store_result()
        row = data.fetch_row()

        if len(row) > 0:
            return True
        else:
            return False

    def add_user(self, uname, email, passwd, phone, fn, ln, admin):
        if self.conn.closed:
            self.__init__()

        if self.check_uname_exist(uname):
            return 'Username exists'
        elif self.check_email_exist(email):
            return 'Email exists'

        self.conn.query("INSERT INTO user (uname, email, passwd, phone, fn, ln, admin) VALUES ('" +
                        uname + "' , '" + email + "' , '" + passwd + "' , " + phone + " , '" + fn + "' , '" +
                        ln + "' , " + admin + ")")

    def add_activity(self, name, skill, datetime, duration, numplayers, private, available, category, leader):
        if self.conn.closed:
            self.__init__()

        self.conn.query("INSERT INTO activity " +
                        "(name, skill, datetime, duration, numplayers, private, available, category, leader) " +
                        "VALUES ('" + name + "' , " + skill + " , '" + datetime + "' , " + duration + " , " +
                        numplayers + " , " + private + " , " + available + " ," + category + " , " + leader + ")")

    def get_activity_type(self, activity_id='', name=''):
        if self.conn.closed:
            self.__init__()

        query = ''

        if id != '':
            query += ("id = " + activity_id + " ")
        if name != '':
            if query != '':
                query += ("AND name ='" + name + "' ")
            else:
                query += ("name ='" + name + "' ")

        if query == '':
            self.conn.query("SELECT * FROM activitytype")
        else:
            self.conn.query("SELECT * FROM activitytype WHERE " + query)

        data = self.conn.store_result()

        return self.pack(data)

    def get_activity(self, activity_id='', name='', skill='', duration='', numplayers='', available='', category='',
                     leader='', operator='AND'):
        if self.conn.closed:
            self.__init__()

        query = ''

        if id != '':
            query += ("id = " + activity_id + " ")
        if name != '':
            if query != '':
                query += (operator + " name LIKE '%" + name + "%' ")
            else:
                query += ("name LIKE '%" + name + "%' ")
        if skill != '':
            if query != '':
                query += (operator + " skill = '" + skill + "' ")
            else:
                query += ("skill = '" + skill + "' ")
        if duration != '':
            if query != '':
                query += (operator + " duration = '" + duration + "' ")
            else:
                query += ("duration = '" + duration + "' ")
        if numplayers != '':
            if query != '':
                query += (operator + " numplayers > '" + numplayers + "' ")
            else:
                query += ("numplayers = '" + numplayers + "' ")
        if available != '':
            if query != '':
                query += (operator + " available = '" + available + "' ")
            else:
                query += ("available = '" + available + "' ")
        if category != '':
            if query != '':
                query += (operator + " category = '" + category + "' ")
            else:
                query += ("category = '" + category + "' ")
        if leader != '':
            if query != '':
                query += (operator + " leader = '" + leader + "' ")
            else:
                query += ("leader = '" + leader + "' ")

        if query == '':
            self.conn.query("SELECT * FROM activity")
        else:
            self.conn.query("SELECT * FROM activity WHERE " + query)

        data = self.conn.store_result()

        return self.pack(data)

    def get_user(self,  user_id='', uname='', email='', phone='', fn='', ln=''):
        if self.conn.closed:
            self.__init__()

        query = ''

        if id != '':
            query += ("id = " + user_id + " ")
        if uname != '':
            if query != '':
                query += ("AND uname LIKE '%" + uname + "%' ")
            else:
                query += ("uname LIKE '%" + uname + "%' ")
        if email != '':
            if query != '':
                query += ("AND email = '" + email + "' ")
            else:
                query += ("email = '" + email + "' ")
        if phone != '':
            if query != '':
                query += ("AND phone = '" + phone + "' ")
            else:
                query += ("phone = '" + phone + "' ")
        if fn != '':
            if query != '':
                query += ("AND fn LIKE '%" + fn + "%' ")
            else:
                query += ("fn LIKE '%" + fn + "%' ")
        if ln != '':
            if query != '':
                query += ("AND ln LIKE '%" + ln + "%' ")
            else:
                query += ("ln LIKE '%" + ln + "%' ")

        if query == '':
            self.conn.query("SELECT * FROM user")
        else:
            self.conn.query("SELECT * FROM user WHERE " + query)

        data = self.conn.store_result()

        return self.pack(data)
