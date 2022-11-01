import streamlit as st
import random
import altair as alt
import numpy as np
import pandas as pd


st.header('Homework 1')

st.markdown(
"**QUESTION 1**: In previous homeworks you created dataframes from random numbers.\n"
"Create a datframe where the x axis limit is 100 and the y values are random values.\n"
"Print the dataframe you create and use the following code block to help get you started"
)



x_limit = 100

# List of values from 0 to 100 each value being 1 greater than the last
x_axis = np.arange(0, x_limit, 1)

# Create a random array of data that we will use for our y values
y_data = [random.random() for value in x_axis]

df = pd.DataFrame({'x_axis': x_axis,
                     'y_data': y_data})
st.write(df)


st.markdown(
"**QUESTION 2**: Using the dataframe you just created, create a basic scatterplot and Print it.\n"
"Use the following code block to help get you started."
)

scatter = alt.Chart(df).mark_point().encode(
    x="x_axis:Q",
    y="y_data:Q"
)

st.altair_chart(scatter, use_container_width=True)


st.markdown(
"**QUESTION 3**: Lets make some edits to the chart by reading the documentation on Altair.\n"
"https://docs.streamlit.io/library/api-reference/charts/st.altair_chart.  "
"Make 5 changes to the graph, document the 5 changes you made using st.markdown(), and print the new scatterplot.  \n"
"To make the bullet points and learn more about st.markdown() refer to the following discussion.\n"
"https://discuss.streamlit.io/t/how-to-indent-bullet-point-list-items/28594/3"
)


st.markdown("""
The 5 changes I made were: changed the color to red, changed the width and height, added a title, added opacity, and removed the grid. 
- Change 1 """)

scatter = alt.Chart(df).mark_point().encode(
    x="x_axis:Q",
    y="y_data:Q"
).configure_mark(color="red")

st.altair_chart(scatter, use_container_width=True)

st.markdown("""
- Change 2
""")

scatter = alt.Chart(df).mark_point().encode(
    x="x_axis:Q",
    y="y_data:Q"
).configure_mark(color="red"
).properties(width=300, height=600)

st.altair_chart(scatter, use_container_width=True)




st.markdown("""
- Change 3
""")

scatter = alt.Chart(df).mark_point().encode(
    x="x_axis:Q",
    y="y_data:Q"
).configure_mark(color="red"
).properties(width=300, height=600
).properties(title='Random Scatter Plot')

st.altair_chart(scatter, use_container_width=True)






st.markdown("""
- Change 4
""")


scatter = alt.Chart(df).mark_point().encode(
    x="x_axis:Q",
    y="y_data:Q"
).configure_mark(color="red", opacity=0.3
).properties(width=300, height=600
).properties(title='Random Scatter Plot')

st.altair_chart(scatter, use_container_width=True)






st.markdown("""
- Change 5
""")

scatter = alt.Chart(df).mark_point().encode(
    x="x_axis:Q",
    y="y_data:Q"
).configure_mark(color="red", opacity=0.3
).properties(width=300, height=600
).properties(title='Random Scatter Plot'
).configure_axis(
    grid=False
)

st.altair_chart(scatter, use_container_width=True)



st.markdown(
"**QUESTION 4**: Explore on your own!  Go visit https://altair-viz.github.io/gallery/index.html.\n "
"Pick a random visual, make two visual changes to it, document those changes, and plot the visual.  \n"
"You may need to pip install in our terminal for example pip install vega_datasets "
)

st.markdown("""
I'm using the simple heatmap.
The 2 changes I made were: changed the range to -8 to 8, and addded a title. 
""")



st.markdown("""
- Change 1
""")


x, y = np.meshgrid(range(-8, 8), range(-8, 8))
z = x ** 2 + y ** 2

source = pd.DataFrame({'x': x.ravel(),
                     'y': y.ravel(),
                     'z': z.ravel()})

heat=alt.Chart(source).mark_rect().encode(
    x='x:O',
    y='y:O',
    color='z:Q'
)
st.altair_chart(heat, use_container_width=True)




st.markdown("""
- Change 2
""")

x, y = np.meshgrid(range(-8, 8), range(-8, 8))
z = x ** 2 + y ** 2

source = pd.DataFrame({'x': x.ravel(),
                     'y': y.ravel(),
                     'z': z.ravel()})

heat=alt.Chart(source).mark_rect().encode(
    x='x:O',
    y='y:O',
    color='z:Q'
).properties(title='Cool HeatMap')
st.altair_chart(heat, use_container_width=True)
