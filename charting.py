import plotly.express as px
import plotly.graph_objects as go
import folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster
import streamlit as st

@st.cache
def scatter_plotly(df,oceancolor,projection_type,scope,coastlinecolor,coastlinewidth,framecolor,framewidth,landcolor,bgcolor):

    ''' create scatter map with plotly'''

    scatter_map = px.scatter_geo(df, 'latitude', 'longitude', color = 'category_long', hover_name = 'Name')

    scatter_map.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)')

    scatter_map.update_traces(line = dict(color = '#FF1801'))

    scatter_map.update_geos(showocean = True,
                    oceancolor = oceancolor,
                    projection_type= projection_type,
                    scope = scope,
                    coastlinecolor = coastlinecolor,
                    coastlinewidth = coastlinewidth,
                    framecolor = framecolor,
                    framewidth = framewidth,
                    landcolor = landcolor,
                    bgcolor = bgcolor)

    return scatter_map

@st.cache
def chloro_plotly(df,oceancolor1,projection_type1,scope1,coastlinecolor1,coastlinewidth1,framecolor1,framewidth1,landcolor1,bgcolor1):

    fig = px.choropleth(df, locations="Country", locationmode = 'country names',
                    color="Name",
                    projection = 'orthographic',
                    color_continuous_scale=px.colors.sequential.Blues)
    
    fig.update_geos(showocean = True,
                    oceancolor = oceancolor1,
                    projection_type= projection_type1,
                    scope = scope1,
                    coastlinecolor = coastlinecolor1,
                    coastlinewidth = coastlinewidth1,
                    framecolor = framecolor1,
                    framewidth = framewidth1,
                    landcolor = landcolor1,
                    bgcolor = bgcolor1)    
    return fig


@st.cache
def mapbox_map(df,mapbox_styles):

    mapbox = px.scatter_mapbox(df, lat="latitude", lon="longitude", hover_name="Name", color = 'category_long', zoom = 0)

    mapbox.update_layout(mapbox_style = mapbox_styles,
                    height = 500,
                    width = 600)
    
    return mapbox

def folium_map(df,tiles):

    marker_cluster = MarkerCluster()
    site_map = folium.Map(width=700,height=350,location=[39.949610, -75.150282],zoom_start=1, control_scale=True, tiles = tiles)

    for i in range(df.shape[0]):
        marker = folium.Marker(location = (df.iloc[i]['latitude'],
                                        df.iloc[i]['longitude']),
                            popup = df.iloc[i]['Name'],
                            icon=folium.features.CustomIcon('https://i.imgur.com/HxrlEwn.png',icon_size=(40,40))).add_to(marker_cluster)
    
    site_map.add_child(marker_cluster)

    return site_map