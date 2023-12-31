import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st


sns.set(context='talk', style='ticks')

st.set_page_config(
     page_title="Análise Exploratória - Previsão de Renda",
     page_icon="./input/icon.png",
     layout="wide",
)


#======================================================================================================

st.markdown("""
    <style>
    .font_style {
        font-size:60px; 
        text-align:center;
    }
    </style>
    <p class='font_style'>Entendimento dos dados</p>
    """, unsafe_allow_html=True)

# Carregando os dados
df = pd.read_csv('previsao_de_renda.csv')

# Criando a figura com subplots
figura, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(15, 15))

# Criando os gráficos
sns.pointplot(data=df, x='data_ref', y='renda', hue='sexo', ax=ax1)
sns.pointplot(data=df, x='data_ref', y='renda', hue='posse_de_veiculo', ax=ax2)
sns.pointplot(data=df, x='data_ref', y='renda', hue='posse_de_imovel', ax=ax3)

# Configurando os rótulos do eixo x
valores_x = pd.to_datetime(df['data_ref']).dt.strftime("%m/%y").unique()
ticks = range(len(valores_x))

for ax in [ax1, ax2, ax3]:
    ax.set_xticks(ticks)
    ax.set_xticklabels(valores_x, rotation=45)
    ax.set_xlabel("")

# Configurando os títulos
ax1.set_title("Média da renda ao longo dos meses baseado no sexo")
ax2.set_title("Média da renda ao longo dos meses baseado se possuí veículo ou não")
ax3.set_title("Média da renda ao longo dos meses baseado se possuí imóvel ou não")

# Ajustando o layout
figura.subplots_adjust(hspace=0.3)

# Exibindo a figura no Streamlit
st.pyplot(figura)

#======================================================================================================
st.markdown("""
    <style>
    .font_style {
        font-size:60px; 
        text-align:center;
    }
    </style>
    <p class='font_style'>Entendimento dos dados</p>
    """, unsafe_allow_html=True)

# Supondo que 'df' seja o DataFrame carregado
df['data_ref'] = pd.to_datetime(df['data_ref'])

# Criando a figura para o gráfico
fig, ax = plt.subplots(figsize=(10, 6))

# Criando o gráfico
sns.pointplot(
    data=df,
    x='data_ref',
    y='renda',
    hue='tipo_renda',
    dodge=True,
    errorbar=('ci', 95)  # Modificado aqui
)

# Configurando os ticks e rótulos do eixo X
tick_labs = df['data_ref'].dt.strftime('%m-%Y').unique()
ticks = range(df['data_ref'].nunique())
ax.set_xticks(ticks)
ax.set_xticklabels(tick_labs, rotation=90)

# Configurando a legenda
plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.10), ncol=3)
plt.legend(bbox_to_anchor=(1.1, 1), loc=2, borderaxespad=0.)

# Exibindo a figura no Streamlit
st.pyplot(fig)

#======================================================================================================
st.markdown("""
    <style>
    .font_style {
        font-size:60px; 
        text-align:center;
    }
    </style>
    <p class='font_style'>Entendimento dos dados</p>
    """, unsafe_allow_html=True)

df['data_ref'] = pd.to_datetime(df['data_ref'])

# Criando a figura
fig, ax = plt.subplots()

# Criando o gráfico
sns.pointplot(
    data=df,
    x='data_ref',
    y='renda',
    hue='sexo',
    dodge=True,
    errorbar=('ci', 95)  # Modificado aqui
)

# Configuração de legenda e etiquetas
plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.10), ncol=3)
tick_labs = df['data_ref'].dt.strftime('%m-%Y').unique()  # Modificado para usar dt
ax.set_xticks(list(range(df['data_ref'].nunique())))
ax.set_xticklabels(tick_labs, rotation=90)
plt.legend(bbox_to_anchor=(1.1, 1), loc=2, borderaxespad=0.)

# Exibindo a figura no Streamlit
st.pyplot(fig)

#======================================================================================================
st.markdown("""
    <style>
    .font_style {
        font-size:60px; 
        text-align:center;
    }
    </style>
    <p class='font_style'>Renda em Relação às Variáveis Numéricas</p>
    """, unsafe_allow_html=True)
corr_matrix = df.select_dtypes('number').corr()

# Criando a figura e os eixos
fig, ax = plt.subplots()

# Criando um gráfico de calor com a nova paleta de cores e linhas divisoras
sns.heatmap(corr_matrix, annot=True, cmap='viridis', linewidths=.5, ax=ax)

# Exibindo o gráfico no Streamlit
st.pyplot(fig)