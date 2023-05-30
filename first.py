# ##=  =   +
# ##>>> Employee the class in empo
# from employee import Employee

# import sqlite3
#                      ### this is will create a file 
# ### <<<<<this is like opening a book and naming it as >> employee.db
# conn = sqlite3.connect('employee.db') ####  in() u pass a variable name
# ##  in memory database >>>>> (":memory:")
# ## if u run (employee.db)file   will be created 

# ###  here u create a cursor 
# ####<<<<  creating a pen where u can use it to write 
# c =  conn.cursor()
# ####it is important to include the brackets when 
# ### calling a method in programming to ensure that it is
# ###  executed correctly.


# ####  TABLE CREATION 
# ## THE PEN  I CREATED WE USE IT TO WRITE THE TABLE 


# # c.execute ("""CREATE TABLE employees(
# #         first text,
# #         last text,
# #         pay integer
# #          )""")


# emp_1 = Employee('john', 'doe', 8000000)
# emp_2 = Employee('dan', 'kinuthia', 8000000)


# c.execute("INSERT INTO employees VALUES (?, ?, ?)",(emp_1.first,emp_1.last,emp_1.pay))


# ##### INPUTING VALUE IN THE TABLE ACORDING TO THE ARRANGMENT OF CREATION

# # c.execute("INSERT INTO employees VALUES ('BARRY', 'KLEIN', 500000)")

# ##### here we   see the table value in the employees

# # c.execute("SELECT * FROM employees WHERE last = 'KLEIN'  ")

# ##### PRINTING THE TABLE VALUE 


# ## c.fetchone() >>>  RETURN THE RAW 

# ## c.fetchmany(56) >>> THIS RETURN THE RAWS U WANT THA WHY 
# #IT TAKES A AGUMENT OF NUMBER AND RETURN THE OUT PUT AS A LIST

# ## c.fetchall() >>> this will return the all raws


# print(c.fetchone())
 

# conn.commit()
# conn.close()





# import sqlite3
# from employee import Employee

# conn = sqlite3.connect(':memory:')
# c = conn.cursor()

# emp_1 = Employee('poul', 'bungo', 8000000)
# emp_2 = Employee('dan', 'kinuthia', 33476400)
# emp_3 = Employee('bill', 'chumba', 80047800)

# c.execute("INSERT INTO employees VALUES ('{}','{}', {})".format(emp_1.first, emp_1.last, emp_1.pay))

# c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_2.first, emp_2.last, emp_2.pay))
# # ### HERE U CAN COMMIT >>>>>>>>>>>>> conn.commit()

# ##### HERE WE USE PLACEHOLDERS TO TO INSERT THE :first, :last, :pay  ARE PLACEHOLDERS
# ###                                                               key >>  value
# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)",{'first': emp_3.first,'last': emp_3.last,'pay': emp_3.pay} )


# # #### PRINTINT  THE ??????  THING
# c.execute("SELECT * FROM employees WHERE last =?",('bungo',))
# print(c.fetchall())


# ######  PRINT THE PLACEHOLDERS
# c.execute("SELECT * FROM employees WHERE last =:last",{'last':'chumba'})
# print(c.fetchall())


# # # Fetch all rows and print them
# rows = c.fetchall()
# for row in rows:
#     print(row)
# conn.commit()
# conn.close()



import sqlite3
from employee import Employee

conn = sqlite3.connect(':memory:')
c = conn.cursor()

c.execute("""CREATE TABLE employees (
        first TEXT,
        last TEXT,
        pay INTEGER
    )""")

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp.first, emp.last, emp.pay))

def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last = :last", {'last': lastname})
    return c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay 
                     WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})

def remove_pay(emp):
    with conn:
        c.execute("DELETE FROM employees WHERE first = :first AND last = :last", {'first': emp.first, 'last': emp.last})

emp_1 = Employee('john', 'doe', 89787500000)
emp_2 = Employee('dan', 'kinuthia', 767800000)
emp_3 = Employee('dan', 'chebulopa', 8787600000)
emp_4 = Employee('dan', 'suiz', 8787600000)

insert_emp(emp_1)
insert_emp(emp_2)
insert_emp(emp_3)
insert_emp(emp_4)

result = get_emps_by_name("chumba")
print(result)

conn.close()
