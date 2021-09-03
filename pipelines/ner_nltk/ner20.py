import nltk
nltk.download('words')
import glob
import os
from nltk import word_tokenize,pos_tag,ne_chunk
import csv
#from nltk.corpus import state_union
#from nltk.tokenize import PunktSentenceTokenizer

#train_text=state_union.raw(text)
#sample_text=state_union.raw(text)
path="../Lorimer/"
stopWords=[
'Monday', 
'Tuesday', 
'Wednesday', 
'Thursday', 
'Friday', 
'Saturday', 
'Sunday', 
'January', 
'February', 
'March', 
'April', 
'May', 
'June', 
'July', 
'August', 
'September', 
'October', 
'November', 
'December', 
'Mondays', 
'Tuesdays', 
'Wednesdays', 
'Thursdays', 
'Fridays', 
'Saturdays', 
'Sundays'
]
ner_full=[]
filenames=[]
entity_names=[]
all_entity_names=[]
for filename in glob.glob(os.path.join(path, '*.txt')):
    entities_filtered=[]
    entity_names=[]
    with open(filename, 'r') as file:
        count=0
        reachedCount=False
        filename1=filename.replace("../Lorimer/","")
        filenames.append(filename1)
        data = file.read().replace('\n', '')
        tokens = word_tokenize(data)
        #print(tokens)
        pos_tags=nltk.pos_tag(tokens)
        #print(pos_tag)
        entities = ne_chunk(pos_tags)
        #print(named_entities)
        for chunk in entities:
            count+=1
            if count>=20:
                break
            if hasattr(chunk, 'label'):
                #print(chunk.label())
                entity=str(chunk.label())
                #print(chunk.label())
                name=chunk[0][0]
                if name not in stopWords: 
                    entity_names.append(name)
                    #print(name)
                    pos_tag=chunk[0][1]
                    #print(pos_tag)
                    string1=str(entity)+","+str(name)+","+pos_tag
                    entities_filtered.append(string1)
    all_entity_names.append(entity_names)
    ner_full.append(entities_filtered)

headers=[]
for fe in filenames: 
    headers.append(fe)

with open('allEntities20.csv', 'w') as f:
    writer = csv.writer(f)
    # write the header
    for i in range(len(ner_full)): 
        f.write(str(filenames[i]))
        f.write("\n")
        f.write("\n")
        for k in range(len(ner_full[i])): 
            f.write(str(ner_full[i][k])+",")
            f.write("\n")
        f.write("\n")

'''
with open('allEntityNames20.csv', 'w') as f:
    writer = csv.writer(f)
    # write the header
    for i in range(len(all_entity_names)): 
        f.write(str(filenames[i]))
        f.write("\n")
        f.write("\n")
        for k in range(len(all_entity_names[i])): 
            f.write(str(all_entity_names[i][k])+",")
            f.write("\n")
        f.write("\n")
'''

with open('all-entity-names20.csv', 'w') as f:
    for i in range(len(all_entity_names) ): 
        values = ','.join(str(v) for v in all_entity_names[i])
        f.write(str(filenames[i])+",")
        f.write(values)
        f.write("\n")