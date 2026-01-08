import streamlit as slt
from connection import conn

slt.title("Course Enroll")

r_id=slt.text_input("Register ID")
c_id=slt.text_input("Enter your Course Id")
cname=slt.text_input("Enter your Course Name")
date=slt.date_input("Date")
price=slt.text_input("Enter course price")

btn=slt.button("Enrolling...")

cur=conn.cursor()
if btn:
    cur.execute("insert into course(c_id,r_id,course_name,c_date,price) values(%s,%s,%s,%s,%s)",(c_id,r_id,cname,date,price))
    conn.commit()
    slt.success("User Enrolled successfully!")



