import streamlit as st

def order():
    st.write('-------------- session_two.py문서  order() --------------')
    if 'user_list'  in st.session_state:
        st.info(f'저장된 총 세션갯수: {len(st.session_state.user_list)}개')
        st.write('세션목록', st.session_state.user_list)
    else:
        st.write('세션목록에 없습니다')