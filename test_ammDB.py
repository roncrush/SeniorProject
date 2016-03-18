import unittest
from amm_db import AmmDB
import random
import sys
from flask.ext import bcrypt

class TestAmmDB(unittest.TestCase):
    def test_conn_check(self):
        db = AmmDB(self.password)
        self.failIf(db.conn.closed, self)

    def test_get_where_stmnt(self):
        db = AmmDB(self.password)
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
        db = AmmDB(self.password)
        self.assertTrue(db.check_email_exist("test@test.com"), True)

    def test_check_uname_exist(self):
        db = AmmDB(self.password)
        self.assertTrue(db.check_uname_exist("test"), True)

    def test_get_user(self):
        # Positive
        db = AmmDB(self.password)
        passwd = b'$2b$12$Z2OaKVc39OH6duIxaKFnkefKztlq7oPiYpzdNHfSwQDvBRfFjVCJ6'
        observed = db.get_user(9, fn='test', email='test@test.com', phone='5555555555', ln='test', uname='test', operator='AND', exact=False)
        expected = ({'suspension': None, 'admin': 0, 'uname': 'test', 'passwd': passwd, 'email': 'test@test.com', 'id': 9, 'phone': '5555555555', 'fn': 'test', 'ln': 'test'},)
        self.assertEqual(observed, expected)

        # Negative
        observed = db.get_user('-1', 'bad', 'bad@bad.com', '-11111111', 'bad', 'bad', 'AND', False)
        expected = ()
        self.assertEqual(observed, expected)

    #def test_add_user(self):
        # Positive
        #db = AmmDB(self.password)
        #db.add_user(fn='test1', email='test@test.com', uname='test', ln='test', passwd=bcrypt.Bcrypt().generate_password_hash('test'), admin=0, phone='1234567890')
        #passwd = b'$2b$12$Z2OaKVc39OH6duIxaKFnkefKztlq7oPiYpzdNHfSwQDvBRfFjVCJ6'
        #observed = db.get_user(9, 'test', 'test@test.com', '1234567890', 'test', 'test', 'AND', False)
        #expected = ({'suspension': None, 'admin': 0, 'email': 'test@test.com', 'uname': 'test', 'passwd': passwd, 'id': 9, 'phone': '1234567890', 'ln': 'test', 'fn': 'test'})
        #self.assertEqual(observed, expected)

        # Negative
        # Add user with bad info
        # get user
        # store observed get_user out
        # store expected get_user out
        # assertnotequal observed is expected

    def test_get_activity(self):
        # Positive
        db = AmmDB(self.password)
        # observed = db.get_activity(1, 'testName', 4, 1, 3, 1, 25, 9, 'AND')
        # expected = ({'id': 1, 'name': 'testName', 'numplayers': 3, 'available': 1, 'skill': 4, 'category': 25, 'longitude': Decimal('0.0000'), 'datetime': datetime.datetime(2017, 4, 13, 18, 36, 49), 'private': 0, 'latitude': Decimal('0.0000'), 'leader': 9, 'duration': 1})
        # self.assertEqual(observed, expected)

        # Negative
        observed = db.get_activity(0, 'badName', 4, 1, 3, 1, 25, 9, 'AND')
        expected = ()
        self.assertEqual(observed, expected)

    #def test_add_activity(self):
        # Positive
        # Add user
        # get user
        # store observed get_act out
        # store expected get_act out
        # assertequal observed is expected
        # Negative
        # Add user with bad info
        # get user
        # store observed get_act out
        # store expected get_act out
        # assertnotequal observed is expected
        #self.fail()

    def test_get_activity_type(self):
        # positive
        db = AmmDB(self.password)
        observed = db.get_activity_type('25', 'Arts and Crafts', 'AND')
        expected = ({'id': 25, 'name': 'Arts and Crafts'},)
        self.assertEqual(observed, expected)

        # negative
        observed = db.get_activity_type('0', 'Invalid', 'AND')
        expected = ()
        self.assertEqual(observed, expected)

    def test_edit_user(self):
        # Positive
        db = AmmDB(self.password)
        passwd=b'$2b$12$Z2OaKVc39OH6duIxaKFnkefKztlq7oPiYpzdNHfSwQDvBRfFjVCJ6'
        #random.seed()
        #randomfn = random.randint(1, 100)
        #randomln = random.randint(1, 100)
        db.edit_user(9, 'test@test.com', 'test', 'test', passwd, '5555555555')
        observed = db.get_user(9, 'test', 'test@test.com', '5555555555', 'test', 'test')
        expected = ({'admin': 0,'email': 'test@test.com','fn': 'test','id': 9,'ln': 'test','passwd': b'$2b$12$Z2OaKVc39OH6duIxaKFnkefKztlq7oPiYpzdNHfSwQDvBRfFjVCJ6','phone': '5555555555','suspension': None,'uname': 'test'},)
        self.assertEqual(observed, expected)

        # Negative
        # Add user with bad info
        # get user
        # store observed get_user out
        # store expected get_user out
        # assertnotequal observed is expected
        #self.fail()

    def test_get_user_activity(self):
        # Positive
        db = AmmDB(self.password)
        #looks like we are missing private_application in the DB
        #we're not missing private_application, it was removed from UserActivity
        #a few weeks ago because it is not needed in UserActivity because private is
        #already stored in Activity, similarly to datetime from earlier
        observed = db.get_user_activity(9, 1, 'AND')
        expected = ({'activityid': 1, 'userid' : 9},)
        self.assertEqual(observed, expected)

        # Negative
        observed = db.get_user_activity(-1, 25, 'AND')
        expected = ()
        self.assertEqual(observed, expected)

    #TODO
    def test_add_user_activity(self):
        pass

if __name__ == '__main__':
    TestAmmDB.password = sys.argv.pop()
    unittest.main()
