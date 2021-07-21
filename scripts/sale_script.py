from xmlrpc import client

url = 'http://localhost:8069'
db = 'openpg'
username = 'admin'
password = 'admin'

common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
print(common.version())

uid = common.authenticate(db, username, password, {})
print(uid)

models = client.ServerProxy("{}/xmlrpc/2/object".format(url))

model_acces = models.execute_kw(db, uid, password,
                                'sale.order', 'check_access_rights',
                                ['write'], {'raise_exception': False})
print(model_acces)

