import streamlit as st
import pandas as pd
import plotly.express as px

# se llama el dataset y se guarda
df_vg = pd.read_csv('vg_sales.csv')

st.header('Sales of Video Games')

# crear casillas de verificación
hist_check_year_rel = st.checkbox(
    'Construir histograma para año de lanzamiento')
hist_check_critic = st.checkbox(
    'Construir histograma para calificación de la crítica')
line_check_sales_year_region = st.checkbox(
    'Construir gráfico de líneas para ventas por año y región')
bar_check_sales_platform = st.checkbox(
    'Construir gráfico de barras para ventas por plataforma y región')
bar_check_sales_genre = st.checkbox(
    'Construir gráfico de barras para ventas por género y región')
scatter_check_na = st.checkbox(
    'Construir gráfico de dispersión para crítica y ventas en Norte América')
scatter_check_eu = st.checkbox(
    'Construir gráfico de dispersión para crítica y ventas en Europa')
scatter_check_jp = st.checkbox(
    'Construir gráfico de dispersión para crítica y ventas en Japón')

# al hacer clic en el botón
if hist_check_year_rel:
    st.write(
        'Creación de un histograma para la columna de año de lanzamiento del conjunto de datos de videojuegos')
    # se crea un histogrma
    fig = px.histogram(df_vg,
                       x='year_of_release',
                       title='Distribution of Videogames by Year of Release',
                       labels={'year_of_release': 'Year of Release'}
                       )

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if hist_check_critic:
    st.write(
        'Creación de un histograma para la columna de calificación de crítica del conjunto de datos de videojuegos')
    # se crea un histogrma
    fig = px.histogram(df_vg,
                       x='critic_score',
                       title='Distribution of Video Games by Critic Score',
                       labels={'critic_score': 'Critic Score'}
                       )

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if line_check_sales_year_region:
    st.write(
        'Creación de un gráfico de líneas para las columnas de ventas por región del conjunto de datos de videojuegos')
    # Ventas por año para cada región
    sales_by_year = df_vg.groupby('year_of_release')[
        ['na_sales', 'eu_sales', 'jp_sales']].agg('sum')

    # se crea gráfico de líneas
    fig = px.line(sales_by_year,
                  y=['na_sales', 'eu_sales', 'jp_sales'],
                  title='Sum of Sales by Year',
                  labels={
                      'value': 'Sum of Sales (in millions)', 'year_of_release': 'Year of Release', 'variable': 'Region'}
                  )

    fig.update_traces(
        name='North America',  # Cambiar el nombre de la primera línea de la leyenda
        selector=dict(name='na_sales')
    )

    fig.update_traces(
        name='Europe',  # Cambiar el nombre de la segunda línea de la leyenda
        selector=dict(name='eu_sales')
    )

    fig.update_traces(
        name='Japan',  # Cambiar el nombre de la tercera línea de la leyenda
        selector=dict(name='jp_sales')
    )

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if bar_check_sales_platform:
    st.write(
        'Creación de un gráfico de barras para las columnas de ventas por plataforma para cada región del conjunto de datos de videojuegos')
    # Ventas por plataforma para cada región
    platform_sales = df_vg.groupby(
        'platform')[['na_sales', 'eu_sales', 'jp_sales']].agg('sum')

    # se crea un gráfico de barras
    fig = px.bar(platform_sales,
                 y=['na_sales', 'eu_sales', 'jp_sales'],
                 title='Sum of Sales by Platform',
                 labels={
                     'value': "Sum of Sales (in millions)", 'variable': 'Region'}
                 )

    fig.update_traces(
        name='North America',  # Cambiar el nombre de la primera línea de la leyenda
        selector=dict(name='na_sales')
    )

    fig.update_traces(
        name='Europe',  # Cambiar el nombre de la segunda línea de la leyenda
        selector=dict(name='eu_sales')
    )

    fig.update_traces(
        name='Japan',  # Cambiar el nombre de la tercera línea de la leyenda
        selector=dict(name='jp_sales')
    )

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


if bar_check_sales_genre:
    st.write(
        'Creación de un gráfico de barras para las columnas de ventas por género para cada región del conjunto de datos de videojuegos')
    # Ventas por género para cada región
    genre_sales = df_vg.groupby(
        'genre')[['na_sales', 'eu_sales', 'jp_sales']].agg('sum')

    # se crea un gráfico de barras
    fig = px.bar(genre_sales,
                 y=['na_sales', 'eu_sales', 'jp_sales'],
                 title='Sum of Sales by Genre',
                 labels={
                     'value': "Sum of Sales (in millions)", 'variable': 'Region'},
                 barmode='group')

    fig.update_traces(
        name='North America',  # Cambiar el nombre de la primera línea de la leyenda
        selector=dict(name='na_sales')
    )

    fig.update_traces(
        name='Europe',  # Cambiar el nombre de la segunda línea de la leyenda
        selector=dict(name='eu_sales')
    )

    fig.update_traces(
        name='Japan',  # Cambiar el nombre de la tercera línea de la leyenda
        selector=dict(name='jp_sales')
    )

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if scatter_check_na:
    st.write(
        'Creación de gráfico de dispersión de  critica y las ventas en Norte América, para el conjunto de datos de venta de videojuegos')
    # se crea gráfico de dispersión
    fig = px.scatter(df_vg, x='critic_score', y='na_sales',
                     title='Scatter Plot',
                     labels={
                         'na_sales': "Sales in North America (in millions)", 'critic_score': 'Critic Score'}
                     )

    # mostrar un gráfico Plotly interactivo de gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True)

if scatter_check_eu:
    st.write(
        'Creación de gráfico de dispersión de  critica y las ventas en Europa, para el conjunto de datos de venta de videojuegos')
    # se crea gráfico de dispersión
    fig = px.scatter(df_vg, x='critic_score', y='eu_sales',
                     title='Scatter Plot',
                     labels={
                         'eu_sales': "Sales in Europe (in millions)", 'critic_score': 'Critic Score'}
                     )
    # mostrar un gráfico Plotly interactivo de gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True)

if scatter_check_jp:
    st.write(
        'Creación de gráfico de dispersión de  critica y las ventas en Japón, para el conjunto de datos de venta de videojuegos')
    # se crea gráfico de dispersión
    fig = px.scatter(df_vg, x='critic_score', y='jp_sales',
                     title='Scatter Plot',
                     labels={
                         'jp_sales': "Sales in Japan (in millions)", 'critic_score': 'Critic Score'}
                     )
    # mostrar un gráfico Plotly interactivo de gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True)
