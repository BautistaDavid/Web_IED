import streamlit as st 
import pandas as pd 
import plotly.express as px
st. set_page_config(layout="wide")
st.title('Graficos Proyecto  Inversion Extranjera Directa')
df_variables = pd.read_csv('variables.csv')
df_variables_1diferencia = pd.read_csv('variables_1diferencia.csv')

var = st.selectbox(
    'Seleccione Variable de Interes',
    ('IED', 'TRM', 'IPC', 'IPI', 'ISE'))


fig = px.line(df_variables, x='periodo', y=var)

# fig.update_xaxes(visible=False, fixedrange=True)
# fig.update_yaxes(visible=False, fixedrange=True)

fig_dif = px.line(df_variables_1diferencia, x='periodo', y=var)


# st.subheader(f'{var} ')
# st.plotly_chart(fig,use_container_width=True, sharing="streamlit", theme='streamlit')

# st.subheader(f'Primera Diferencia {var}')
# st.plotly_chart(fig_dif,use_container_width=True, sharing="streamlit", theme='streamlit')

col1, col2 = st.columns(2)

with col1:
   st.header("Niveles")
   st.plotly_chart(fig,use_container_width=True, sharing="streamlit", theme='streamlit')

with col2:
   st.header("Primera Diferencia")
   st.plotly_chart(fig_dif,use_container_width=True, sharing="streamlit", theme='streamlit')



