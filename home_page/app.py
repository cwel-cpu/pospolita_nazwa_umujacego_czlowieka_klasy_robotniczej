# 05.06.2026
# print("test")
# name = input("whats ur name?")
# print("hello", name)

# print("hello")
# name = input("My name is ")
# place = input("Im from ")
# fav = input("My favourite thing is ")

# print("hello")
# name = input("My name is \n")
# place = input("Im from \n")
# fav = input("My favourite thing is \n")
# print("information which u wrote:", name, place, fav)

# print("calculator")
# x=int(input("type first number: "))
# y=int(input("type second number: "))
# print(x+y)
# print(x-y)
# print(x*y)
# if y!=0:
#     print(x/y)
# else:
#     print("cant")

# essa = int(input("enter number: "))
# if essa%2 == 0:
#     print("even number")
# else:
#     print("odd number")

# cwel = int(input("type a number: "))
# if cwel > 0:
#     print("positive")
# elif cwel == 0:
#     print("its zero")
# else:
#     print("negative")

# login = "cwel"
# password = "upo"

# logint = input("login: ")
# passwordt = input("password: ")
# passwordre = input("retype password: ")
# if login == logint and password == passwordt and password == passwordre:
#     print("login and password checked")
# else:
#     print("err")

# print("can u access")
# age = int(input("type age: "))
# if age <= 16:
#     print("bad age")
#     exit()
# paid = input("did u pay? (only yes or no) ")
# if paid == "no":
#     print("u have to pay")
#     exit()
# score = int(input("type ur score: "))
# if score >80:
#     print("u gain access to higher level")
# elif score >50:
#     print("u gain acces to intermediate lvl")
# else:
#     print("bad grade no access")

# if age >= 16 and paid == "yes" and score >80:
#     print("u gain access to higher level")
# elif age >= 16 and paid == "yes" and score >50:
#     print("u gain acces to intermediate lvl")
# elif age >= 16 and paid == "yes" and score <50:
#     print("bad grade no access")
# else:
#     print("no access")

# for i in range(1, 5):
#     print(i* "*")

# dalsza czesc 06.06.2026 dzien

# balance = 1000 
# choice = 0 

# while choice != 4: 
#     choice = int(input("choose option: 1-check balance, 2-deposit money, 3-withdraw money, 4-exit: ")) 
    
#     if choice == 1: 
#         print(balance) 
#     elif choice == 2: 
#         addmoney = int(input("type how much to deposit: ")) 
#         balance += addmoney 
#         print("u deposit: ", addmoney) 
#         print("ur balance is: ", balance) 
#     elif choice == 3: 
#         rmoney = int(input("type how much to withdraw: ")) 
#         if rmoney > balance: 
#             print("not enough money") 
#         else: 
#             balance -= rmoney 
#             print("u withdraw: ", rmoney) 
#             print("ur balance is: ", balance) 
#     elif choice == 4: 
#         print("end") 
#     else: 
#         print("err")


# balance = 1000
# choice = 0

# def balancecheck():
#     global balance
#     print(balance)
# def depositcheck():
#     addmoney = int(input("type how much to deposit: "))
#     global balance
#     balance += addmoney
#     print("u deposit: ", addmoney)
#     print("ur balance is: ", balance)
# def rmoney():
#     rmoney = int(input("type how much to withdraw: "))
#     global balance
#     if rmoney > balance:
#         print("not enough money")
#     else:
#         balance -= rmoney
#         print("u withdraw: ", rmoney)
#         print("ur balance is: ", balance)



# while choice != 4:
#     choice = int(input("choose option: 1-check balance, 2-deposit money, 3-withdraw money, 4-exit: "))
#     match choice:
#         case 1:
#             balancecheck()
#         case 2:
#             depositcheck()
#         case 3:
#             rmoney()
#         case 4:
#             print("end")

# fruits = ["apple", "peach", "rasberry", "watermelon", "banana"]
# fruits.append("kivi")
# fruits.insert(0, "ork")
# fruits.insert(1, "new")
# fruits[3] = "newnew"
# fruits.pop(7)
# print(fruits)
# napisz w pythonie prosty program ktory pyta o liczbe uczniow po tym ich imie plec i ocene wedlug wpisanej ilosci uczniow zapisz dane w tablicach. oceny od 0 do 50 fail, 50 do 69 srednio, 70 do 89 dobrze, od 90 do 100 bardzo dobrych, statystyka ilczba uczniow, srednia ocen, liczba ocen bardzo dobrych, liczba ocen fail

# countstudents = int(input("how many students u have: "))
# studentsdat = input("name of a student: ")
# gradestudent = int(input("grade 0-100: "))
# tc = []
# ts = []
# tg = []
# tc.append(countstudents)
# for i in range(1, countstudents):
#     ts.append(studentsdat)
    
# tg.append(gradestudent)
# print(tc)
# print(ts)
# print(tg)

# from flask import Flask, render_template, request, url_for
# import sqlite3

# app = Flask(__name__)

# def get_db_connection():
#     connection = sqlite3.connect("dataSchool.db")
#     cursor = connection.cursor()


#     cursor.execute("CREATE TABLE IF NOT EXISTS grade_table (id INTEGER PRIMARY KEY, subject_score1 REAL, subject_score2 REAL, subject_score3 REAL)")
#     cursor.execute("CREATE TABLE IF NOT EXISTS students_table (id INTEGER PRIMARY KEY, fname TEXT, lname TEXT, age INTEGER, id_grade INTEGER, FOREIGN KEY(id_grade) REFERENCES grade_table(id))")
#     cursor.execute("INSERT OR IGNORE INTO grade_table(id, subject_score1, subject_score2, subject_score3) VALUES (1, NULL, NULL, NULL)")
#     cursor.execute("INSERT OR IGNORE INTO students_table(id, fname, lname, age, id_grade) VALUES (1, 'dominik', 'nieckowski', 18, 1)")
#     cursor.execute("SELECT * FROM students_table")
#     connection.commit()
#     connection.close()

# name = []
# gender = []
# grades = []

# @app.route("/", methods=["GET", "POST"])
# def home():
#     gr = ""

#     if request.method == "POST":
#         if "name" in request.form:
#             imie = request.form.get("name")
#             plec = request.form.get("gender")
#             ocena = float(request.form.get("grade"))
            
#             name.append(imie)
#             gender.append(plec)
#             grades.append(ocena)

#         if "sname" in request.form:
#             searchname = request.form.get("sname")
#             se = name.index(searchname)
#             gr = grades[se]

#     countstu = len(grades)
#     if countstu > 0:
#         srednia = sum(grades) / countstu

#         excellent = 0
#         fail = 0
#         for g in grades:
#             if g < 50:
#                 fail += 1
#             if g >= 90:
#                 excellent += 1
#         highest = max(grades)
#         lowest = min(grades)
#     else:
#         srednia = 0; excellent = 0; fail = 0; highest = 0; lowest = 0

#     return render_template(
#         "index.html",
#         name="Dominik",
#         grade=gr,
#         countstu=countstu,
#         srednia=srednia,
#         excellent=excellent,
#         fail=fail,
#         highest=highest,
#         lowest=lowest,
#         css=url_for("static", filename="style.css")
#     )
# if __name__ == "__main__":
#     app.run(debug=True)

# 11 i 12 czerwiec to caly czas 12 czerwca dodane zostalo sqllite3 do pythona i wstep fo version control github

from flask import Flask, render_template, request, url_for
import sqlite3
app = Flask(__name__)

def run():
    conn = sqlite3.connect("dataSchool.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS grade_table (id INTEGER PRIMARY KEY AUTOINCREMENT, subject_score1 REAL, subject_score2 REAL, subject_score3 REAL)")
    cur.execute("CREATE TABLE IF NOT EXISTS students_table (id INTEGER PRIMARY KEY AUTOINCREMENT, fname TEXT, id_grade INTEGER)")
    conn.commit()
    conn.close()
run()

@app.route("/", methods=["GET", "POST"])
def home():
    gr = ""
    conn = sqlite3.connect("dataSchool.db")
    cur = conn.cursor()

    if request.method == "POST":
        if "name" in request.form and "grade" and "grade2" and "grade3" in request.form:
            imie = request.form.get("name")
            ocena = float(request.form.get("grade"))
            ocena2 = float(request.form.get("grade2"))
            ocena3 = float(request.form.get("grade3"))
            cur.execute("INSERT INTO grade_table (subject_score1, subject_score2, subject_score3) VALUES (?, ?, ?)", (ocena, ocena2, ocena3))
            cur.execute("INSERT INTO students_table (fname, id_grade) VALUES (?, ?)", (imie, cur.lastrowid))
            conn.commit()
        if "sname" in request.form:
            cur.execute("SELECT g.subject_score1, g.subject_score2, g.subject_score3 FROM students_table s JOIN grade_table g ON s.id_grade = g.id WHERE s.fname = ?", (request.form.get("sname"),))
            wynik = cur.fetchone()
            gr = wynik if wynik else "brak"
            if "delete_id" in request.form:
                id_del = request.form.get("delete_id")
                cur.execute("SELECT id_grade FROM students_table WHERE id = ?", (id_del,))
                wiersz = cur.fetchone()
                if wiersz:
                    cur.execute("DELETE FROM students_table WHERE id = ?", (id_del,))
                    cur.execute("DELETE FROM grade_table WHERE id = ?", (wiersz[0],))
                    conn.commit()
    cur.execute("SELECT subject_score1, subject_score2, subject_score3 FROM grade_table")
    wszystkie_oceny = [w for w in cur.fetchall() if all(x is not None for x in w)]
    countstu = len(wszystkie_oceny)

    if countstu > 0:
        srednia = sum(sum(oceny) for oceny in wszystkie_oceny) / (countstu * 3)
        excellent = sum(1 for oceny in wszystkie_oceny if all(g >= 90 for g in oceny))
        fail = sum(1 for oceny in wszystkie_oceny if all(g < 50 for g in oceny))
        highest = max(max(oceny) for oceny in wszystkie_oceny)
        lowest = min(min(oceny) for oceny in wszystkie_oceny)
    else:
        srednia = excellent = fail = highest = lowest = 0
    conn.close()

    return render_template(
        "index.html",
        name="Dominik",
        grade=gr,
        countstu=countstu,
        srednia=round(srednia, 2),
        excellent=excellent,
        fail=fail,
        highest=highest,
        lowest=lowest,
        css=url_for("static", filename="style.css")
    )

if __name__ == "__main__":
    app.run(debug=True)





        # if "delete_id" in request.form:
        #     id_del = request.form.get("delete_id")
        #     cur.execute("SELECT id_grade FROM students_table WHERE id = ?", (id_del,))
        #     wiersz = cur.fetchone()
        #     if wiersz:
        #         cur.execute("DELETE FROM students_table WHERE id = ?", (id_del,))
        #         cur.execute("DELETE FROM grade_table WHERE id = ?", (wiersz[0],))
        #         conn.commit()





# name = []
# gender = []
# grades = []

# countstu = int(input("how many students: "))
# for i in range(countstu):
#     imie = input("name: ")
#     plec = input("gender: ")
#     ocena = float(input("grade: "))
    
#     name.append(imie)
#     gender.append(plec)
#     grades.append(ocena)
# srednia = sum(grades) / countstu

# excellent = 0
# fail = 0
# for g in grades:
#     if g < 50:
#         fail += 1
#     if g >= 90:
#         excellent += 1

# highest = max(grades)
# lowest = min(grades)

# print("number of students: ", countstu)
# print("average grade: ", srednia)
# print("number of excellent grades: ", excellent)
# print("number of fail grades: ", fail)
# print("highest grade: ", highest)
# print("lowest grade: ", lowest)
# choice = 0
# while choice != 2: 
#     choice = int(input("search after name - 1, exit - 2: ")) 
    
#     if choice == 1: 
#         searchname= input("type: ")
#         se = name.index(searchname)
#         gr = grades[se]
#         print("index of name ", se)
#         print("grade: ", gr)
#     elif choice == 2: 
#         print("end") 
#     else: 
#         print("err")