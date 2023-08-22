import streamlit as st
import modules.functions as fc
from modules.global_variables import todo_list, box

st.title("My ToDo App")

st.subheader("Subheader hehe")

st.write("a lot of text")

filepath = "todos_web.txt"

fc.read_todo_list(filepath)

for todo in todo_list:
    st.checkbox(todo)

st.text_input(label="Enter a ToDo:", placeholder="Add new ToDo...")


