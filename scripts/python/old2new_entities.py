import re

entity_dict = {}

with open('nlu.md', 'r') as old:
    with open('nlu_new_new.md', 'w') as new:
        for line in old:
            # print(x)
            line_s = re.split(r"\((.*?)\)", line)
            print(line)
            if(len(line_s) <= 1):
                new.write(line)
            else:
                for block in line_s:
                    if(":" in block):
                        print(line_s)
                        s_block = re.split(r":", block)
                        if s_block[0] in entity_dict and len(s_block[0])>0:
                            new.write(
                                "{\"entity\": \"" + entity_dict[s_block[0]] + "\", \"value\": \"" + s_block[1] + "\"}")
                        elif len(s_block[0])>0:
                            ask = input("is entity(y/n):" + s_block[0]+"\n")
                            if("y" in ask):
                                new_entity = s_block[0][3:]
                                ask = input("is this ok: " + new_entity)
                                if("n" in ask):
                                    new_entity = input("new entity name: ")
                                entity_dict[s_block[0]] = new_entity
                                new.write(
                                    "{\"entity\": \"" + entity_dict[s_block[0]] + "\", \"value\": \"" + s_block[1] + "\"}")
                            elif("n" in ask):
                                new.write(block)
                        else:
                            new.write("\n")
                    else:
                        new.write(block)

with open('entity.dict', 'w') as e_dict:
    e_dict.write(str(entity_dict))
