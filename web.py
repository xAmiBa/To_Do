import streamlit as st
import modules.functions as fc
from modules.global_variables import todo_list
import random as ran

st.title("My ToDo App")
st.subheader("Create & store your todo lists!")
#st.write("a looooot of text")
filepath = "todos_web.txt"
fc.read_todo_list(filepath)

#FUNCTIONS:
def add_todo():
    todo = st.session_state["new_todo"]
    todo_list.append(todo)
    fc.reset_txt_list(filepath, todo_list)
    pass

key = ran.randint(1, 100)
for todo in todo_list:
    st.checkbox(todo, key, f"checkbox {key}")
    key = key + 1
# for todo in todo_list:
#     key = key + 1
#     st.checkbox(todo, key=f"checkbox{key}")

st.text_input(label="Add ToDo", placeholder="Add new ToDo...", on_change=add_todo, key="new_todo")


