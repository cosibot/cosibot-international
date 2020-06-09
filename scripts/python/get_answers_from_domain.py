import bios
import fire
import json
import os
import csv

## Extract responses from domain
## python get_answers_from_domain.py extract_answers

## Import responses to domain
## python get_answers_from_domain.py import_answers


class Process_domain(object):
    def extract_answers(self):
        domain_file_path = "../../bot/domain.yml"
        domain_file_dict = bios.read(domain_file_path)

        with open('domain_answers.csv', mode='w', newline='') as domain_answers_file:
            domain_answers_writer = csv.writer(domain_answers_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            for key in domain_file_dict["responses"].keys():
                key = key
                custom_key = 0
                for custom in domain_file_dict["responses"][key]:
                    for answer in custom["custom"]["answers"]:
                        answer_type = answer["type"]
                        
                        if answer_type == "html":
                            answer_export = "text"
                        else:
                            answer_export = answer_type

                        try:
                            domain_answers_writer.writerow([key, "custom_{}".format(custom_key) , answer_type, answer[answer_export]])
                        except:
                            domain_answers_writer.writerow([key, "custom_{}".format(custom_key) , answer_type, answer])
                    custom_key+=1



    def import_answers(self):
        domain_file_path = "../../bot/domain.yml"
        domain_file_dict = bios.read(domain_file_path)

        #print(domain_file_dict["responses"])
        responses = {}

        with open('domain_answers_updated.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                custom_level = int(row[1].split('_')[1])
                
                if row[0] in responses.keys():
                    if actual_level == custom_level:
                        pass
                    else:
                        responses[row[0]].append({"custom":{"answers":[]}})
                        actual_level = custom_level    
                else:
                    responses[row[0]] = [{"custom":{"answers":[]}}]
                    actual_level = custom_level

                
                if row[2] == "html":
                    answer_import = "text"
                    responses[row[0]][custom_level]["custom"]["answers"].append({"type":row[2],"{}".format(answer_import):row[3]})
                elif row[2] == "command":
                    responses[row[0]][custom_level]["custom"]["answers"].append(json.loads(row[3].replace("\'", "\"")))
                elif row[2] == "hints":
                    responses[row[0]][custom_level]["custom"]["answers"].append(json.loads(row[3].replace("\'", "\"")))
                elif row[2] == "links":
                    responses[row[0]][custom_level]["custom"]["answers"].append({"type":row[2],"{}".format(row[2]):json.loads(row[3].replace("\'", "\""))})
                elif row[2] == "multichoice":
                    print(line_count)
                    print(type(row[3]))
                    print(row[3])
                    print(row[3].replace("\'", "\""))
                    responses[row[0]][custom_level]["custom"]["answers"].append(json.loads((row[3].replace("\"", "\\\"")).replace("\'", "\"")))
                    #break
                else:
                    responses[row[0]][custom_level]["custom"]["answers"].append({"type":row[2],"{}".format(row[2]):row[3]})

                line_count += 1

        
        domain_updated = {
            "session_config":domain_file_dict["session_config"],
            "slots":domain_file_dict["slots"],
            "entities":domain_file_dict["entities"],
            "actions":domain_file_dict["actions"],
            "intents":domain_file_dict["intents"],
            "responses": responses
        }
          
      
        print(responses)
        print(line_count)
        bios.write('../../bot/domain_updated.yml', domain_updated)



if __name__ == "__main__":
    fire.Fire(Process_domain)
    #app.run()