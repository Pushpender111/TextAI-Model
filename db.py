import json
class database:
    def insert(self,name,email,password):
        with open("C:\\Users\\pushpender\\Desktop\\Python\\Pyhton Project\\user.json","r+") as rf:
            users=json.load(rf)
            if email in users:
                return 0
            else:
                users[email]=[name,password]
        with open("C:\\Users\\pushpender\\Desktop\\Python\\Pyhton Project\\user.json","w+") as wf:
            json.dump(users,wf,indent=4)
            return 1
    def user_exist(self,email,password):
        with open("C:\\Users\\pushpender\\Desktop\\Python\\Pyhton Project\\user.json","r") as rf:
            users=json.load(rf)
            if email in users:
                if password==users[email][1]:
                    return 1
                else:
                    return 0
            else:
                return 0