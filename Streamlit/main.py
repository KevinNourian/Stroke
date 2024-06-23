import streamlit as st
import pandas as pd
import numpy as np

table1 = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [10, 20, 30, 40]})

st.title("Hello World. This is streamlit.")

st.header("This is a header")

st.subheader("This is a subheader")

st.text("This is a text")

st.markdown("**This is a markdown**")

st.markdown("*This is a markdown*")

st.markdown("~~This is a markdown~~")   

st.caption("This is a caption")

st.code("print('Hello World')")

st.write('## H2 Heading')

st.table(table1)

st.dataframe(table1)


# Diisplaying a dataframe without uisng st.write()
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})
df

# Highlights some of the cells in the dataframe
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))


# Displaying code with syntax highlighting
code = '''
def hello():
    print('This is a function')
'''
st.code(code, language ='python')

# Draw a line chart
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


st.text_input("Your name", key="name")

# Creates a text input box for the user to enter their name
st.session_state.name


# Creates a checkbox for the user to check if they want to see the dataframe
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option


# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)


# Update the progress bar with each iteration.
import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'