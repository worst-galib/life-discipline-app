import streamlit as st
import datetime
import random

st.set_page_config(page_title="Life Discipline Dashboard", layout="centered")

if 'tasks' not in st.session_state:
    st.session_state.tasks = []
if 'goal' not in st.session_state:
    st.session_state.goal = ""
if 'progress' not in st.session_state:
    st.session_state.progress = 0

quotes = [
    "Discipline is choosing between what you want now and what you want most.",
    "Small steps every day lead to big results.",
    "Success is nothing more than a few simple disciplines practiced daily.",
    "Wake up with determination, go to bed with satisfaction.",
    "The secret to your future is hidden in your daily routine."
]

st.title("Your Life Discipline Dashboard")
st.subheader(f"Today: {datetime.date.today().strftime('%A, %d %B %Y')}")
st.success(random.choice(quotes))

st.header("Your Main Goal")
goal_input = st.text_input("Set or update your main goal:", st.session_state.goal)
if goal_input:
    st.session_state.goal = goal_input
    st.success(f"Your goal is: {goal_input}")

progress = st.slider("Progress toward your goal (%)", 0, 100, st.session_state.progress)
st.session_state.progress = progress
st.progress(progress / 100)

st.header("Today's To-Do List")
new_task = st.text_input("Add a new task")
if st.button("Add Task") and new_task:
    st.session_state.tasks.append({"task": new_task, "done": False})

for i, task in enumerate(st.session_state.tasks):
    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        task_done = st.checkbox(task['task'], value=task['done'], key=i)
        st.session_state.tasks[i]['done'] = task_done
    with col2:
        if st.button("❌", key=f"del_{i}"):
            st.session_state.tasks.pop(i)
            st.experimental_rerun()

st.header("Decision Helper")
decision_question = st.text_area("What's your decision problem?")
if st.button("Get Suggestion") and decision_question:
    st.info("Think logically. What are the pros and cons? Here's a tip:")
    st.write("Ask yourself: Will this decision bring you closer to your main goal or take you away from it?")

st.caption("Created by Soat's AI Discipline Bot")
