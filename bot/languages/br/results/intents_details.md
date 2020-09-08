# Intents
|              class              |support|f1-score|                     confused_with                     |
|---------------------------------|------:|-------:|-------------------------------------------------------|
|country                          |    254|   0.996|covid_current_statistics(1), covid_situation(1)        |
|covid_symptoms                   |    187|   0.989|test_virus(2), prevention_medical_attention(1)         |
|covid_sars                       |    181|   1.000|N/A                                                    |
|cc_philosophical                 |    178|   0.997|user_love(1)                                           |
|cc_religion                      |    143|   1.000|N/A                                                    |
|bot_sexual                       |    134|   0.989|bot_personal_questions(1)                              |
|spread_pets                      |    121|   1.000|N/A                                                    |
|spread_general                   |    119|   0.979|N/A                                                    |
|bot_personal_questions           |    118|   0.979|bot_sexual(2)                                          |
|bot_capabilities                 |    112|   0.996|cc_lets_talk(1)                                        |
|prevention_medical_attention     |    104|   0.971|prevention_home(1), covid_info(1)                      |
|vocative_thank_you               |    103|   0.912|comment_positive(9), user_no_further_questions(1)      |
|user_no_further_questions        |     99|   0.955|vocative_thank_you(3)                                  |
|spread_no_symptoms               |     94|   1.000|N/A                                                    |
|covid_situation                  |     89|   0.989|N/A                                                    |
|comment_offense                  |     88|   0.994|N/A                                                    |
|myth_transmission_hot_areas      |     85|   1.000|N/A                                                    |
|prevention_vaccine               |     83|   0.881|prevention_medicine(13)                                |
|spread_risk                      |     82|   0.994|covid_worry(1)                                         |
|prevention_general               |     82|   1.000|N/A                                                    |
|covid_surfaces                   |     78|   1.000|N/A                                                    |
|prevention_medicine              |     77|   0.871|prevention_vaccine(6)                                  |
|bot_worst_experience             |     74|   1.000|N/A                                                    |
|covid_info                       |     73|   0.986|coronavirus_info(1)                                    |
|greeting_goodbye                 |     68|   0.962|greeting_hello(5)                                      |
|mask_general                     |     67|   0.992|mask_use_put(1)                                        |
|covid_worry                      |     66|   0.985|prevention_medical_attention(1)                        |
|comment_positive                 |     61|   0.870|vocative_thank_you(3), comment_smart(1)                |
|prevention_touch                 |     60|   1.000|N/A                                                    |
|user_happy                       |     59|   0.991|prevention_medical_attention(1)                        |
|bot_games                        |     59|   1.000|N/A                                                    |
|vocative_help                    |     59|   0.992|N/A                                                    |
|cc_geography                     |     57|   1.000|N/A                                                    |
|prevention_respiratory_hygiene   |     54|   1.000|N/A                                                    |
|covid_incubation                 |     53|   0.971|spread_general(3)                                      |
|cc_fun_fact                      |     53|   0.981|N/A                                                    |
|covid_immunity                   |     52|   0.990|myth_alcohol(1)                                        |
|greeting_hello                   |     52|   0.926|vocative_thank_you(1), greeting_how_are_you(1)         |
|cc_politics                      |     51|   1.000|N/A                                                    |
|mask_use_put                     |     51|   0.990|N/A                                                    |
|cc_weather                       |     50|   1.000|N/A                                                    |
|vocative_call                    |     48|   0.960|N/A                                                    |
|covid_situation_deaths           |     48|   0.979|covid_mortality_rate(1), covid_situation_last_update(1)|
|vocative_yes                     |     48|   0.968|greeting_how_are_you(2), vocative_thank_you(1)         |
|user_no_data                     |     48|   1.000|N/A                                                    |
|user_love                        |     47|   0.979|N/A                                                    |
|vocative_sorry                   |     47|   1.000|N/A                                                    |
|comment_negative                 |     46|   0.978|comment_racist(1), comment_offense(1)                  |
|bot_appearance                   |     46|   0.978|greeting_how_are_you(1), comment_smart(1)              |
|comment_racist                   |     46|   0.989|N/A                                                    |
|bot_real                         |     45|   1.000|N/A                                                    |
|travel_while                     |     44|   1.000|N/A                                                    |
|features_date                    |     44|   1.000|N/A                                                    |
|greeting_how_are_you             |     43|   0.889|bot_name(2), comment_smart(1)                          |
|covid_preexisting_illness        |     43|   1.000|N/A                                                    |
|prevention_home                  |     43|   0.977|prevention_medical_attention(1)                        |
|spread_air                       |     43|   1.000|N/A                                                    |
|spread_animals                   |     43|   1.000|N/A                                                    |
|user_angry                       |     41|   1.000|N/A                                                    |
|cc_newspaper                     |     41|   1.000|N/A                                                    |
|spread_feces                     |     40|   1.000|N/A                                                    |
|features_time                    |     40|   1.000|N/A                                                    |
|bot_residence                    |     40|   0.974|bot_personal_questions(2)                              |
|bot_languages                    |     40|   1.000|N/A                                                    |
|travel_after                     |     39|   1.000|N/A                                                    |
|user_friend                      |     39|   0.987|user_love(1)                                           |
|vocative_no                      |     39|   0.960|user_no_further_questions(3)                           |
|cc_chickegg                      |     37|   1.000|N/A                                                    |
|myth_hot_bath                    |     37|   1.000|N/A                                                    |
|bot_availability                 |     37|   1.000|N/A                                                    |
|prevention_clean_hands           |     37|   1.000|N/A                                                    |
|cc_joke                          |     37|   0.986|cc_fun_fact(1)                                         |
|mask_use_after                   |     36|   1.000|N/A                                                    |
|user_scared                      |     36|   1.000|N/A                                                    |
|travel_before                    |     35|   1.000|N/A                                                    |
|bot_hobbies                      |     34|   1.000|N/A                                                    |
|bot_music                        |     34|   1.000|N/A                                                    |
|covid_situation_last_update      |     33|   0.985|N/A                                                    |
|covid_schools                    |     32|   1.000|N/A                                                    |
|bot_sports                       |     32|   1.000|N/A                                                    |
|bot_version                      |     32|   1.000|N/A                                                    |
|myth_cold_weather                |     32|   1.000|N/A                                                    |
|bot_goal                         |     31|   1.000|N/A                                                    |
|cc_lets_talk                     |     30|   0.893|vocative_call(4), comment_smart(1)                     |
|prevention_measures              |     30|   1.000|N/A                                                    |
|comment_smart                    |     30|   0.923|N/A                                                    |
|bot_books                        |     29|   1.000|N/A                                                    |
|covid_situation_infected         |     28|   0.982|covid_situation(1)                                     |
|prevention_distance              |     27|   1.000|N/A                                                    |
|covid_situation_tested           |     27|   1.000|N/A                                                    |
|covid_meaning                    |     27|   1.000|N/A                                                    |
|covid_current_statistics         |     26|   0.981|N/A                                                    |
|prevention_informed              |     26|   1.000|N/A                                                    |
|bot_name                         |     26|   0.963|N/A                                                    |
|cc_deepest_point                 |     26|   1.000|N/A                                                    |
|covid_situation_recovered        |     26|   1.000|N/A                                                    |
|coronavirus_info                 |     25|   0.917|spread_general(2), covid_symptoms(1)                   |
|bot_fear                         |     24|   1.000|N/A                                                    |
|test_virus                       |     24|   0.923|N/A                                                    |
|covid_situation_infected_critical|     24|   1.000|N/A                                                    |
|bot_sing                         |     23|   1.000|N/A                                                    |
|bot_origin                       |     22|   1.000|N/A                                                    |
|bot_personality                  |     21|   0.865|comment_positive(4), comment_smart(1)                  |
|user_particles                   |     21|   0.923|vocative_you_welcome(1), cc_fun_fact(1)                |
|bot_movies                       |     21|   1.000|N/A                                                    |
|quarantine_general               |     19|   0.947|quarantine_when_who_howlong(1)                         |
|cc_moon                          |     19|   1.000|N/A                                                    |
|covid_crisis_howlong             |     19|   0.973|covid_duration(1)                                      |
|vocative_you_welcome             |     18|   0.848|greeting_how_are_you(2), user_no_further_questions(2)  |
|myth_alcohol                     |     17|   0.971|N/A                                                    |
|covid_tech4covid                 |     16|   1.000|N/A                                                    |
|myth_packages                    |     16|   1.000|N/A                                                    |
|myth_conspiracy_fakenews         |     16|   1.000|N/A                                                    |
|cc_highest_building              |     16|   1.000|N/A                                                    |
|quarantine_dogwalking            |     14|   1.000|N/A                                                    |
|covid_origins                    |     13|   0.929|N/A                                                    |
|covid_treatment                  |     13|   0.917|prevention_medicine(2)                                 |
|prevention_disinfection          |     13|   1.000|N/A                                                    |
|myth_garlic                      |     12|   1.000|N/A                                                    |
|quaratine_how_it_works           |     12|   0.909|greeting_hello(1), quarantine_general(1)               |
|covid_sex                        |     12|   1.000|N/A                                                    |
|prevention_cloroquina            |     11|   1.000|N/A                                                    |
|covid_aftereffects               |     11|   1.000|N/A                                                    |
|myth_uv_lamps                    |     11|   1.000|N/A                                                    |
|covid_volunteer                  |     10|   0.947|vocative_help(1)                                       |
|covid_duration                   |      9|   0.824|covid_origins(2)                                       |
|prevention_ivermectina           |      9|   1.000|N/A                                                    |
|quarantine_dos_and_donts         |      9|   1.000|N/A                                                    |
|myth_5G                          |      9|   1.000|N/A                                                    |
|myth_thermal_scanner             |      8|   1.000|N/A                                                    |
|myth_pneumonia_vaccine           |      8|   1.000|N/A                                                    |
|myth_mosquitoes                  |      7|   1.000|N/A                                                    |
|ebola                            |      7|   1.000|N/A                                                    |
|covid_mortality_rate             |      7|   0.933|N/A                                                    |
|mask_visors                      |      6|   1.000|N/A                                                    |
|covid_disease_process            |      6|   1.000|N/A                                                    |
|myth_air_conditioning            |      6|   1.000|N/A                                                    |
|start                            |      6|   1.000|N/A                                                    |
|economy_consequences             |      6|   1.000|N/A                                                    |
|covid_cosibot                    |      6|   1.000|N/A                                                    |
|quarantine_when_who_howlong      |      5|   0.909|N/A                                                    |
|spread_surfaces_food_objects     |      5|   1.000|N/A                                                    |
|covid_pandemic                   |      5|   1.000|N/A                                                    |
|covid_food                       |      5|   1.000|N/A                                                    |
|test_who                         |      5|   0.750|test_virus(2)                                          |
|myth_saline                      |      4|   1.000|N/A                                                    |
|myth_antibiotics                 |      4|   1.000|N/A                                                    |
|myth_influenza                   |      4|   1.000|N/A                                                    |
|myth_sesame_oil                  |      4|   1.000|N/A                                                    |
|covid_register                   |      4|   1.000|N/A                                                    |
|myth_hand_dryer                  |      4|   1.000|N/A                                                    |
|quarantine_control               |      3|   1.000|N/A                                                    |
|covid_dangerous                  |      3|   1.000|N/A                                                    |
|covid_procedure_after_infection  |      2|   1.000|N/A                                                    |
|covid_babys_children             |      2|   1.000|N/A                                                    |
|quarantine_toiletpaper           |      2|   1.000|N/A                                                    |



# Confusion table
|           intent           |       confused_with        |count|
|----------------------------|----------------------------|----:|
|prevention_vaccine          |prevention_medicine         |   13|
|vocative_thank_you          |comment_positive            |    9|
|prevention_medicine         |prevention_vaccine          |    6|
|greeting_goodbye            |greeting_hello              |    5|
|cc_lets_talk                |vocative_call               |    4|
|bot_personality             |comment_positive            |    4|
|vocative_no                 |user_no_further_questions   |    3|
|user_no_further_questions   |vocative_thank_you          |    3|
|covid_incubation            |spread_general              |    3|
|comment_positive            |vocative_thank_you          |    3|
|greeting_how_are_you        |bot_name                    |    2|
|test_who                    |test_virus                  |    2|
|vocative_you_welcome        |greeting_how_are_you        |    2|
|coronavirus_info            |spread_general              |    2|
|covid_symptoms              |test_virus                  |    2|
|vocative_yes                |greeting_how_are_you        |    2|
|bot_personal_questions      |bot_sexual                  |    2|
|vocative_you_welcome        |user_no_further_questions   |    2|
|covid_duration              |covid_origins               |    2|
|bot_residence               |bot_personal_questions      |    2|
|covid_treatment             |prevention_medicine         |    2|
|cc_joke                     |cc_fun_fact                 |    1|
|cc_lets_talk                |comment_smart               |    1|
|bot_capabilities            |cc_lets_talk                |    1|
|bot_sexual                  |bot_personal_questions      |    1|
|quaratine_how_it_works      |greeting_hello              |    1|
|vocative_yes                |vocative_thank_you          |    1|
|vocative_thank_you          |user_no_further_questions   |    1|
|quaratine_how_it_works      |quarantine_general          |    1|
|user_particles              |vocative_you_welcome        |    1|
|greeting_hello              |greeting_how_are_you        |    1|
|prevention_home             |prevention_medical_attention|    1|
|covid_symptoms              |prevention_medical_attention|    1|
|bot_appearance              |greeting_how_are_you        |    1|
|bot_appearance              |comment_smart               |    1|
|user_particles              |cc_fun_fact                 |    1|
|user_happy                  |prevention_medical_attention|    1|
|greeting_hello              |vocative_thank_you          |    1|
|comment_positive            |comment_smart               |    1|
|user_friend                 |user_love                   |    1|
|covid_situation_infected    |covid_situation             |    1|
|cc_philosophical            |user_love                   |    1|
|greeting_how_are_you        |comment_smart               |    1|
|covid_worry                 |prevention_medical_attention|    1|
|mask_general                |mask_use_put                |    1|
|coronavirus_info            |covid_symptoms              |    1|
|spread_risk                 |covid_worry                 |    1|
|comment_negative            |comment_racist              |    1|
|comment_negative            |comment_offense             |    1|
|covid_situation_deaths      |covid_mortality_rate        |    1|
|covid_situation_deaths      |covid_situation_last_update |    1|
|country                     |covid_current_statistics    |    1|
|country                     |covid_situation             |    1|
|quarantine_general          |quarantine_when_who_howlong |    1|
|prevention_medical_attention|prevention_home             |    1|
|prevention_medical_attention|covid_info                  |    1|
|covid_volunteer             |vocative_help               |    1|
|covid_immunity              |myth_alcohol                |    1|
|covid_info                  |coronavirus_info            |    1|
|bot_personality             |comment_smart               |    1|
|covid_crisis_howlong        |covid_duration              |    1|
