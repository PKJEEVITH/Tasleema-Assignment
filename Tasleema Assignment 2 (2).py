#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import os


# In[2]:


API_Data = pd.read_excel(r'C:\Users\p.jeevith\Documents\API_19_DS2_en_csv_v2_5340933\API_19_DS2_en_csv_v2_5340933.xlsx')


# In[ ]:





# In[9]:


def choose_data(filename):
    path=r"C:\Users\p.jeevith\Documents\API_19_DS2_en_csv_v2_5340933"
    API_Data = pd.read_excel(path + "/" + filename)
    API_Data_Archive = API_Data.copy()
    API_Data1 = API_Data[3:]
    API_Data1.columns = API_Data1.iloc[0]
    API_Data = API_Data1[1:]
    
    
    API_Data2 = pd.melt(API_Data, id_vars=['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'], 
                        var_name="Year", value_name="Value")
    
    Clean_Data = cleaning(API_Data2)
    API_Data2 = Clean_Data.copy()
    
    Country_As_Columns = API_Data2.pivot(index = ['Indicator Name', 'Indicator Code', 'Year'], columns = 'Country Name', 
                                      values = 'Value').reset_index()
    
    Date_As_Columns = API_Data2.pivot(index = ['Country Name', 'Country Code', 'Indicator Name'], columns = 'Year', 
                                      values = 'Value').reset_index()
    return Date_As_Columns , Country_As_Columns
    


# In[13]:


def cleaning(data):
    columns = data.columns
    country_list = data['Country Name'].unique()
    Indicator_list = data['Indicator Name'].unique()
    
    data=data.sort_values(['Country Name','Indicator Name'])
    Clean_Data = pd.DataFrame()
    
    for i in Indicator_list:
        data_i = data[(data['Indicator Name']==i)]
        data_i['Value'] = data_i['Value'].fillna(data_i['Value'].mean())

    Clean_Data = Clean_Data.append(data_i)
    
    return Clean_Data    


# In[ ]:





# In[14]:


Date_As_Columns , Country_As_Columns = choose_data('API_19_DS2_en_csv_v2_5340933.xlsx')


# In[15]:


Date_As_Columns


# In[ ]:


Date_As_Columns.describe()


# In[ ]:


Country_As_Columns.describe()


# In[ ]:


Urban_pop = Date_As_Columns[(Date_As_Columns['Indicator Name']=='Urban population growth (annual %)')&(Date_As_Columns['Country Name']=='India')]
Urban_pop.describe()


# In[ ]:


Dates_Country_choosen = Date_As_Columns[(Date_As_Columns['Country Name']=='India')|(Date_As_Columns['Country Name']=='Australia')
                |(Date_As_Columns['Country Name']=='Japan')|(Date_As_Columns['Country Code']=='USA')
                |(Date_As_Columns['Country Name']=='United Kingdom')|(Date_As_Columns['Country Name']=='Germany')
                |(Date_As_Columns['Country Name']=='China')|(Date_As_Columns['Country Name']=='Brazil')]


# In[ ]:


API_Data2 = pd.melt(Dates_Country_choosen, id_vars=['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'], 
                        var_name="Year", value_name="Value")


# In[ ]:


API_Data3 = API_Data2[API_Data2['Indicator Name']=='CO2 emissions (kt)']


# In[ ]:


API_Data2['Indicator Name'].unique()


# In[ ]:


API_Data3


# In[ ]:



Country_Name = API_Data3['Country Name'].unique()
for i in Country_Name:
#     plt.figure(figsize=(17,6))
    country_i = API_Data3[API_Data3['Country Name']==i].sort_values('Year')
    plt.plot(country_i['Year'], country_i['Value'], label=i)
    plt.legend()
    plt.plot()
    


# In[ ]:


API_Data4 = API_Data2[API_Data2['Indicator Name']=='Electric power consumption (kWh per capita)']
Country_Name = API_Data4['Country Name'].unique()
for i in Country_Name:
#     plt.figure(figsize=(17,6))
    country_i = API_Data4[API_Data4['Country Name']==i].sort_values('Year')
    plt.plot(country_i['Year'], country_i['Value'], label=i)
    plt.title('electricity consumption')
    plt.legend()
    plt.plot()


# In[ ]:


API_Data4 = API_Data2[API_Data2['Indicator Name']=='Population, total']
Country_Name = API_Data4['Country Name'].unique()
for i in Country_Name:
#     plt.figure(figsize=(17,6))
    country_i = API_Data4[API_Data4['Country Name']==i].sort_values('Year')
    plt.plot(country_i['Year'], country_i['Value'], label=i)
    plt.title('population total')
    plt.legend()
    plt.plot()


# In[ ]:


API_Data2


# In[ ]:


API_Data5 = API_Data2[(API_Data2['Indicator Name']=='Renewable energy consumption (% of total final energy consumption)')&
                      ((API_Data2['Country Code']=='USA')|(API_Data2['Country Name']=='China'))]
Country_Name = API_Data5['Country Name'].unique()
for i in Country_Name:
#     plt.figure(figsize=(17,6))
    country_i = API_Data5[API_Data5['Country Name']==i].sort_values('Year')
    plt.plot(country_i['Year'], country_i['Value'], label=i)
    plt.title('renewable energy %')
    plt.legend()
    plt.plot()


# In[ ]:


API_Data6 = API_Data2[(API_Data2['Indicator Name']=='Renewable energy consumption (% of total final energy consumption)')|
         (API_Data2['Indicator Name']=='Electric power consumption (kWh per capita)')|
         (API_Data2['Indicator Name']=='Population, total')|
         (API_Data2['Indicator Name']=='CO2 emissions (kt)')|
         (API_Data2['Indicator Name']=='Total greenhouse gas emissions (kt of CO2 equivalent)')]


# In[ ]:


pivotdata = API_Data6.pivot(index = ['Country Name', 'Year', 'Country Code'], columns = 'Indicator Name', 
                                      values = 'Value').reset_index()


# In[ ]:





# In[ ]:


data = pivotdata[(pivotdata['Country Name']=='China')|(pivotdata['Country Code']=='USA')]
corr = data.corr()
heat = sns.heatmap(corr)
heat


# In[ ]:




