import streamlit as st
import numpy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Importando o datasets
barragem = pd.read_csv('dataframe final.csv',encoding='latin1')

topicos = ['Sobre o projeto','Análise inicial','Análise por mapa','Análise por cluster']
barra_lateral = st.sidebar.empty()
estado_sel = st.sidebar.selectbox('Selecione as opções para as base de dados ou para acessar os tópicos',
                                  topicos)

if estado_sel == topicos[0]:
    st.header('Ecomonitor para monitoramento ambiental')
    st.subheader('Ferramentas usando Inteligência Artificial')
    
    st.markdown('Neste mvp faremos uma análise de barragens e utilizaremos técnicas de Ia para se fazer segmentação das barragens')
    st.markdown('Segundo no portal da ANM (que pode ser acessado [aqui](https://www.gov.br/anm/pt-br/assuntos/barragens))')
    st.markdown('Barragem são estruturas projetadas para contenção ou acumulação de substâncias liquidas ou misturas de liquidos e sólidos')
    st.markdown('Dessa forma, todo cuidado e monitoramento é essencial pois com vazamento pode haver impactos ambientais')

    st.cache(persist=True)
    figura_barragem = px.scatter_mapbox(barragem, lat='Latitude', lon='Longitude',title='Barragens de mineração',
                        hover_name="Nome",hover_data=['Empreendedor','MunicÃ\xadpio'],zoom=4, height=900,
                        center={"lat":-14.235004,"lon":-51.92528},
                        color_discrete_sequence=px.colors.qualitative.G10)
    figura_barragem.update_layout(mapbox_style="open-street-map",)
    st.plotly_chart(figura_barragem)

if estado_sel == topicos[1]:
    
    st.header('Análise Exploratória')
    
    # Da análise univariada
    st.markdown('### Análise de apenas uma única variavel')
    
    
    tab1, tab2, tab3, tab4,tab5 = st.tabs(['Estados','Categoria de risco','Dano Potencial Associado - DPA',
                                      'Necessita de PAEBM','Inserido na PNSB'])
    
    
    with tab1:
        Estados = px.histogram(barragem,x='UF',title='Estados onde estão localizadas asbarragens')
        st.plotly_chart(Estados)
    with tab2:
        Risco = px.histogram(barragem,x='Categoria de Risco - CRI',title='categoria de risco das barragens')
        st.plotly_chart(Risco)   
    with tab3:
        Dano = px.histogram(barragem,x='Dano Potencial Associado - DPA',
                            title='Dano Potencial das Barragens')
        st.plotly_chart(Dano)   
    with tab4:
        paebm = px.histogram(barragem,x='Necessita de PAEBM')
        st.plotly_chart(paebm)
    with tab5:
        pnsb = px.histogram(barragem,x='Inserido na PNSB')
        st.plotly_chart(pnsb)
    
    st.markdown('Para entender melho o que é PAEBM clique [aqui](https://www.institutominere.com.br/blog/resolucao-anm-sobre-planos-de-acao-de-emergencia-de-barragens-de-mineracao)')
    st.markdown('Para entender melho o que é PNSB clique [aqui](https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2010/lei/l12334.htm)')

    # Da análise bivariada
    st.markdown('### Análise de das variaveis em relação ao Estado')
    
    tab6, tab7, tab8, tab9 = st.tabs(['Categoria de risco','Dano Potencial Associado - DPA','Necessita de PAEBM',
                               'Inserido na PNSB'])
    
    with tab6:
        Estados_risco = px.histogram(barragem,x='UF',
                                     title='Estados onde estão localizadas asbarragens de acordo com o risco',
                                     color='Categoria de Risco - CRI')
        st.plotly_chart(Estados_risco)
    with tab7:
        Estados_dano = px.histogram(barragem,x='UF',
                                     title='Estados onde estão localizadas asbarragens de acordo com o dano potencial',
                                     color='Dano Potencial Associado - DPA')
        st.plotly_chart(Estados_dano)  
    with tab8:
        Estados_paebm = px.histogram(barragem,x='UF',
                                     title='Estados onde estão localizadas onde necessitam de PAEBM',
                                     color='Necessita de PAEBM')
        st.plotly_chart(Estados_paebm)
    with tab9:
        Estados_pnsb = px.histogram(barragem,x='UF',
                                     title='Estados onde estão localizadas ondeestão inserido no PNSB',
                                     color='Inserido na PNSB')
        st.plotly_chart(Estados_pnsb)
        
    st.markdown('### Análise multivariado')
    
    ana_multivariado = px.parallel_categories(barragem,dimensions=['UF','Categoria de Risco - CRI',
                                                                   'Dano Potencial Associado - DPA','Necessita de PAEBM',
                                                                   'Inserido na PNSB'],
                                              color_continuous_scale=px.colors.sequential.Inferno)
    st.plotly_chart(ana_multivariado)

if estado_sel == topicos[2]:
    
    figura_barragem_risco = px.scatter_mapbox(barragem, lat='Latitude', lon='Longitude',
                                              title='Barragens de mineração de acordo com o risco',
                        hover_name="Nome",hover_data=['Empreendedor','MunicÃ\xadpio',
                                                      'Necessita de PAEBM','Necessita de PAEBM'],zoom=4, height=900,
                        center={"lat":-14.235004,"lon":-51.92528},
                        color_discrete_sequence=px.colors.qualitative.G10,
                        color='Categoria de Risco - CRI')
    figura_barragem_risco.update_layout(mapbox_style="open-street-map")
    st.plotly_chart(figura_barragem_risco)
    
    figura_barragem_dano = px.scatter_mapbox(barragem, lat='Latitude', lon='Longitude',
                                              title='Barragens de mineração de acordo com o dano potencial',
                        hover_name="Nome",hover_data=['Empreendedor','MunicÃ\xadpio',
                                                      'Necessita de PAEBM','Necessita de PAEBM'],zoom=4, height=900,
                        center={"lat":-14.235004,"lon":-51.92528},
                        color_discrete_sequence=px.colors.qualitative.G10,
                        color='Dano Potencial Associado - DPA')
    figura_barragem_dano.update_layout(mapbox_style="open-street-map")
    st.plotly_chart(figura_barragem_dano)

if estado_sel == topicos[3]:
    
    st.header('Análise de cluster')
    
    st.markdown('''Foi feito a *análise de cluster* aplicando o algoritmo kmeans para segmentar as barragens,
                após uma análise as brragens foram divididas em cincos perfis, que foram essas:''')
    
    st.markdown('''1. Clsuter 0:

- A maioria está inserido na categoria de risco baixo
- Dano ptencial na maioria como alto ou médio
- *Estão todos inserido no PNSB*
- São todos do tipo barramento/barragem/dique
- O teor percentual de minério principal do rejeito é ente 0 25% aproximadamente em sua maioria

2. Cluster 1

- A maioria  da categoria de risco baixo ou médio
- A maiorio tem potencial de dano baix
- A maioria não necessita de PAEDM
- *Todos são construido com cava de barramento*
- Teor do minerio principal está entre 0 e 20% aprox. em sua maioria

3. Cluster 2

- Todos tem dano de potencial alto
- Não necessitam de PAEBM
- Estão inserindo do PNSB
- Barra/barragem/dique
- Altura Máxima do projeto da Back Up Dam (m) até 40 m em sua maioria (os mais altos)
- Vida útil prevista da Back Up Dam em até 10 anos em sua maioria (o maiores se comparado com os outros)
- Apresentar um dos maiores teores de minerio principal inserido nos rejeitos

4. Cluster 3

- Maioria da categoria de risco é médio ou baixo
- Dano potencial baixo em sua maioria
- Não necessita de PAEBM
- Maioria não está inserido na PNSB
- Barragem/Dique
- Teor de minério até 15% aproximadamente em sua maioria

5. Cluster 4

- Categoria de risco baixo em sua maioria
- Dano potencial baixo em sua maioria
- *Empilhamento drenado construído hidraulicamente e sucetivel a liquefação*
- *Teor de minerio principal são os menores (próximo a zero)*
                ''')
    
    figura_cluster = px.scatter_mapbox(barragem, lat='Latitude', lon='Longitude',
                                              title='Barragens de mineração de acordo com a segmentação (cluster)',
                        hover_name="Nome",hover_data=['Empreendedor','MunicÃ\xadpio',
                                                      'Necessita de PAEBM','Necessita de PAEBM',
                                                      'Dano Potencial Associado - DPA',
                                                      'Categoria de Risco - CRI'],zoom=4, height=900,
                        center={"lat":-14.235004,"lon":-51.92528},
                        color_discrete_sequence=px.colors.sequential.Inferno,
                        color=barragem['Cluster'].astype(str))
    figura_cluster.update_layout(mapbox_style="open-street-map")
    st.plotly_chart(figura_cluster)
