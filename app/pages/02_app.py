import streamlit as st
import pandas as pd

# 입력
st.title('1. 입력 버튼들')
st.text('Fixed width text')
st.markdown('_Markdown_') # see #*
st.caption('Balloons. Hundreds of them...')
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')

# * optional kwarg unsafe_allow_html = True

data = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]    
)

# 출력
st.title('2. 출력 메서드들')
button_result = st.button('Hit me')
st.text(button_result)

if button_result == True:
    st.write(data)

st.data_editor(data)

check_result = st.checkbox('Check me out')
if check_result == True:
    st.write(data)
    
st.radio('Pick one:', ['nose','ear'])
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1,2,3,4])
st.text_input('Enter some text')
st.number_input('Enter a number')
st.text_area('Area for textual entry')
st.date_input('Date input')
st.time_input('Time entry')
st.file_uploader('File uploader')
st.download_button('On the dl', data=data.to_csv(), file_name='data.csv', mime='text/csv')
st.camera_input("一二三,茄子!")
st.color_picker('Pick a color')

name_list = ['쟈니', '후토마끼', '동']
address_list = ['https://i.imgur.com/AvCirS7.jpg', 
                'https://i.imgur.com/ZfMZBw0.jpg',
                'https://i.imgur.com/fuTQgqp.jpg'
                ]
search = st.text_input("검색어를 입력하세요.")
if search in name_list:
    img_index = name_list.index(search)
    st.image(address_list[img_index])