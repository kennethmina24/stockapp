import streamlit as st
import config
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def app():
   st.set_page_config(layout="wide")
   sidebar = st.sidebar
   leftpanel, rightpanel = st.beta_columns([7, 3])

   Players = pd.DataFrame(config.Players, columns=['Name', 'Url'])
   Player_list = Players.Name.tolist()

   with sidebar:
       st.subheader("User Input Features")
       selected_year = st.selectbox("Year 1 to Year", list((range(2, 9))), 4)
       SelectedPlayer = st.multiselect("Player", Player_list, Player_list[:4])

   with rightpanel:
       @st.cache(allow_output_mutation=True)
       def load_data(url):
           html = pd.read_html(url, header=0) 
           df = html[0]
           df = df[:selected_year]
           df["Years In NBA"] = range(1, selected_year+1)
           return df

       dataframes = []
       st.title("Individual Player Statistics")
       for player in SelectedPlayer:
           st.subheader(player)
           url = config.URL+Players.loc[Players.Name == player, "Url"].values[0]
           df = load_data(url)
           df["Player Name"] = player
           dataframes.append(df)
           st.write(df)

   glossary = pd.DataFrame(config.Glossary, columns=['Name', 'Meaning'])
   stat_type = glossary.Name.tolist()
   selected_stats = sidebar.multiselect('Player Stats', stat_type, stat_type[:4])
   sidebar.table(glossary)

   dataframes_stacked = pd.concat(dataframes, axis=0).to_csv('output.csv', index=False)
   dataframes_stacked = pd.read_csv('output.csv')

   leftpanel.title("Player Comparison")
   for stat in selected_stats:
       leftpanel.subheader(glossary.loc[glossary.Name == stat, "Meaning"].values[0])
       pivot_table = dataframes_stacked.pivot("Years In NBA", "Player Name", stat)
       leftpanel.write(pivot_table)
       with sns.axes_style("darkgrid"):
           f, ax = plt.subplots(figsize=(5, 3))
           ax = sns.lineplot(data=pivot_table)
           plt.legend(fontsize='xx-small', loc='center left', bbox_to_anchor=(1, 0.5))
           leftpanel.pyplot(f)




