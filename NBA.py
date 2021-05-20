import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import tweepy
import re
from NBA_Players_Names import replace_values 

def app():
      # Sidebar - Position selection
      st.title('NBA Player Explorer')
      #File Upload
      st.subheader("DataFrame")
      # Web scraping of NBA player stats
      @st.cache
      def load_data():
          url = "https://www.basketball-reference.com/leagues/NBA_2021_per_game.html"
          html = pd.read_html(url, header = 0)
          df = html[0]
          raw = df.drop(df[df.Age == 'Age'].index) # Deletes repeating headers in content
          raw = raw.fillna(0)
          playerstats = raw.drop(['Rk','Age','G','GS'], axis=1)
          playerstats=playerstats.rename(columns={'Player':'Name'})
          playerstats=playerstats.drop_duplicates(subset=(['Name']))
          playerstats["Name"] = playerstats["Name"].str.replace("ć", "c")
          playerstats["Name"] = playerstats["Name"].str.replace("é", "e")
          playerstats["Name"] = playerstats["Name"].str.replace("ö", "o")
          playerstats["Name"] = playerstats["Name"].str.replace("č", "c")
          playerstats["Name"] = playerstats["Name"].str.replace("ū", "u")
          playerstats["Name"] = playerstats["Name"].str.replace("Š", "S")
          playerstats["Name"] = playerstats["Name"].str.replace("š", "s")
          playerstats["Name"] = playerstats["Name"].str.replace("á", "a")
          playerstats["Name"] = playerstats["Name"].str.replace("ý", "y")
          playerstats["Name"] = playerstats["Name"].str.replace("í", "i")
          playerstats["Name"] = playerstats["Name"].str.replace("ò", "o")
          playerstats["Name"] = playerstats["Name"].str.replace("ó", "o")
          playerstats["Name"] = playerstats["Name"].str.replace("ņ", "n")
          playerstats["Name"] = playerstats["Name"].str.replace("ģ", "g")
          playerstats["Name"] = playerstats["Name"].str.replace("ā", "a")
          playerstats["Name"] = playerstats["Name"].str.replace("Č", "C")
          playerstats["Name"] = playerstats["Name"].str.replace("İ", "I")
          playerstats["Pos"] = playerstats["Pos"].str.replace("SF-SG", "SG")
          playerstats=playerstats.replace({'Name':replace_values})   
          return playerstats
      playerstats = load_data()
      # Filtering data
      st.header('Display Player Stats of Selected Team(s)')
      #st.write('Data Dimension: ' + str(df_selected_team.shape[0]) + ' rows and ' + str(df_selected_team.shape[1]) + ' columns.')
      st.dataframe(playerstats)
# Upload CSV data
    
      # Mine Data
      data_file=st.file_uploader("Upload File",type=['csv','txt','docx','pdf'])
      if data_file is None:
            st.write("Enter File, the data set is empty")
            st.sidebar.markdown("""
      [Example CSV input file](https://raw.githubusercontent.com/kennethmina24/stockapp/master/playerstats.csv)
      """)
      if data_file is not None:
            pf = pd.read_csv('data_file')
            pf=pf.drop(columns=['TeamAbbrev','Name + ID','Game Info','Roster Position','ID'])
            file_details = {"Filename":data_file.name,"FileType":data_file.type,"FileSize":data_file.size}
            pf=pf.rename(columns={'Position':'Pos'})
            pf=pf.rename(columns={'TeamAbbrev':'Tm'})
                   #Show Data
            st.write(file_details)
                     # Filtering data    
            #Combine List
            Combined_DK_Website=pf.merge( playerstats,how='outer',on='Name')
            Combined_DK_Website=Combined_DK_Website.drop(columns= ['Pos_x'])
            Combined_DK_Website=Combined_DK_Website.dropna(subset=['Salary'])
            Combined_DK_Website = Combined_DK_Website[Combined_DK_Website.Name !='Udonis Haslem' ]
            Combined_DK_Website=Combined_DK_Website.fillna('Empty')
            Combined_DK_Website['MP'] =  Combined_DK_Website.MP.astype(float)
            Combined_DK_Website['Points/Minutes']=Combined_DK_Website['AvgPointsPerGame']/Combined_DK_Website['MP']
            titles=list(Combined_DK_Website.columns)
            titles[3],titles[28]= titles[28],titles[3]
            Combined_DK_Website=Combined_DK_Website[titles]
            x=Combined_DK_Website.dtypes
            st.dataframe(x)
            
             #Sidebar - Team selection
            sorted_unique_team = sorted(Combined_DK_Website.Tm.unique())
            selected_team = st.sidebar.multiselect('Team', sorted_unique_team, sorted_unique_team)

            # Sidebar - Position selection
            unique_pos = ['C','PF','SF','PG','SG','Empty']
            selected_pos = st.sidebar.multiselect('Position', unique_pos, unique_pos)

            # Filtering data
            Combined_DK_Website = Combined_DK_Website[(Combined_DK_Website.Tm.isin(selected_team)) & (Combined_DK_Website.Pos_y.isin(selected_pos))]
            # Download CSV
            st.dataframe(Combined_DK_Website)
            def filedownload(pf):
                csv = pf.to_csv(index=False)
                b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
                href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
                return href
            st.markdown(filedownload(Combined_DK_Website), unsafe_allow_html=True)
            
            
             # Heatmap
            if st.button('Intercorrelation Heatmap'):
                  st.header('Intercorrelation Matrix Heatmap')
                  playerstats.to_csv('output.csv',index=False)
                  df = pd.read_csv('output.csv')
                  corr = df.corr()
                  mask = np.zeros_like(corr)
                  mask[np.triu_indices_from(mask)] = True
                  with sns.axes_style("white"):
                        f, ax = plt.subplots(figsize=(7, 5))
                        ax = sns.heatmap(corr, mask=mask, vmax=1, square=True)
                        st.set_option('deprecation.showPyplotGlobalUse', False)
                        st.pyplot()
                        
                 #Twitter
            API_Key='erGvaGFQ04PUhHoIbCbXoB6Gy'
            API_secret='owHXRfmvCzDCy2wBWERQpwanz6cq6qokuzmUd1jnqsNCtOLxpD'
            Access_key='1308415930029010944-Tc0xoXoQHBDfGqAJvAJXCEYBwHaV7b'
            Access_secret='oerSooSzTUW7vjStaDWhbm5XD5WOy09AAEyB8qrGAmegm'
            #Step 2
            #Authenication Object
            auth=tweepy.OAuthHandler(API_Key,API_secret)

            # Set the access
            auth.set_access_token(Access_key,Access_secret)

            #API Object
            api=tweepy.API(auth,wait_on_rate_limit=True)
           
            st.title('Sentiment Analysis of a users tweets')
            st.markdown('Enter user and number of tweets')
            twitterAccount = st.text_input('Twitter User','FantasyLabsNBA')
            n = int(st.text_input('Number of tweets','50'))
            
            tweets = tweepy.Cursor(api.user_timeline, 
                    screen_name=twitterAccount, 
                    count=None,
                    since_id=None,
                    max_id=None,
                    trim_user=True,
                    exclude_replies=True,
                    contributor_details=False,
                    include_entities=False
                    ).items(n);

            sa = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweet'])
            st.dataframe(sa)
            
           



