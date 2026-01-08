import streamlit as slt
from connection import conn


slt.title("Registration Form")
id=slt.text_input("Enter the RegisterID")
name=slt.text_input("Enter your Name")
email=slt.text_input("Enter your Email")
city=slt.text_input("Enter your City")

col1,col2,col3,col4,col5=slt.columns(5)

with col1:
     button=slt.button("Submit")
with col2:
     u_btn=slt.button("Update",key=f"update_{id}")
with col3:
     u_del=slt.button("Delete")
with col4:
     next=slt.button("View Data")
with col5:
     enroll=slt.button("Enroll")

cur=conn.cursor()
if (button):
    cur.execute("insert into register(r_id,fname,email,city) values(%s,%s,%s,%s)", (id,name,email,city))
    conn.commit()
    slt.success("User Added successfully!")

if (u_btn):
    cur.execute("update register set fname=%s,email=%s,city=%s where r_id=%s",(name,email,city,id))
    conn.commit()
    slt.success("User updated successfully!")

if (u_del):
    cur.execute("delete from register where r_id=%s",(id,))
    conn.commit()
    slt.success("User deleted successfully!")



if next:
    slt.switch_page("pages/Data.py")

if enroll:
    slt.switch_page("pages/Enroll.py")

