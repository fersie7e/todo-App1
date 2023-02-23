import streamlit as st
import model

todos = model.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    model.set_todos(todos)
    st.session_state["new_todo"] = ""


st.title("Lista de Compra")
st.subheader("Miriam y Fernando")
st.write("07/07/07")



for index, item in enumerate(todos):
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        todos.pop(index)
        model.set_todos(todos)
        del st.session_state[item]
        st.experimental_rerun()

st.text_input(label=" ", label_visibility='hidden', placeholder='Add new todo...',
              on_change=add_todo, key='new_todo')
