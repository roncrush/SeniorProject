from unittest import TestCase
from amm_db import AmmDB
import MySQLdb as mysql


class TestAmmDB(TestCase):
    def test_conn_check(self):
        host = ''
        user = ''
        passwd = ''
        self.conn = mysql.connect(host=host, port=3306, user=user, passwd=passwd, db='mydb')
        self.cursor = self.conn.cursor(mysql.cursors.DictCursor)
        self.failIf(self.conn.closed, self)

    def test_get_where_stmnt(self):
        db = AmmDB()
        observed = db.get_where_stmnt("", "testCol", "testVal", "", 'like')
        expected = "WHERE testCol LIKE '%testVal%' "
        self.assertEqual(observed, expected)

        observed = db.get_where_stmnt("", "testCol", "testVal", "", '')
        expected = "WHERE testCol = 'testVal'"
        self.assertEqual(observed, expected)

        observed = db.get_where_stmnt("testWhere", "testCol", "testVal", ">", 'like')
        expected = " > testCol LIKE '%testVal%' "
        self.assertEqual(observed, expected)

        observed = db.get_where_stmnt("testWhere", "testCol", "testVal", ">", '')
        expected = " > testCol = 'testVal'"
        self.assertEqual(observed, expected)

    def test_check_email_exist(self):
        db = AmmDB()
        self.assertTrue(db.check_email_exist("test@test.com"), True)

    def test_check_uname_exist(self):
        db = AmmDB()
        self.assertTrue(db.check_uname_exist("test"), True)

    def test_get_user(self):
        #first test output
        #Positive:
        #store observed get_user out
        #store expected get_user out
        #assertequal observed is expected
        #Negative:
        #store observed get_user out for bad params
        #store expected get_user out for bad params
        #assertequal observed is expected
        self.fail()

    def test_add_user(self):
        #Positive
        #Add user
        #get user
        #store observed get_user out
        #store expected get_user out
        #assertequal observed is expected
        #Negative
        #Add user with bad info
        #get user
        #store observed get_user out
        #store expected get_user out
        #assertnotequal observed is expected
        self.fail()

    def test_get_activity(self):
        #first test output
        #Positive:
        #store observed get_act out
        #store expected get_act out
        #assertequal observed is expected
        #Negative:
        #store observed get_act out for bad params
        #store expected get_act out for bad params
        #assertequal observed is expected
        self.fail()

    def test_add_activity(self):
        #Positive
        #Add user
        #get user
        #store observed get_act out
        #store expected get_act out
        #assertequal observed is expected
        #Negative
        #Add user with bad info
        #get user
        #store observed get_act out
        #store expected get_act out
        #assertnotequal observed is expected
        self.fail()

    def test_get_activity_type(self):
        # db = AmmDB()
        # observed = db.get_activity_type('25', 'testName', 'AND')
        # expected = "25 Arts and Crafts"
        # self.assertEqual(observed, expected)
        self.fail()

    def test_edit_user(self):
        #Positive
        #Edit user
        #get user
        #store observed get_user out
        #store expected get_user out
        #assertequal observed is expected
        #Negative
        #Add user with bad info
        #get user
        #store observed get_user out
        #store expected get_user out
        #assertnotequal observed is expected
        self.fail()


    def test_get_user_activity(self):
        #Positive
        #Edit usr_act
        #get act
        #store observed get_usract out
        #store expected get_usract out
        #assertequal observed is expected
        #Negative
        #Edit useract with bad info
        #get useract
        #store observed get_useract out
        #store expected get_useract out
        #assertnotequal observed is expected
        self.fail()
