import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title('Hello Streamlit')

# Text Display
st.write('This is a simple text')

df = pd.DataFrame({
    'Person': ['A', 'B', 'C', 'D'],
    'Age': [10, 20, 30, 40]
})

# Display DataFrame
st.write("Here is the dataframe")
st.write(df)

# Create a line chart
chart_data = pd.DataFrame(
    np.random.rand(20, 3), columns=['a', 'b', 'c']
)
st.line_chart(chart_data)