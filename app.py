import streamlit as st
import plotly.express as px
from streamlit.file_util import file_is_in_folder_glob

st.set_page_config(layout="wide")

col1, col2, col3 = st.columns([5,5,20])

with col3:
    st.title("My First Streamlit App")

year_col, continent_col, log_x_col = st.columns([5,5,5])

with year_col:
    year_choice = st.slider(
        "Year",
        min_value=1950,
        max_value=2007,
        step=1,
        value=2007
    )

with continent_col:
    continent_choice = st.selectbox(
        "Continent",
        ('All','Asia','Europe','Africa','Americas','Oceania')
    )

with log_x_col:
    log_x_choice = st.checkbox("Log X axis?")

df = px.data.gapminder()
filtered_df = df.copy()

if continent_choice != "All":
    filtered_df = filtered_df[filtered_df.continent == continent_choice]

fig = px.scatter(
    filtered_df[filtered_df.year == year_choice],
    x = "gdpPercap",
    y = "lifeExp",
    size = "pop",
    color = "continent",
    hover_name = "country",
    log_x=log_x_choice,
    size_max=60
)

fig.update_layout(title = "GDP per Capita vs Life Expectancy")
st.plotly_chart(fig, use_container_width=True)