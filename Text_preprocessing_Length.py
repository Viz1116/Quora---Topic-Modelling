#!/usr/bin/env python
# coding: utf-8

# In[55]:


import spacy

def clean_text(text):
    '''Make text lowercase, remove text in square brackets, remove punctuation and remove words containing numbers.'''
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub(r'\w*\d\w*', '', text)
    
    return text
df_clean = pd.DataFrame(df.question_text.apply(lambda x: clean_text(x)))

nlp=spacy.load('en_core_web_sm')
def lemmatizer(text):        
  sent = []
  doc=nlp(text) 
  print(doc)
  for word in doc :
        sent.append(word.lemma_)
  return "".join(sent)

df_clean["question_lemmatize"] =  df_clean.apply(lambda x: lemmatizer(x['question_text']), axis=1)
df_clean['question_lemmatize_clean'] = df_clean['question_lemmatize'].str.replace('-PRON-', '')


# In[56]:


plt.figure(figsize=(10,6))
doc_lens = [len(d) for d in df_clean.question_text]
plt.hist(doc_lens, bins = 100)
plt.title('Distribution of Question character length')
plt.ylabel('Number of questions')
plt.xlabel('Question character length')
sns.despine();


# In[ ]:




