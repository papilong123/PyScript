import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)

# 创建用户testUser
# db0 = client["admin"]
# db0.authenticate('admin', 'admin')
# db0.command('createUser', 'testUser', pwd='password', roles=[{
#     'role': 'readWrite',
#     'db': 'testDB'
# }])

# 连接和认证用户testUser
client['admin'].authenticate("testUser", "password", mechanism='SCRAM-SHA-1')

user_coll = client["testDB"]["users"]

new_user = {"ljl": "ljl"}
result = user_coll.insert_one(new_user)


client.close()


