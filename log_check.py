#!/usr/bin/env python3
import re
import csv

d, new_d = {}, {}
users, new_users = {}, {}
names = []
with open("syslog.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
            error = re.findall("([ERROR|INFO]+) ([\w\'\s]*)", line)
            user = re.findall("\((\w*\.?\w*)\)", line)
            error, user, kind = error[0][1], user[0], error[0][0]
            if user not in names:
                names.append(user)
            if kind == "ERROR":  
                if error in d.keys():
                    d[error] = d[error]+1
                else:
                    d[error] = 1
                if f"{user}_err" in users.keys():
                    users[f"{user}_err"] = users[f"{user}_err"]+1
                else:
                    users[f"{user}_err"] = 1
            elif kind == "INFO":
                if f"{user}_info" in users.keys():
                    users[f"{user}_info"] = users[f"{user}_info"]+1
                else:
                    users[f"{user}_info"] = 1          
for name in names:
    if f"{name}_err" not in users.keys():
        users[f"{name}_err"] = 0
    if f"{name}_info" not in users.keys():
        users[f"{name}_info"] = 0
names = sorted(names)
users = sorted(users.items())
resultUsers = dict((x, y) for x, y in users)
d = sorted(d.items(), key=lambda x:x[1], reverse=True)
resultMessages = dict((x, y) for x, y in d)
for x, y in resultMessages.items():
    new_d[x] = {"Error": x, "Count":y}
for name in names:
    inf = (resultUsers.get(f"{name}_info"))
    err = (resultUsers.get(f"{name}_err"))
    temp = {"Username": name, "INFO": inf, "ERROR": err}
    new_users[name] = temp
    
keys_err = ["Error", "Count"]
users_count = ["Username", "INFO", "ERROR"]
with open("error_message.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=keys_err)
    writer.writeheader()
    writer.writerows(new_d.values())
with open("user_statistics.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=users_count)
    writer.writeheader()
    writer.writerows(new_users.values())