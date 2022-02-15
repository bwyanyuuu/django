import os
import sys
import pymysql
import subprocess

if __name__ == '__main__':
    db = pymysql.connect(
        host="localhost",
        user="icmr21_usr",
        passwd="@i1c2m3R4!",
        db="icmr21_db"
    )
    
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql_info = "SELECT * FROM info"
    cursor.execute(sql_info)
    users = cursor.fetchall()
    
    with open('./done.txt', 'r') as df:
        done = [e.strip() for e in df.readlines()]
            
        users = [user for user in users if user['email'] not in done]
        
        for idx, user in enumerate(users):
            first = user['firstname']
            middle = user['middle_name']
            last = user['lastname']
            email = user['email']
            affiliation = user['affiliation']
            password = user['password']
            
            if len(middle) == 0:
                # subprocess.call("/home/zk44nbagxcgk/virtualenv/program/3.7/bin/python  /home/zk44nbagxcgk/public_html/newUserParse.py --first $first_name --last $last_name --email $email --aff '$affiliation' --passw $password |  /home/zk44nbagxcgk/virtualenv/program/3.7/bin/python /home/zk44nbagxcgk/program/manage.py shell", shell=True) 
                os.system("/home/zk44nbagxcgk/virtualenv/program/3.7/bin/python  /home/zk44nbagxcgk/public_html/newUserParse.py --first '{}' --last '{}' --email '{}' --aff '{}' --passw '{}' |  /home/zk44nbagxcgk/virtualenv/program/3.7/bin/python /home/zk44nbagxcgk/program/manage.py shell".format(first, last, email, affiliation, password))
            else:
                # subprocess.call("/home/zk44nbagxcgk/virtualenv/program/3.7/bin/python  /home/zk44nbagxcgk/public_html/newUserParse.py --first $first_name --last $last_name --middle $middle_name --email $email --aff '$affiliation' --passw $password |  /home/zk44nbagxcgk/virtualenv/program/3.7/bin/python /home/zk44nbagxcgk/program/manage.py shell", shell=True)
                os.system("/home/zk44nbagxcgk/virtualenv/program/3.7/bin/python  /home/zk44nbagxcgk/public_html/newUserParse.py --first '{}' --last '{}' --middle '{}' --email '{}' --aff '{}' --passw '{}' |  /home/zk44nbagxcgk/virtualenv/program/3.7/bin/python /home/zk44nbagxcgk/program/manage.py shell".format(first, last, middle, email, affiliation, password))
