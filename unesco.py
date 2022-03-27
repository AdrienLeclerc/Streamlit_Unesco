import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster
from charting import *


px.set_mapbox_access_token("pk.eyJ1IjoiYWRyaWVuLWxlY2xlcmMiLCJhIjoiY2t4ZGhvcnExMHM3ajJvbW1xY3plYm5pOSJ9.GGUXThlnQKPJ-FO-Kmv4Kw")

st.set_page_config(page_title = "Unesco Heritage Sites",
                   page_icon = ":planet:",
                   layout = 'wide')

@st.cache
def load_sites():

    sites = pd.read_csv("data/UNESCO.csv")

    return sites

sites = load_sites()
chloro = sites.groupby('Country name').count()
chloro['Country'] = chloro.index


st.sidebar.image("images/unesco.png")

navigation = st.sidebar.radio("Navigation", ('Plotly','Mapbox', 'Folium'))

st.sidebar.image("images/logo.png")

if navigation == 'Plotly':

    st.image("images/scatter_plotly.png")

    col1, col2, col3 = st.columns([1,4,1])

    with col1: 
        projection_type = st.selectbox("Type de projection", options = ('equirectangular', 'mercator', 'orthographic', 'natural earth', 'kavrayskiy7', 'miller', 'robinson', 'eckert4', 'azimuthal equal area', 'azimuthal equidistant', 'conic equal area', 'conic conformal', 'conic equidistant', 'gnomonic', 'stereographic', 'mollweide', 'hammer', 'transverse mercator', 'albers usa', 'winkel tripel', 'aitoff', 'sinusoidal'), index = 2)
        bgcolor = st.color_picker("Bg Color", value = '#0E1117')
        oceancolor = st.color_picker("Ocean Color", value = '#0E1117')
        landcolor = st.color_picker("Land Color", value = '#FFFFFF')
        framewidth = st.slider("Frame Width", min_value = 0, max_value = 10, value = 2, step = 1)
        
    with col3:
        scope = st.selectbox("Scope", options = ( "africa" , "asia" , "europe" , "north america" , "south america" , "usa" , "world" ), index = 6)
        coastlinecolor = st.color_picker("Coastline Color", value = '#0E1117')
        framecolor = st.color_picker("Frame Color", value = '#FFFFFF')
        coastlinewidth = st.slider("Coastline Width", min_value = 0, max_value = 10, value = 2, step = 1)


    with col2:

        st.plotly_chart(scatter_plotly(sites,oceancolor,projection_type,scope,coastlinecolor,coastlinewidth,framecolor,framewidth,landcolor,bgcolor), use_container_width = True)

    st.image("images/chloro_plotly.png")

    col1, col2, col3 = st.columns([1,4,1])

    with col1: 
        projection_type1 = st.selectbox("Type de projection", options = ('equirectangular', 'mercator', 'orthographic', 'natural earth', 'kavrayskiy7', 'miller', 'robinson', 'eckert4', 'azimuthal equal area', 'azimuthal equidistant', 'conic equal area', 'conic conformal', 'conic equidistant', 'gnomonic', 'stereographic', 'mollweide', 'hammer', 'transverse mercator', 'albers usa', 'winkel tripel', 'aitoff', 'sinusoidal'), index = 2, key = 1)
        bgcolor1 = st.color_picker("Bg Color", value = '#0E1117', key = 1)
        oceancolor1 = st.color_picker("Ocean Color", value = '#0E1117', key = 1)
        landcolor1 = st.color_picker("Land Color", value = '#FFFFFF', key = 1)
        framewidth1 = st.slider("Frame Width", min_value = 0, max_value = 10, value = 2, step = 1, key = 1)
        
    with col3:
        scope1 = st.selectbox("Scope", options = ( "africa" , "asia" , "europe" , "north america" , "south america" , "usa" , "world" ), index = 6, key = 1)
        coastlinecolor1 = st.color_picker("Coastline Color", value = '#0E1117', key = 1)
        framecolor1 = st.color_picker("Frame Color", value = '#FFFFFF', key = 1)
        coastlinewidth1 = st.slider("Coastline Width", min_value = 0, max_value = 10, value = 2, step = 1, key = 1)

    with col2:

        st.plotly_chart(chloro_plotly(chloro,oceancolor1,projection_type1,scope1,coastlinecolor1,coastlinewidth1,framecolor1,framewidth1,landcolor1,bgcolor1), use_container_width = True)

if navigation == 'Mapbox':

    st.image("images/scatter_mapbox.png")

    mapbox_styles = st.selectbox("Mapbox Style", options = ("open-street-map", "carto-positron", "carto-darkmatter", "stamen-terrain", "stamen-toner", "stamen-watercolor","basic", "streets", "outdoors", "light", "dark", "satellite", "satellite-streets"), index = 4)

    st.plotly_chart(mapbox_map(sites,mapbox_styles),use_container_width = True)

if navigation == 'Folium':

    st.image("images/cluster_folium.png")

    tiles = st.selectbox("Folium Tiles", options = ("OpenStreetMap", "Stamen Terrain", "Stamen Toner", "Stamen Water Color", "cartodbpositron", "cartodbdark_matter"), index = 2)

    folium_static(folium_map(sites,tiles),width=700,height=350)
