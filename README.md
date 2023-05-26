# 1- Problema de Negócio

A empresa Food Company é uma marketplace de restaurantes. Seu core business é facilitar o encontro e negociações de clientes e restaurantes. Os restaurantes fazem o cadastro dentro da plataforma da Food Company, que disponibiliza informações como endereço, tipo de culinária, se possui reservas, se faz entregas e também uma nota de avaliação dos serviços e produtos do restaurante, dentre outras informações.


O CEO também foi recém contratado e precisa entender melhor o negócio para conseguir tomar as melhores decisões estratégicas e alavancar ainda mais a Food Company, e para isso, ele precisa que seja feita uma análise nos dados da empresa e que sejam gerados dashboards para a partir disso ele conseguir responsder algumas perguntas de negócio.



# 2- Premissas do Negócio

- Foi utilizado apenas um tipo de culinária de cada restaurante, a primeira culinária da lista de cada restaurante foi tomada como a principal.

- As 3 principais visões assumidas para criação do dashboard foram: Visão Países, Visão Cidades, Visão Culinárias


# 3- Estratégia da Solução

O dashboaard foi construído seguindo as 3 principais visões do negócio.

- Visão Países, 
- Visão Cidades,
- Visão Culinárias

Cada visão é representada pelo segguinte conjunto de métricas:

## Visão Países:

- Quantidade de Restaurantes Por País
- Quantidade de Cidades Resgistradas po País
- Média de avaliações feitas país
- Média do preço do prato para duas pessoas por país


## Visão Cidades

- Top 10 Cidades com mais restaurantes
- 7 cidade com restaurantes com mais avaliações
- 7 cidade com restaurantes com avaliações acima de 4.5
- 10 cidade com mais quantidade de tipo de culinária distinto


## Visão Culinárias

- Culinárias Predominantes
- Restaurantes melhor avaliados nos tipos de culinárias predominantes
- 7 culinárias melhor avaliadas
- 7 culinárias com pior avaliadas



# 4- Top 3 Insights de Dados

- Índia é o país com mais cidades registradas, tendo mais que o dobro do país que está em segundo lugar. Também é o país resgitrado com a maior variedade de culinárias distintas.

- Mesmo não sendo o país com mais restaurantes registrados, EUA é o país que possui maior quantidade de restaurantes registrados no nível de preço 'Gourmet', o mais alto.

- Restaurantes que aceitam pedidos online recebem mais pedidos, consequentemente mais avaliações.



# 5- O produto final do projeto

Painel hospedado em cloud que pode ser acessado de qualquer lugar e a qualquer momento.

Pode ser acessado através desse link: https://arsantos-pa-ftc.streamlit.app/


# 6- Conclusão

O objetivo desse projeto é criar um dashboard que ajude o CEO no acompnhamento dos resultados e tomadas de decisão mas rápidas. 

Da visão da empresa pode-se concluir que a empresa possui forte presença em regiões da Ásia e Oriente Médio, tendo oportunidades de crescimento especialmente na América do Sul.


# 7- Próximos passos

- Criar novos filtros para facilitar a visualização.

- Definir e incluir novas métricas

- Adicionar novas visões de negócio
