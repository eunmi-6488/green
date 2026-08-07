import streamlit as st
import time
import random
import session_two

st.header('st.session_state 세션 테스트')
def main():
    if 'user_list' not in st.session_state:
        st.session_state.user_list = []

    userkey = st.text_input('추가할 ID입력 하세요')
    if st.button('ID 추가하기'):
        if userkey:
            st.session_state.user_list.append(userkey)
            st.success(f'{userkey} 추가 완료 성공했습니다')

    st.divider()
    st.write('### 현재 누적된 세션리스트 목록')
    st.write(st.session_state.user_list)

    st.divider()
    session_two.order() #함수호출

main() #함수에서 세션기술

@st.cache_data
def slow_cal(x):
    '''
    같은 x값이 들어오면 저장된 결과를 사용한다.
    처음 입력된 값일 때면 3초만 동안 기다린다
    '''
    time.sleep(1)
    cal = x*100
    return cal

dice = [1,2,3,4,5,6]
pick = random.choice(dice)
st.write('pick = ',pick)
result = slow_cal(pick)
st.write('slow_cal(x)함수 결과 = ' , result)
# (.venv) C:\~~> streamlit run session_first.py










