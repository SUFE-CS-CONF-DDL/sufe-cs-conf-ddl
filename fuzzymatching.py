# pip install fuzzywuzzy
# pip install python-Levenshtein

import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def fuzzy_merge(df_1, df_2, key1, key2, threshold=90, limit=2):
    s = df_2[key2].tolist()
    m = df_1[key1].apply(lambda x: process.extract(x, s, limit=limit))
    df_1['matches'] = m
    m2 = df_1['matches'].apply(lambda x: ', '.join([i[0] for i in x if i[1] >= threshold]))
    df_1['matches'] = m2
    df_1['merge_key'] = df_1['matches']
    df_2['merge_key'] = df_2[key2]
    df = pd.merge(df_1, df_2, how='left',on='merge_key')
    return df

df1 = pd.DataFrame([['Apple','A'],['Banana','B'],['Orange','C'],['Strawberry','D'],['Mango','G']], columns=['Fruits','AA'])
df2 = pd.DataFrame([['Aple','a'],['Bannanna','b'],['Orag','c'],['Strawb','d']], columns=['Fruits','aa'])
all_CCF_path = r'C:\Users\Administrator.WIN-T57L97EEQAK\Desktop\博士毕业\中国计算机学会CCF推荐会议.xlsx'
sime_tenure_path = r'F:\VSCodeProjects\SIME-conference-DDL\.readme_assets\SIME-Tenure-CS-Conference.xlsx'
all_CCF_pd = pd.read_excel(all_CCF_path)
sime_tenure_pd = pd.read_excel(sime_tenure_path)
all_CCF_pd['会议全称'] = all_CCF_pd['会议全称'].str.replace('_x000D_',' ')
sime_tenure_pd.rename(columns={'刊物名称':'会议全称'},inplace=True)
# df = fuzzy_merge(sime_tenure_pd, all_CCF_pd.loc[:,['CCF-Level','会议简称','会议全称','出版社', '网址']], '会议全称', '会议全称', 90)
df = fuzzy_merge(sime_tenure_pd, all_CCF_pd, '会议全称', '会议全称', 90)