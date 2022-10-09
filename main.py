# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

st.title('测试标题')

# st.write('表格绘制')
# df = pd.DataFrame(
#     {
#         '第一组': np.random.rand(10),
#         '第二组': np.random.rand(10)
#     }
# )
#
# st.write(df)
#
# dataframe = pd.DataFrame(
#     np.random.randn(10, 20),
#     columns=('col %d' % i for i in range(20)))
#
# st.table(dataframe)
# st.dataframe(dataframe.style.highlight_max(axis=0))
###################################################
# st.header('st.button 按键展示')
# if st.button('你好'):
#     st.write('点了')
# else:
#     st.write('没点')
###################################################
st.header('st.write')
st.write('Hello, *World!* :sunglasses:')
st.write(1234)
df = pd.DataFrame(
    {
        '第一行': [1, 2, 3, 4],
        '第二行': [10, 20, 30, 40]
    }
)
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
st.write(df2)
c = alt.Chart(df2).mark_circle().encode(x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

