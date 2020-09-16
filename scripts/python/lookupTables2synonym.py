import os

entries = os.listdir('lookup_tables/')
with open('synonym.txt', 'w') as s:
    for entry in entries:
        #print(entry[:-4])
        if (entry[-4:]==".txt"):
            s.write("## synonym:"+entry[:-4])
            with open('lookup_tables/'+ entry, 'r') as f:
                data = f.read().split("\n")
                for line in data:
                    #print(len(line))
                    if(len(line)>0):
                        s.write("\n- "+ line)
                    else:
                        s.write("\n\n")
                        
entries = os.listdir('lookup_tables/yes')
with open('lookup.txt', 'w') as l:
    for entry in entries:
        l.write("## lookup:"+entry[:-4]+"\n"+"lookup_tables/" + entry +"\n\n")


"""
## synonym:EG
- República Árabe do Egipto
- República Árabe do Egito
- Egipto
- Egito
- Arab Republic of Egypt
- Egypt

## lookup:joke
lookup_tables/joke.txt

"""