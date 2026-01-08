from connection import conn
import pandas as pd
import Home as d
import streamlit as slt


slt.title("Student Information")

d.cur.execute("select * from register")
rows=d.cur.fetchall()
df=pd.DataFrame(rows,columns=["id","Name","Email","City"])
slt.table(df)
slt.title("Course Information")
d.cur.execute("select * from course")
rows=d.cur.fetchall()
df=pd.DataFrame(rows,columns=["CourseId","RegisterId","Course Name","Date","Price"])
slt.table(df)

col1,col2=slt.columns(2)

with col1:
    inner_join=slt.button("Inner Join")


if inner_join:
    d.cur.execute("select * from register r inner join course c on r.r_id=c.r_id")
    rows=d.cur.fetchall()
    df1=pd.DataFrame(rows,columns=["RegisterId","Name","Email","City","CourseID","RID","Course Name","Date","Price"])
    slt.table(df1)


d.cur.execute("select fname,count(c_id) from register r join course c on r.r_id=c.r_id group by fname")
rows=d.cur.fetchall()
df3=pd.DataFrame(rows,columns=["Name","No. of Course Enrolled"])
slt.table(df3)