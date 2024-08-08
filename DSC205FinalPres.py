import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Celtics 2023-2024 Regular Season Stats')

file_path1 = '/Users/annie/Documents/DSC205/Celt_Reg_P_Stats.xlsx'
file1 = pd.read_excel(file_path1)

file_path2 = '/Users/annie/Documents/DSC205/Team_Stats.xlsx'
file2 = pd.read_excel(file_path2)

file_path3a = '/Users/annie/Documents/DSC205/CvsB.xlsx'
file3a = pd.read_excel(file_path3a)

file_path3b = '/Users/annie/Documents/DSC205/CvsW.xlsx'
file3b = pd.read_excel(file_path3b)

file_path4 = '/Users/annie/Documents/DSC205/NBA_All_Stats.xlsx'
file4 = pd.read_excel(file_path4)

file_path5 = '/Users/annie/Documents/DSC205/Thndr.xlsx'
file5 = pd.read_excel(file_path5)

file_path6 = '/Users/annie/Documents/DSC205/EvW_S1.xlsx'
file6 = pd.read_excel(file_path6)

#What were the total minutes played versus the total points made of each player?
file1 = pd.read_excel(file_path1)
minutes = file1[['MP', 'PTS']]

plt.figure(figsize=(10, 6))
plt.scatter(file1['MP'], file1['PTS'], alpha=0.6, color='g', edgecolor='k', linewidth=0.5)
plt.title('Minutes Played Versus Points Made')
plt.xlabel('Minutes Played')
plt.ylabel('Number of Points')
plt.grid(True)
plt.show()

#Celtics v Opponent:
file2 = pd.read_excel(file_path2)
file2.drop([1,2,3,5,6,7],axis=0,inplace=True)
f2_melted = pd.melt(file2, id_vars=['Unnamed: 0'], value_vars=['FG', '3P', '2P', 'AST', 'FT', 'ORB', 'DRB', 'TOV', 'PTS'],
                    var_name='Variable', value_name='Value')
#Celtics v Opponent:
palette = sns.color_palette('YlGn')
sns.set_palette(palette)

sns.catplot(data=f2_melted, x='Variable', y='Value', hue='Unnamed: 0', kind='bar', height=6, aspect=2)

plt.xlabel('Stats')
plt.ylabel('Value')
plt.title('Celtcs vs. Opponent')
plt.xticks(rotation=45)
plt.show()

#Eastern vs Western Seed 1:
file6 = pd.read_excel(file_path6)

f6_melted = pd.melt(file6, id_vars=['Team'], value_vars=['FG', '3P', '2P', 'AST', 'FT', 'ORB', 'DRB', 'TOV', 'PTS'],
                    var_name='Variable', value_name='Value')

palette = sns.color_palette('YlGn')
sns.set_palette(palette)

sns.catplot(data=f6_melted, x='Variable', y='Value', hue='Team', kind='bar', height=6, aspect=2)

plt.xlabel('Stats')
plt.ylabel('Value')
plt.title('Eastern vs Western Seed 1: Stats')
plt.xticks(rotation=45)
plt.show()
