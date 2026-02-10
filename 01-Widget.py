import streamlit as st

import os, time


print(f"✅ {os.path.basename(__file__)} 실행됨 {time.strftime('%Y-%m-%d %H:%M:%S')}")

st.title("다양한 widget들")

model = st.selectbox(
    "모델 선택", 
    ("GPT-3", "GPT-4", "GPT-5"))

st.markdown(f"model: green[{model}]")

name = st.text_input("이름이 뭡니까?")
st.markdown(f"이름 : red[{name}]")

value = st.slider(label="temperature",
            min_value=0.1, max_value=1.0)
st.markdown(f"value: :violet[{value}]")

if value > 0.4:
    st.write("다양성이 높은 모델")
else:
    st.write("정형화된 답변을 하는 모델")
    st.text_input("질문을 입력해보세요")

button = st.button("버튼을 눌러보세요")
if button:
    st.write(":blue[버튼] 이 눌렸습니다 :sparkles:")

st.markdown('---')
num1 = st.number_input('숫자1 입력', 
    min_value=10, max_value=100, step=5)    

num2 = st.number_input('숫자2 입력', 
    min_value=10, max_value=100, step=5)        

btn_calc = st.button('계산을 합니다')

if btn_calc:
    st.markdown(f"""
            {num1} + {num2} = {num1 + num2}

            {num1} - {num2} = {num1 - num2}
             """)