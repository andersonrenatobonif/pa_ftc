# libraries

import pandas as pd
import inflection
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st
from PIL import Image

st.set_page_config(page_title='Visão Países', page_icon='🌎', layout='wide')

# =======================================
# Funções
# =======================================



# Gráfico de barras quantidade de restaurantes por país
def country_id(df1):
              
    df1_country_id = df1.loc[:, ['restaurant_id', 'country']].groupby('country').count().reset_index()

    country_chart = px.bar(df1_country_id, x='country', y='restaurant_id',
                           labels={'restaurant_id': 'Quantidade de Restaurantes', 'country': 'Países'})
        
    return country_chart



# Gráfico de barras quantidade de cidades por país
def country_city(df1):
    df1_country_city = df1.loc[:, ['city', 'country']].groupby('country').nunique().reset_index()

    city_chart = px.bar(df1_country_city, x='country', y='city', labels = {'country' : 'País', 'city' : 'Cidade'})

    return city_chart


# Média da quantidade de avaliações feitas por país
def rate_country(df1):
    df1_country_rate = df1.loc[:, ['country', 'votes']].groupby('country').mean().reset_index()
            
    rate_chart = px.bar(df1_country_rate, x= 'country', y='votes',
                        labels= {'country' : 'País', 'votes' : 'Avaliações' })
    
    rate_chart.update_layout(barmode='group', xaxis_tickangle=45)
            
    return rate_chart
            

# Média do preço do prato para duas pessoas separados por país
def country_price(df1):    
        df1_country_price = df1.loc[:, ['average_cost_for_two', 'country']].groupby('country').mean().round(2).reset_index()
            

        price_chart = px.bar(df1_country_price, x='country', y='average_cost_for_two', 
                             labels= {'country' : 'País', 'average_cost_for_two' : 'Custo para duas pessoas' })
        
        price_chart.update_layout(barmode='group', xaxis_tickangle=45)
        
        return price_chart




# Data load

df = pd.read_csv('zomato1.csv')

df1 = df.copy()



# =======================================
# Barra Lateral
# =======================================

st.title('Visão Países')

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
    st.caption("<h3 style='text-align: center; color: white;'>Quantidade de Restaurantes Por País</h3>", unsafe_allow_html=True)
    country_chart = country_id(df1)
    st.plotly_chart(country_chart, use_container_width=True)
    
    
    
with st.container():
    st.caption("<h3 style='text-align: center; color: white;'>Quantidade de Cidades Resgistradas po País</h3>", unsafe_allow_html=True)
    city_chart = country_city(df1)
    st.plotly_chart(city_chart, use_container_width=True)
    
      
    
col1, col2 = st.columns(2, gap='large')
    
with col1:
    
    # Média de avaliações feitas país 
    rate_chart = rate_country(df1)
    st.caption("<h3 style='text-align: center; color: white;'>Média de avaliações feitas país</h3>", unsafe_allow_html=True)
    st.plotly_chart(rate_chart, use_container_width=True)
        
           
        
with col2:
    # Média do preço do prato para duas pessoas por país
    
    st.caption("<h3 style='text-align: center; color: white;'>Média do preço do prato para duas pessoas por país</h3>", unsafe_allow_html=True)
    price_chart = country_price(df1)
    st.plotly_chart(price_chart, use_container_width=True)
    
    
    
        
    
    
    
    