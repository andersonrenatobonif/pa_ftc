# libraries

import pandas as pd
import inflection
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st
from PIL import Image

st.set_page_config(page_title='Visão Culinárias', page_icon='🥘', layout='wide')


# =======================================
# Funções
# =======================================


#Ranking de melhores lojas das culinárias mais predominates
def dataframe_view(df1):
    cuisines = ((df1.loc[:, 'cuisines'] == 'North Indian') | 
                (df1.loc[:, 'cuisines'] == 'American') | 
                (df1.loc[:, 'cuisines'] == 'Cafe') | 
                (df1.loc[:, 'cuisines'] == 'Italian') | 
                (df1.loc[:, 'cuisines'] == 'Pizza')) & (df1.loc[:, 'aggregate_rating'] >= 4.9)

    cuisines = (df1.loc[cuisines, ['restaurant_name', 'aggregate_rating', 'cuisines', 'country', 'restaurant_id', 'city']].
                groupby(['cuisines', 'country',]).
                max().sort_values(by='restaurant_id', ascending=False).
                reset_index())

    cuisines = (cuisines.rename(columns = {'restaurant_name' : "Nome do Restaurante", 
                                           'aggregate_rating' : 'Avaliação Média', 
                                           'city' : 'Cidade', 
                                           'country' : 'País', 
                                           'cuisines' : 'Culinária' }))
    
    return cuisines


# Top 7 culinárias melhor avaliadas
def top_7_cuisines(df1):
    top_7_cuisines = (df1.loc[:, ['cuisines', 'aggregate_rating', 'country'] ].
                      groupby('cuisines').mean().
                      sort_values(by='aggregate_rating', ascending=False).
                      reset_index())
    top_rate_chart = px.bar(
            top_7_cuisines.head(7), x= 'cuisines', y='aggregate_rating' , 
            labels= {'cuisines' : 'Culinárias', 'aggregate_rating' : 'Avaliação Média' }
            )
    
    return top_rate_chart



def bottom_7_cuisines(df1):
    bottom_7_cuisines = (df1.loc[:, ['cuisines', 'aggregate_rating', 'country'] ].
                         groupby('cuisines').mean().
                         sort_values(by='aggregate_rating').
                         reset_index())

    bottom_rate_chart = px.bar(bottom_7_cuisines.head(7), x= 'cuisines', y='aggregate_rating' , 
                               labels= {'cuisines' : 'Culinárias', 'aggregate_rating' : 'Avaliação Média' })
    
    return bottom_rate_chart



def top_cuisines(df1):
    df1_cuisines_id = (df1.loc[:, ['restaurant_id', 'cuisines']].
                          groupby('cuisines').nunique().
                          sort_values(by='restaurant_id', ascending=False).
                          reset_index())
    
    return df1_cuisines_id



# Data load

df = pd.read_csv('zomato1.csv')

df1 = df.copy()



# =======================================
# Barra Lateral
# =======================================

st.title('Visão Culinárias')

st.write('  ')
st.write('  ')
st.write('  ')

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
    st.caption("<h3 style='text-align: center; color: grey;'>Culinárias Predominantes</h3>", 
               unsafe_allow_html=True)
    st.write('  ')
    
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        top_cuisines = top_cuisines(df1)
        col1.metric('Culinária', top_cuisines['restaurant_id'][0], top_cuisines['cuisines'][0])
        
          
    with col2:
               
        col2.metric('Culinária', top_cuisines['restaurant_id'][1], top_cuisines['cuisines'][1])
        
    with col3:
        
        col3.metric('Culinária', top_cuisines['restaurant_id'][2], top_cuisines['cuisines'][2]) 
        
    with col4:
        
        col4.metric('Culinária', top_cuisines['restaurant_id'][3], top_cuisines['cuisines'][3])  
        
    with col5:
        
        col5.metric('Culinária', top_cuisines['restaurant_id'][4], top_cuisines['cuisines'][4])


with st.container():
    st.write('      ')
    st.write('      ')
    


with st.container():
    
    # 10 restaurantes melhor avaliados nos 5 principais tipos de culinárias
    
    st.caption("<h3 style='text-align: center; color: grey;'>Restaurantes melhor avaliados nos tipos de culinárias predominantes</h3>", 
               unsafe_allow_html=True)
    
    st.write('  ')
    
    cuisines = dataframe_view(df1)
    st.dataframe(cuisines[['Nome do Restaurante', 'País', 'Cidade', 'Culinária', 'Avaliação Média']], 
                 use_container_width=True)
    
st.write('  ')
st.write('  ')        
col1, col2 = st.columns(2, gap='large')
    
with col1:
        # Top 7 culinárias melhor avaliadas
        
    st.caption("<h3 style='text-align: center; color: grey;'>7 culinárias melhor avaliadas</h3>", 
               unsafe_allow_html=True)
    top_rate_chart = top_7_cuisines(df1)
    st.plotly_chart(top_rate_chart, use_container_width=True)
    
        
        
with col2:
        # 7 culinárias com pior avaliadas
        
    st.caption("<h3 style='text-align: center; color: grey;'>7 culinárias com pior avaliadas</h3>", 
               unsafe_allow_html=True)
    bottom_rate_chart = bottom_7_cuisines(df1)
    st.plotly_chart(bottom_rate_chart, use_container_width=True)
        
        


            
        
        