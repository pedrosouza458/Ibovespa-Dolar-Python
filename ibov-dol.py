#!/usr/bin/env python
# coding: utf-8

# In[36]:


import pandas as pd
import datetime
import yfinance as yf
from matplotlib import pyplot as plt
import mplcyberpunk


# In[ ]:


codigos_de_negociação = ["^BVSP","BRL=X"] 
hoje = datetime.datetime.now()
um_ano_atras = hoje - datetime.timedelta(days = 365) 

dados_mercado = yf.download(codigos_de_negociação, um_ano_atras, hoje)

display(dados_mercado)


# In[49]:


dados_fechamento = dados_mercado["Adj Close"]
dados_fechamento.columns = ['dolar','ibovespa']
dados_fechamento = dados_fechamento.dropna()

dados_fechamento


# In[57]:


dados_anuais = dados_fechamento.resample("Y").last()
dados_mensais = dados_fechamento.resample("M").last()
dados_anuais


# In[68]:


retorno_anual = dados_anuais.pct_change().dropna()
retorno_mensal = dados_mensais.pct_change().dropna()
retorno_diario = dados_fechamento.pct_change().dropna()

retorno_diario


# In[108]:


#retorno_dia = retorno_diario.loc['2022-02-08', 'dolar']
#retorno_dia_iloc = retorno_diario.iloc[0, 0]

retorno_diario_dolar = retorno_diario.iloc[-1, 0]
retorno_diario_ibov = retorno_diario.iloc[-1, 1]

retorno_mensal_dolar = retorno_mensal.iloc[-1, 0]
retorno_mensal_ibov = retorno_mensal.iloc[-1, 1]

retorno_anual_dolar = retorno_anual.iloc[-1, 0]
retorno_anual_ibov = retorno_anual.iloc[-1, 1]

print(retorno_anual_dolar)
display(retorno_anual)


# In[ ]:





# In[109]:


retorno_diario_dolar = round((retorno_diario_dolar * 100), 2)
retorno_diario_ibov = round((retorno_diario_ibov * 100), 2)

retorno_mensal_dolar = round((retorno_mensal_dolar * 100), 2)
retorno_mensal_ibov = round((retorno_mensal_ibov * 100), 2) 

retorno_anual_dolar = round((retorno_anual_dolar * 100), 2)
retorno_anual_ibov = round((retorno_anual_ibov * 100), 2)

print(retorno_anual_dolar)


# In[113]:


plt.style.use("cyberpunk")

dados_fechamento.plot(y = "ibovespa", use_index = True, legend = False)

plt.title("Ibovespa")
plt.savefig('ibovespa.png', dpi = 300)

plt.show()

