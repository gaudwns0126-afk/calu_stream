import streamlit as st

st.set_page_config(page_title="Assignment 7 Calculator", layout="centered")
# secrets.toml에 사용자 시크릿 정보 있으면 게시 (디폴트는 1234)
try:
    SECRET_KEY = st.secrets["secret_key"]
except Exception:
    SECRET_KEY = "1234"

if "calc_input" not in st.session_state:
    st.session_state.calc_input = "0"

def add_char(char):
    if st.session_state.calc_input == "0" and char not in [".", "+", "-", "*", "/"]:
        st.session_state.calc_input = char
    else:
        st.session_state.calc_input += char

def clear_all():
    st.session_state.calc_input = "0"

def delete_char():
    if len(st.session_state.calc_input) > 1:
        st.session_state.calc_input = st.session_state.calc_input[:-1]
    else:
        st.session_state.calc_input = "0"

def calculate():
    # 기타 예외 처리 및 계산 내장 함수.
    try:
        res = eval(st.session_state.calc_input, {"__builtins__": None}, {})
        if isinstance(res, float) and res.is_integer():
            res = int(res)
        st.session_state.calc_input = str(res)
    except Exception:
        st.session_state.calc_input = "Error"

st.title("Assignment 7 Calculator")
st.caption(f"Loaded Secret Info: {SECRET_KEY}")

st.text_input("Result", value=st.session_state.calc_input, disabled=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button("7", on_click=add_char, args=("7",))
    st.button("4", on_click=add_char, args=("4",))
    st.button("1", on_click=add_char, args=("1",))
    st.button("0", on_click=add_char, args=("0",))

with col2:
    st.button("8", on_click=add_char, args=("8",))
    st.button("5", on_click=add_char, args=("5",))
    st.button("2", on_click=add_char, args=("2",))
    st.button(".", on_click=add_char, args=(".",))

with col3:
    st.button("9", on_click=add_char, args=("9",))
    st.button("6", on_click=add_char, args=("6",))
    st.button("3", on_click=add_char, args=("3",))
    st.button("=", on_click=calculate)

with col4:
    st.button("+", on_click=add_char, args=("+",))
    st.button("-", on_click=add_char, args=("-",))
    st.button("*", on_click=add_char, args=("*",))
    st.button("/", on_click=add_char, args=("/",))
    st.button("C", on_click=clear_all)
    st.button("⌫", on_click=delete_char)