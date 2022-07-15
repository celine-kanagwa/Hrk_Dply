import streamlit as st
import matplotlib.pyplot as plt 
import seaborn as sns 
from BreastData import dataset


dataframe = dataset()

def DataAnalysis_section():
   
     col1, col2 = st.columns(2)

     with col1:
         st.text('Bellow is a Breast Cancer dataset')
         st.dataframe(dataframe.data.head())

     with col2:
          st.text('Explotary Data Anlysis')

          st.dataframe(dataframe.remove_id_unnamed)

    
     st.text('Diognasis Target values on graph ')
     Target, Count_Target = dataframe.Target
     st.bar_chart(Target)
        
     st.text("Relationship Between features")
     st.dataframe(dataframe.Corr_graph)   

     #st.markdown('### Analysing column relations')
     #st.text('Correlations:')
     #fig, ax = plt.subplots(figsize=(10,10))
     #sns.heatmap(dataframe.corr(), annot=True, ax=ax)
     #st.pyplot(fig)
     #st.text('Effect of the different classes')
     #Generate a scatter plot matrix with 'mean' columns

    