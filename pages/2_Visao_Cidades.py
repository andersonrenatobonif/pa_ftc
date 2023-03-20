# libraries

import pandas as pd
import inflection
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
from PIL import Image

st.set_page_config(page_title='Visão Cidades', page_icon='🗺️', layout='wide')


# =======================================
# Funções
# =======================================

# Top 10 Restaurantes por cidade
def id_city(df1):
    df1_id_city = df1.loc[:, ['restaurant_id', 'country', 'city']].groupby(['city', 'country']).count().sort_values(by='restaurant_id', ascending=False).reset_index()

    city_chart = px.bar(
        df1_id_city.head(10), x='city', y='restaurant_id', color='country',
        labels={'restaurant_id': 'Quantidade de Restaurantes', 'city': 'Cidades'})
    
    return city_chart


# 7 cidade com restaurantes com mais avaliações
def votes_city(df1):
    df1_votes_city  = df1.loc[:, ['country', 'votes', 'city']].groupby(['city', 'country']).sum().sort_values(by='votes', ascending=False).reset_index()
    rate_chart = px.bar(df1_votes_city.head(7), x= 'city', y='votes' , 
                        labels= {'city' : 'Cidades', 'votes' : 'Avaliações' })
    
    
    return rate_chart



# 7 cidade com restaurantes com avaliações acima de 4.5
def rate_city(df1):
    rat_max_4_5 = df1[df1.loc[:, 'aggregate_rating'] >= 4.5]
        
    df1_rate_city = df1.loc[:, ['restaurant_id', 'country', 'city']].groupby(['city', 'country']).count().sort_values(by='restaurant_id', ascending=False).reset_index()
        
    price_chart = px.bar(df1_rate_city.head(7), x='city', y='restaurant_id',
                        labels= {'city' : 'Cidades', 'restaurant_id' : 'Quantidade de Restaurantes' })
    
    return price_chart



# 10 cidade com mais quantidade de tipo de culinária distinto   
def cuisines_city(df1):
    df1_city_cuisines = df1.loc[:, ['city', 'country', 'cuisines']].groupby(['city', 'country']).nunique().sort_values(by='cuisines', ascending=False).reset_index()

    city_chart = px.bar(df1_city_cuisines.head(10), x='city', y='cuisines', color='country', 
                        labels = {'city' : 'Cidades', 'cuisines' : 'Culinárias'})
    
    return city_chart





# Data load

df = pd.read_csv('zomato1.csv')

df1 = df.copy()



# =======================================
# Barra Lateral
# =======================================

st.title('Visão Cidades')

image = Image.open( 'logo.png')

st.sidebar.image(image, width=120)

st.sidebar.markdown( '# Food Company')
st.sidebar.markdown( '## Fastest Delivery in Town')
st.sidebar.markdown( """_ _ _ """)

st.sidebar.markdown( '## Filtros')

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


# =======================================
# Layout Streamlit
# =======================================




with st.container():
    # Top 10 Restaurantes por cidade
    st.caption("<h3 style='text-align: center; color: grey;'>Top 10 cidades com mais restaurantes</h3>", unsafe_allow_html=True)
    city_chart = id_city(df1)
    st.plotly_chart(city_chart, use_container_width=True)
    
    
    

col1, col2 = st.columns(2, gap='large')
    
with col1:
# 7 cidade com restaurantes com mais avaliações

    st.caption("<h3 style='text-align: center; color: grey;'>7 cidades com restaurantes com mais avaliações</h3>", unsafe_allow_html=True)
    rate_chart = votes_city(df1)
    st.plotly_chart(rate_chart, use_container_width=True)
    
   
        
with col2:
    # 7 cidade com restaurantes com avaliações acima de 4.5
        
    st.caption("<h3 style='text-align: center; color: grey;'>7 cidades com restaurantes com avaliações acima de 4.5</h3>", unsafe_allow_html=True)
    price_chart = rate_city(df1)
    st.plotly_chart(price_chart, use_container_width=True)
        
              
    
with st.container():
        
# 10 cidade com mais quantidade de tipo de culinária distinto        
        
    st.caption("<h3 style='text-align: center; color: grey;'>10 cidade com mais quantidade de tipo de culinária distinto</h3>", unsafe_allow_html=True)
    cuisines_chart = cuisines_city(df1)
    st.plotly_chart(cuisines_chart, use_container_width=True)
       
        
        


        
