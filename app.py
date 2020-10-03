from fbchat import Client
from Auth.credentials import user, password, person

client = Client(user, password)
if not client.isLoggedIn():
    client.login(user, password)
    print("Login successful...")

user = client.searchForUsers(person)[0]
userid = user.uid
thread_id = userid
messages = []

me = client.fetchThreadMessages(thread_id=thread_id, limit=500)
me.reverse()
print(len(me))
for m in me:
    u = client.fetchUserInfo(m.author)[m.author]
    print(u.name, m.text)

client.logout()
