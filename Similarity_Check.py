
# coding: utf-8

# In[52]:


import sys,os
import numpy as np 
import nltk as nt
import docx
from nltk.corpus import stopwords
import glob,os
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import glob,os, itertools


# In[53]:


import re, math
from collections import Counter

WORD = re.compile(r'\w+')

def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)


vector1 = text_to_vector(text1)
vector2 = text_to_vector(text2)

cosine = get_cosine(vector1, vector2)


# In[54]:


# reading data scientist JD
f = open("Data_Scientist_JD.txt","r")
Data_Science_JD = f.read()
Data_Science_JD = text_to_vector(Data_Science_JD)

# creating 2 lists
person = []
score = []


# reading the resumes
for file in glob.glob('resumes\\*.txt'):
    #print(file)
    files = file.split('\\')[6].split('.')[0]
    f1 = open(file,"r")
    resume = f1.read()
    resume_skills = resume.split('Skills:')[1]
    resume_skills = text_to_vector(resume_skills)
    #resume = process(filepath)
    Data_Scientist = get_cosine(resume_skills,Data_Science_JD)
    person.append(files)
    score.append(Data_Scientist)


# In[55]:


final_score = pd.DataFrame(
    {'Person': person,
     'Percentage_Match': score
    })
final_score['Percentage_Match'] = final_score['Percentage_Match']*100


# In[50]:


final_score.to_csv('score.csv')


# In[56]:


final_score


# In[57]:


os.getcwd()


# In[ ]:




