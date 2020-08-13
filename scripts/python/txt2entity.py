import os

entries = os.listdir('lookup_tables/')
with open('e_country_new.txt', 'w') as e:
    for entry in entries:
        if (entry[-4:]==".txt" and len(entry)==6):
            country = entry[:-4]
            with open('lookup_tables/'+ entry, 'r') as c:
                for x in range(2):
                    entity=c.readline()[:-1]
                    if x==0:
                        e.write("- ["+entity.lower()+"]{\"entity\": \"country_code\", \"value\": \"" +country+"\"}\n" )
                    e.write("- ["+entity+"]{\"entity\": \"country_code\", \"value\": \"" +country+"\"}\n" )





"""
- [Spain]{"entity": "country_code", "value": "ES"}
"""