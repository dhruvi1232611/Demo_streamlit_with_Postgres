import streamlit as slt

slt.title("Square Counter App")
c = slt.number_input("enter the number")
slt.write("Square : ",c*c)