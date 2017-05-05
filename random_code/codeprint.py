# -*- coding: utf-8 -*-
import os
import random
import pyperclip
import sqlite3
# import getpass #安全输入密码，不显示，Python自带库

# result = False
# while not result:
#     word = "0123456789abcdefghijklmnopqrstuvwxyz,./<>?!@#$%^&*-_+"
#     guess = ''.join(random.sample(word, random.randint(6, len(word))))
#     password = guess
#     print password

#     user_id = self._user_control.verify_admin_user_login(username, password)
#     if user_id > 0:
#         result = True
#         print password

def randomString(num):
    source_word = "0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz!@#$%^&*"
    guess = ''.join(random.choice(source_word) for x in range(num))
    return guess

# def create_sql(sql_name):
#     conn = sqlite3.connect(sql_name)
#     cursor = conn.cursor()
#     if not sql_name:
#         cursor.execute('create table password (id VARCHAR(20) PRIMARY KEY, name VARCHAR(20), password VARCHAR(32), password_create_time CURRENT_TIMESTAMP, password_update_time CURRENT_TIMESTAMP)')

def save_to_sql(table_name, for_name, content):
    # 打开或创建数据库
    conn = sqlite3.connect('passbook')
    cursor = conn.cursor()

    # 表不存在则创建
    try:
        cursor.execute('create table IF NOT EXISTS password (id INTEGER PRIMARY KEY autoincrement, name VARCHAR(20), password VARCHAR(32), password_create_time CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP , password_update_time CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP )')
    except:
        pass

    data = (for_name, content)
    cursor.execute('insert into %s (name, password) VALUES (?, ?)' %table_name , data)
    result = cursor.rowcount
    cursor.close()
    conn.commit()
    conn.close()

    return result if result else None

if __name__ == "__main__":
    print 'Start...'
    for_name = raw_input("For what:").decode('utf-8')
    # for_name = getpass.getpass("For what:").decode('utf-8')
    guess = randomString(32)
    result = save_to_sql('password', for_name, guess)
    if result:
        print for_name, '-->', '***'
        pyperclip.copy(guess)
