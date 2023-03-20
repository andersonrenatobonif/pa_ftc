import streamlit as st
from PIL import Image
import folium
import pandas as pd
from streamlit_folium import folium_static



st.set_page_config(
    page_title='Home',
    page_icon='📈',
    layout='wide'
    
)


# Data load

df = pd.read_csv('zomato1.csv')

df1 = df.copy()

# image_path = 'C:/Users/anderson.bonifacio_i/Desktop/Dados/cds/FTC/pa_/'
image = Image.open('logo.png')

st.sidebar.image(image, width=120)

st.sidebar.markdown( '# Food Company')
st.sidebar.markdown( '## Fastest Delivery in Town')
st.sidebar.markdown( """_ _ _ """)

st.write(' # Bem vindo ao Food Company Growth Dashboard ')
st.write('#### Navegue na barra lateral e utilize os filtros para ver as métricas da empresa em seus principais indicadores')

#st.sidebar.markdown( '## Filtros')

country_options = st.sidebar.multiselect(
    'Escolha os Paises que Deseja visualizar as Informações',
    ['Philippines', 'Brazil', 'Australia', 'United States of America',
     'Canada', 'Singapure', 'United Arab Emirates', 'India',
     'Indonesia', 'New Zeland', 'England', 'Qatar', 'South Africa',
     'Sri Lanka', 'Turkey'],
    default=['England', 'Turkey', 'South Africa', 'Singapure', 'Brazil', 'Australia' ])

st.sidebar.markdown("""_ _ _ """)
st.sidebar.markdown('### Powered by Anderson Bonifácio')

#filtro países

linhas_selecionadas = df1['country'].isin(country_options)
df1 = df1.loc[linhas_selecionadas, :]



# ======================
# Mapa
# ======================
st.caption("<h3 style='text-align: center; color: white;'>Localização das lojas no mapa</h3>", unsafe_allow_html=True)
map_chart = (df1.loc[:, ['city', 'longitude', 'latitude', 'country', 'aggregate_rating', 'restaurant_name'] ].
             groupby(['city', 'aggregate_rating', 'country', 'restaurant_name']).median().reset_index())

map_chart = (map_chart.rename(columns = {'city' : "Cidade", 
                                           'aggregate_rating' : 'Avaliação Média',  
                                           'country' : 'País',
                                           'restaurant_name': 'Nome'}))


map = folium.Map()

for index, location_info in map_chart.iterrows():
    folium.Marker([location_info['latitude'],
                  location_info['longitude']],
                 popup=location_info[['Cidade', 'País', 'Avaliação Média', 'Nome' ]]).add_to(map)
    
folium_static(map, width=900 , height=600)
