from xmlrpc import client

url = 'https://arasilva-odoo-academy-main-2921480.dev.odoo.com'
db = 'arasilva-odoo-academy-main-2921480'
username = 'admin'
password = 'admin'

common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
print(common.version())

uid = common.authenticate(db, username, password, {})
print(uid)

models = client.ServerProxy("{}/xmlrpc/2/object".format(url))

model_acces = models.execute_kw(db, uid, password,
                                'academy.session', 'check_access_rights',
                                ['write'], {'raise_exception': False})
print(model_acces)

courses = models.execute_kw(db, uid, password,
                            'academy.course', 'search_read',
                            [[['level', 'in', ['intermediate', 'beginner']]]])
print(courses)

course = models.exceute_kw(db, uid, password,
                           'academy.course', 'search',
                           [[['name', '=', '   ']]])
print(course)

session_fields = models.execute_kw(db, uid, password,
                                   'academy.session', 'fields_get',
                                   [], {'attributes': ['string', 'type', 'required']})
print(session_fields)

new_session = models.execute(db, uid, password,
                             'academy.session', 'create',
                             [
                                 {
                                     'course_id': course[0],
                                     'state': 'open',
                                     'duration': 5,
                                 }
                             ]
                             )
print(new_session)
