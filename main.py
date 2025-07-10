import streamlit as st

st.write('---')
st.title('1.버튼')
st.write('---')

if st.button("클릭하세요"):
    st.write("버튼이 눌렸습니다!")

st.write('---')
st.title('2.체크박스')
st.write('---')

agree = st.checkbox("약관에 동의합니다.")
if agree :
    st.write("동의 감사합니다.")

st.write('---')
st.title('3.라디오버튼')
st.write('---')

mood = st.radio("오늘 기분이 어때요?",["행복","보통","슬픔"],index=1)
st.write(f"선택된 기분: {mood}")

st.write('---')
st.title('4.셀렉트박스')
st.write('---')

choice = st.selectbox("가장 좋아하는 과일을 선택하세요",["사과","바나나","체리"])
st.write(f"선택한 과일: {choice}")

st.write('---')
st.title('5.멀티셀렉트')
st.write('---')

fruits = st.multiselect("먹고 싶은 과일을 선택하세요",["사과","바나나","체리","포도"],default=["사과"])
st.write(f"선택된 과일: {fruits} ")

st.write('---')
st.title('6.슬라이더')
st.write('---')

age = st.slider("나이를 선택하세요",min_value=0,max_value=100,value=20)
height = st.slider("키 범위 선택",min_value=140.0,max_value=200.0,value=(160.0,180.0))

st.write('---')
st.title('7.더')
st.write('---')

name = st.text_input(label="이름을 입력하세요",placeholder="홍길동")
password = st.text_input(label="비밀번호",type="password",help="영문,숫자,특수문자 조합 8~16자",max_chars=16)
st.text_input(label="읽기 전용 필드",value="수정 불가",disabled=True)

st.write('---')
st.title('8.텍스트 영역')
st.write('---')

feedback = st.text_area("자유롭게 의션을 남겨주세요",height=150)

st.write('---')
st.title('9.숫자입력')
st.write('---')

score = st.number_input("점수를 입력하세요",min_value=0,max_value=100,value=50,step=5)

st.write('---')
st.title('10.날짜입력')
st.write('---')

from datetime import date
birthday = st.date_input("생년월일 선택")
period = st.date_input("기간 선택",value=[date(2025,1,1),date(2025,12,31)])

st.write('---')
st.title('11.시간입력')
st.write('---')

from datetime import time
wakeup = st.time_input("기상 시간을 선택하세요",value=time(7,30))

st.write('---')
st.title('12.컬러 피커')
st.write('---')

color = st.color_picker("테마 색상을 선택하세요",value="#00ff00")

st.write('---')
st.title('13.파일 업로드')
st.write('---')

uploaded_file = st.file_uploader("파일을 업로드하세요",type=["csv","xlsx"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

st.write('---')
st.title('16.폼')
st.write('---')

with st.form("my_form"):
    name = st.text_input("이름")
    age = st.number_input("나이",0,100)
    submitted = st.form_submit_button("제출")
if submitted:
    st.write(f"{name} ({age}세) 제출 완료!")

st.write('---')
st.title('17.획장 영역')
st.write('---')

with st.expander("추가 정보 보기",expanded=False):
    st.write("여기에 세부 정보를 넣어요.")
    st.text_input("나머지주소")

st.write('---')
st.title('18.스피너j')
st.write('---')

import time
with st.spinner("처리 중입니다..."):
      time.sleep(3)
st.success("완료!")

st.write('---')
st.title('19.프로그레스 바')
st.write('---')

import time
my_bar = st.progress(0)
for percent in range(100):
    time.sleep(0.05)
    my_bar.progress(percent + 1)

st.write('---')
st.title('20.컬럼 레이아웃')
st.write('---')

col1, col2 = st.columns(2)
with col1 :
    st.write("왼쪽 열")
with col2:
    st.write("오른쪽 열")

st.write('---')
st.title('21.사이드바')
st.write('---')

oprion = st.sidebar.selectbox("사이드바 메뉴",["홈","설정","정보"])

st.write('---')
st.title('22.상태 알림')
st.write('---')

st.success("성공 메세지")
st.info("정보")
st.warning("경고 메시지")
st.error("오류 메시지")
 
from streamlit_option_menu import option_menu
with st.sidebar :
    choice = option_menu("Menu",["페이지1","페이지2","페이지3"], icons=['house','kanban','bi bi-robot'], menu_icon="app-indicator",default_index=0)

