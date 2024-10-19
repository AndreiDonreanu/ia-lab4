

f=open("document.txt","r")

content=f.readlines()

new=''.join(content)
words=new.split()

dictionarul=dict()

for cuvant in words:
    if(dictionarul.get(cuvant)==None):
        dictionarul.update({cuvant:1})
    else:
        i=dictionarul.get(cuvant)+1
        dictionarul.update({cuvant:i})


print(dictionarul)
