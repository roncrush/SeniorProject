import MySQLdb as mysql


class AmmDB(object):
    def __init__(self):
        self.conn = mysql.connect(host='127.0.0.1', port=3306, user='root', passwd='admin', db='mydb')
        self.cursor = self.conn.cursor(mysql.cursors.DictCursor)

    @staticmethod
    def get_where_stmnt(where_query, col_name, value, operator, compare=''):
        if where_query == "":
            if compare == 'like':
                return "WHERE " + col_name + " LIKE '%" + value + "%' "
            else:
                return "WHERE " + col_name + " = " + value
        else:
            if compare == 'like':
                return " " + operator + " " + col_name + " LIKE '%" + value + "%' "
            else:
                return " " + operator + " " + col_name + " = " + value

    def check_email_exist(self, email):
        if self.conn.closed:
            self.__init__()

        self.cursor.execute("SELECT email FROM user WHERE email = '" + email + "'")
        data = self.cursor.fetchall()

        if len(data) > 0:
            return True
        else:
            return False

    def check_uname_exist(self, uname):
        if self.conn.closed:
            self.__init__()

        self.cursor.execute("SELECT uname FROM user WHERE uname = '" + uname + "'")
        data = self.cursor.fetchall()

        if len(data) > 0:
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

        self.cursor.execute("INSERT INTO user (uname, email, passwd, phone, fn, ln, admin) "
                            "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                            (uname, email, passwd, phone, fn, ln, admin))
        self.conn.commit()

    def add_activity(self, name, skill, datetime, duration, numplayers, private, available, category, leader):
        if self.conn.closed:
            self.__init__()

        self.cursor.execute("INSERT INTO activity " +
                            "(name, skill, datetime, duration, numplayers, private, available, category, leader) " +
                            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                            (name, skill, datetime, duration, numplayers, private, available, category, leader, ))
        self.conn.commit()

    def get_activity_type(self, activity_type_id='', name='', operator='AND'):
        if self.conn.closed:
            self.__init__()

        where_query = ''

        params = {
            'id': activity_type_id,
            'name': name,
        }

        for param, value in params.items():
            if value != '':
                if param == 'name':
                    where_query += self.get_where_stmnt(where_query, param, value, operator, 'like')
                else:
                    where_query += self.get_where_stmnt(where_query, param, str(value), operator)

        self.cursor.execute("SELECT * FROM activitytype " + where_query)
        data = self.cursor.fetchall()

        return data

    def get_activity(self, activity_id='', name='', skill='', duration='', numplayers='', available='', category='',
                     leader='', operator='AND'):
        if self.conn.closed:
            self.__init__()

        where_query = ""

        params = {
            'id': activity_id,
            'name': name,
            'skill': skill,
            'duration': duration,
            'numplayers': numplayers,
            'available': available,
            'category': category,
            'leader': leader,
        }

        for param, value in params.items():
            if value != '':
                if param == 'name':
                    where_query += self.get_where_stmnt(where_query, param, value, operator, 'like')
                else:
                    where_query += self.get_where_stmnt(where_query, param, str(value), operator)

        self.cursor.execute("SELECT * FROM activity " + where_query)
        data = self.cursor.fetchall()

        return data

    def get_user(self, user_id='', uname='', email='', phone='', fn='', ln='', operator='AND'):
        if self.conn.closed:
            self.__init__()

        where_query = ""

        params = {
            'id': user_id,
            'uname': uname,
            'email': email,
            'phone': phone,
            'fn': fn,
            'ln': ln,
        }

        for param, value in params.items():
            if value != '':
                if param == 'name':
                    where_query += self.get_where_stmnt(where_query, param, value, operator, 'like')
                else:
                    where_query += self.get_where_stmnt(where_query, param, str(value), operator)

        self.cursor.execute("SELECT * FROM user " + where_query)
        data = self.cursor.fetchall()

        return data

    def get_user_activity(self, user_id='', activity_id='', private_app='', operator='AND'):
        if self.conn.closed:
            self.__init__()

        where_query = ''

        params = {
            'userid': user_id,
            'activityid': activity_id,
            'private_application': private_app,
        }

        for param, value in params.items():
            if value != '':
                where_query += self.get_where_stmnt(where_query, param, str(value), operator)

        self.cursor.execute("SELECT * FROM useractivity " + where_query)
        data = self.cursor.fetchall()

        return data
