# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 15:20:17 2020

@author: joaopq
"""

#   HDI: is development going the right way?

'''
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   IMPORTING LIBRARIES  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math
import scipy.stats
import more_itertools
import statsmodels.api as sm
import sys
from glob import glob
    
'''
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   CREATING DATAFRAMES BELOW   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
'''

#DEPENDENT var: HUMAN DEVELOPMENT INDEX (HDI)
hdi=pd.read_csv("E:\\2. Aprendizagem\\2.3. Ironhack\\2. Projects\\Week_6\\human development theme\\timeline\\human-development-index.csv")

'''
#INDEPENDENT vars: 
mental_disorders=pd.read_csv("E:\\2. Aprendizagem\\2.3. Ironhack\\2. Projects\\Week_6\\human development theme\\timeline\\share-with-mental-and-substance-disorders.csv")
#schizophrenia=pd.read_csv("E:\\2. Aprendizagem\\2.3. Ironhack\\2. Projects\\Week_6\\human development theme\\timeline\\share-of-population-with-schizophrenia.csv")
#anxiety=pd.read_csv("E:\\2. Aprendizagem\\2.3. Ironhack\\2. Projects\\Week_6\\human development theme\\timeline\\share-with-anxiety-disorders.csv")
forest_area=pd.read_csv("E:\\2. Aprendizagem\\2.3. Ironhack\\2. Projects\\Week_6\\human development theme\\timeline\\forest-area-percent.csv")
#military_exp=pd.read_csv("E:\\2. Aprendizagem\\2.3. Ironhack\\2. Projects\\Week_6\\human development theme\\timeline\\military-expenditure-as-share-of-gdp.csv")
trust=pd.read_csv("E:\\2. Aprendizagem\\2.3. Ironhack\\2. Projects\\Week_6\\human development theme\\timeline\\self-reported-trust-attitudes.csv")
divorces=pd.read_csv("E:\\2. Aprendizagem\\2.3. Ironhack\\2. Projects\\Week_6\\human development theme\\timeline\\divorces-per-1000-people.csv")
#freedom_score=pd.read_csv("E:\\2. Aprendizagem\\2.3. Ironhack\\2. Projects\\Week_6\\human development theme\\timeline\\world-map-of-the-freedom-of-the-press-status.csv")
perceived_corruption=pd.read_csv("E:\\2. Aprendizagem\\2.3. Ironhack\\2. Projects\\Week_6\\human development theme\\timeline\\TI-corruption-perception-index.csv")
gini=pd.read_csv("E:\\2. Aprendizagem\\2.3. Ironhack\\2. Projects\\Week_6\\human development theme\\timeline\\gini-coefficient-equivalized-income-chartbook.csv")
suicides=pd.read_csv("E:\\2. Aprendizagem\\2.3. Ironhack\\2. Projects\\Week_6\\human development theme\\timeline\\suicide-rates-by-country.csv")
'''
'''
not working:
human_height=pd.read_csv("E:\\2. Aprendizagem\\2.3. Ironhack\\2. Projects\\Week_6\\human development theme\\timeline\\average-height-by-year-of-birth.csv")
'''
'''IMPORT ALL FILES IN FOLDER:'''
from glob import glob
filenames = glob("E:\\2. Aprendizagem\\2.3. Ironhack\\2. Projects\\Week_6\\human development theme\\timeline\\*.csv")
frames=[pd.read_csv(f) for f in filenames]


'''Concatenate all the dataframes with columns YEAR and ENTITY'''

#frames that we'll set indexes
#frames=[mental_disorders, divorces,freedom_score,perceived_corruption, forest_area,gini, suicides]

elements_to_drop=pd.read_csv("E:\\2. Aprendizagem\\2.3. Ironhack\\2. Projects\\Week_6\\human development theme\\dt selection and cleaning criterias\\elements to drop in dfs.csv")
#print(elements_to_drop)

def cleaner(x):
    return x not in elements_to_drop

#cleaning them and then merging the dfs
results = []
for df in frames:
    #condition = df['Entity'].apply(cleaner)
    #df = df[condition]
    df.drop(['Code'], axis=1)
    #df.set_index(["Entity", "Year"], inplace=True)
    results.append(df)
#print(results[5])
    
condition = hdi['Entity'].apply(cleaner)
hdi = hdi[condition]
hdi.to_excel("E:\\2. Aprendizagem\\2.3. Ironhack\\2. Projects\\Week_6\\human development theme\\from python to excel\\hdi.xlsx")

hdi=hdi.drop(['Code'], axis=1)
df_analysis = hdi

for x in range(len(results)):
    #print(df_analysis.columns, len(df_analysis),results[x].dtypes)
    df_analysis = df_analysis.merge(results[x], on=['Entity', 'Year'], how='outer')
    #if len(df_analysis) == 0:
        #print(x)

condition = df_analysis['Entity'].apply(cleaner)
df_analysis = df_analysis[condition]
    
#print("status: df_analysis")
#print(df_analysis.head())
#print(df_analysis.columns)
df_analysis.to_excel("E:\\2. Aprendizagem\\2.3. Ironhack\\2. Projects\\Week_6\\human development theme\\from python to excel\\df_analysis.xlsx")


'''
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   INFERENTIAL STATISTICS   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
'''

'''.
▒▒▒▒ Do correlation matrixes to filter worthwhile dependent variables.▒▒▒▒▒▒▒▒
'''
corr_methods=['pearson','spearman','kendall']
path="E:\\2. Aprendizagem\\2.3. Ironhack\\2. Projects\\Week_6\\human development theme\\from python to excel\\"
excel_format="xlsx"

corr_pearson_matrix=df_analysis.corr(method='pearson')
corr_pearson_matrix.drop(['HDI_y', 'Year'], axis=1)
corr_pearson_matrix.to_excel(path+"corr_pearson_matrix."+excel_format)

corr_spearman_matrix=df_analysis.corr(method='spearman')
corr_spearman_matrix.drop(['HDI_y', 'Year'], axis=1)
corr_spearman_matrix.to_excel(path+"corr_spearman_matrix."+excel_format)

corr_kendaltau_matrix=df_analysis.corr(method='kendall')
corr_kendaltau_matrix.drop(['HDI_y', 'Year'], axis=1)
corr_kendaltau_matrix.to_excel(path+"corr_kendaltau_matrix."+excel_format)

#compute differences between correlation matrixes
diff_pearson_spearman=corr_pearson_matrix-corr_spearman_matrix
diff_pearson_spearman.drop(['HDI_y', 'Year'], axis=1)
diff_pearson_spearman.to_excel(path+"diff_pearson_spearman."+excel_format)
print("avg difference between pearson and spearman is: "+str(diff_pearson_spearman.mean().mean()))


'''
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   plotting   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
'''
sns.set()

# Draw a heatmap with the numeric values in each cell
f, ax = plt.subplots(figsize=(16, 8))
path_plots="E:\\2. Aprendizagem\\2.3. Ironhack\\2. Projects\\Week_6\\human development theme\\from python to images\\"
sns.heatmap(corr_pearson_matrix, linewidths=.5,cmap="RdBu_r")
plt.savefig(path+"corr_pearson_matrix.png")


#sns.heatmap(corr_spearman_matrix, annot=True, linewidths=.5,cmap="RdBu_r")
plt.savefig(path+"corr_spearman_matrix.png")

#sns.heatmap(corr_kendaltau_matrix, annot=True, linewidths=.5,cmap="RdBu_r")
plt.savefig(path+"corr_kendaltau_matrix.png")

#sns.heatmap(diff_pearson_spearman, linewidths=.5,cmap="RdBu_r")
plt.savefig(path+"diff_pearson_spearman.png")


'''
#Univariate statistics on each variable
for n in range(0,len(frames)):

    sns.distplot(frames[n], kde=False) 

print(mental_disorders.head())

print(sns.distplot(mental_disorders[3], kde=False))
'''


'''
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   Do multilinear regression   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
'''
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ multilinear regression for ALL ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
print(df_analysis.columns)

X_all=df_analysis[["Entity", "Year", "Annual hours worked per worker", "Avg Height (cm)" , "Live births per woman","Total population","Crude divorce rate (per 1,000 inhabitants)" ,"Forest area (% of land area)", "Gini coeff" ,"World Happiness Report","Interpersonal violence (homicides per 100,000)" , "Human Rights Protection Scores" ,"Military expenditure (% of GDP)", "Schizophrenia (%)","Bipolar disorder (%)", "Eating disorders (%)", "Anxiety disorders (%)","Drug use disorders (%)", "Depression (%)", "Alcohol use disorders (%)", "Trust in others (%)","Share of Top 1% in Pre-tax national income (%)" ,"Share with Mental and Substance disorders", "Suicide rate", "Taxes  goods and services (% GDP)","Corruption Perception Index", "Freedom score"]]
X_all=X_all.fillna(0)   
print(X_all.dtypes)
Y=df_analysis['HDI_x'].fillna(0)
print(Y)
OLSmodel_all_vars=sm.OLS(Y,X_all).fit()
print(OLSmodel_all_vars.summary())

df_OLS_all = pd.concat((OLSmodel_all_vars.params, OLSmodel_all_vars.tvalues), axis=1)
df_OLS_all.rename(columns={0: 'beta', 1: 't-values',2:'r2'}).to_excel(path+"df_OLS_all."+excel_format)

#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ multilinear regression for strongly correlated ▒▒▒▒▒▒▒▒▒▒▒▒▒▒
X_selected=df_analysis[["World Happiness Report", "Live births per woman", "Corruption Perception Index", "Avg Height (cm)", "Eating disorders (%)", "Human Rights Protection Scores", "Annual hours worked per worker", "Schizophrenia (%)", "Bipolar disorder (%)", "Taxes  goods and services (% GDP)"]]
X_selected=X_selected.fillna(0)
print(X_all.dtypes)
Y=df_analysis['HDI_x'].fillna(0)
print(Y)
OLSmodel_selected_vars=sm.OLS(Y,X_selected).fit()
print(OLSmodel_selected_vars.summary())


df_OLS_selected = pd.concat((OLSmodel_selected_vars.params, OLSmodel_selected_vars.tvalues), axis=1)
df_OLS_selected.rename(columns={0: 'beta', 1: 't-values',2:'r2'}).to_excel(path+"OLSmodel_selected_vars."+excel_format)

#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#multilinear regression for strongly correlated var's with negative connotation
X_negative=df_analysis[["Schizophrenia (%)"," Live births per woman","Eating disorders (%)","Bipolar disorder (%)"]]
X_negative=X_negative.fillna(0)
print(X_all.dtypes)
Y=df_analysis['HDI_x'].fillna(0)
print(Y)
OLSmodel_neg_vars=sm.OLS(Y,X_negative).fit()
print(OLSmodel_neg_vars.summary())


df_OLSmodel_neg_vars = pd.concat((OLSmodel_neg_vars.params, OLSmodel_neg_vars.tvalues), axis=1)
df_OLSmodel_neg_vars.rename(columns={0: 'beta', 1: 't-values',2:'r2'}).to_excel(path+"df_OLSmodel_neg_vars."+excel_format)

#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#multilinear regression for strongly correlated var's with positive connotation

X_positive=df_analysis[["World Happiness Report","Corruption Perception Index","Human Rights Protection Scores","Annual hours worked per worker","Taxes  goods and services (% GDP)"]]
X_positive=X_positive.fillna(0)
print(X_all.dtypes)
Y=df_analysis['HDI_x'].fillna(0)
print(Y)
OLSmodel_pos_vars=sm.OLS(Y,X_positive).fit()
print(OLSmodel_pos_vars.summary())


df_OLSmodel_pos_vars = pd.concat((OLSmodel_pos_vars.params, OLSmodel_pos_vars.tvalues), axis=1)
df_OLSmodel_pos_vars.rename(columns={0: 'beta', 1: 't-values',2:'r2'}).to_excel(path+"df_OLSmodel_pos_vars."+excel_format)


#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ Comparing all R Squareds ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
print("R Squared of all vars is: "+str(OLSmodel_all_vars.rsquared))
print("R Squared of selected vars is: "+str(OLSmodel_selected_vars.rsquared))
print("R Squared of selected positive sentiment vars is: "+str(OLSmodel_pos_vars.rsquared))
print("R Squared of selected negative sentiment vars "+str(OLSmodel_neg_vars.rsquared))

'''
X_selected=df_analysis[['Year','Cylinders','Fuel Barrels/Year','Combined MPG','Fuel Cost/Year']]
OLSmodel_all_vars=sm.OLS(Y,X).fit()
print(OLSmodel_selected_vars.summary())
'''