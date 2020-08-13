## spread_surfaces_food_objects (/tmp/tmpd84t951e/b5997dd125844727b9f026fb54b5e5a3_conversation_tests.md)
* spread_surfaces_food_objects: Can I become infected with the novel coronavirus from food?   <!-- predicted: covid_food: Can I become infected with the novel coronavirus from food? -->
    - utter_spread_surfaces_food_objects   <!-- predicted: utter_covid_food -->


## test_virus (/tmp/tmpd84t951e/b5997dd125844727b9f026fb54b5e5a3_conversation_tests.md)
* test_virus: Should i be tested   <!-- predicted: test_who: Should i be tested -->
    - utter_test_virus   <!-- predicted: utter_test_who -->


## user_no_data (/tmp/tmpd84t951e/b5997dd125844727b9f026fb54b5e5a3_conversation_tests.md)
* user_no_data: Unfortunately I have no personal data with me.
    - utter_user_no_data   <!-- predicted: utter_user_no_further_questions -->


## bot_personality (/tmp/tmpd84t951e/b5997dd125844727b9f026fb54b5e5a3_conversation_tests.md)
* bot_personality: Are you smart?   <!-- predicted: comment_smart: Are you smart? -->
    - utter_bot_personality   <!-- predicted: utter_comment_smart -->


## bot_personal_questions (/tmp/tmpd84t951e/b5997dd125844727b9f026fb54b5e5a3_conversation_tests.md)
* bot_personal_questions: Do you sleep Helen?
    - utter_bot_personal_questions   <!-- predicted: action_default_fallback -->


## bot_sing (/tmp/tmpd84t951e/b5997dd125844727b9f026fb54b5e5a3_conversation_tests.md)
* bot_sing: Do you have voice for singing?
    - utter_bot_sing   <!-- predicted: action_default_fallback -->


## bot_sports (/tmp/tmpd84t951e/b5997dd125844727b9f026fb54b5e5a3_conversation_tests.md)
* bot_sports: What is your favorite sports team?
    - utter_bot_sports   <!-- predicted: action_default_fallback -->


## bot_worst_experience (/tmp/tmpd84t951e/b5997dd125844727b9f026fb54b5e5a3_conversation_tests.md)
* bot_worst_experience: Tell me your toughest experience.
    - utter_bot_worst_experience   <!-- predicted: action_default_fallback -->


## cc_deepest_point (/tmp/tmpd84t951e/b5997dd125844727b9f026fb54b5e5a3_conversation_tests.md)
* cc_deepest_point: What is the deepest point on earth?
    - utter_cc_deepest_point   <!-- predicted: action_default_fallback -->


## cc_fun_fact (/tmp/tmpd84t951e/b5997dd125844727b9f026fb54b5e5a3_conversation_tests.md)
* cc_fun_fact: You know interesting facts?
    - utter_cc_fun_fact   <!-- predicted: action_default_fallback -->


## cc_geography (/tmp/tmpd84t951e/b5997dd125844727b9f026fb54b5e5a3_conversation_tests.md)
* cc_geography: Where is America?   <!-- predicted: cc_geography: Where is [America]{"entity": "world_region", "value": "US"}? -->
    - slot{"world_region": "US"}
    - utter_cc_geography   <!-- predicted: action_default_fallback -->


## cc_highest_building (/tmp/tmpd84t951e/b5997dd125844727b9f026fb54b5e5a3_conversation_tests.md)
* cc_highest_building: What is the biggest building on earth?
    - utter_cc_highest_building   <!-- predicted: action_default_fallback -->


## covid_schools (/tmp/tmpd84t951e/b5997dd125844727b9f026fb54b5e5a3_conversation_tests.md)
* covid_schools: When is school opening
    - utter_covid_schools   <!-- predicted: action_default_fallback -->


## covid_situation (/tmp/tmpd84t951e/b5997dd125844727b9f026fb54b5e5a3_conversation_tests.md)
* covid_situation: Which country has the highest cases?
    - utter_covid_situation   <!-- predicted: utter_want_to_add_country -->


## covid_situation_deaths (/tmp/tmpd84t951e/b5997dd125844727b9f026fb54b5e5a3_conversation_tests.md)
* covid_situation_deaths: how many covid 19 death cases in [Netherlands]{"entity": "country_code", "value": "NL"}?   <!-- predicted: covid_current_statistics: how many covid 19 death cases in [Netherlands]{"entity": "country_code", "value": "NL"}? -->
    - slot{"country_code": "NL"}
    - action_search_stats   <!-- predicted: action_default_fallback -->
    - utter_covid_situation_deaths   <!-- predicted: utter_fallback_first -->


## covid_situation_infected (/tmp/tmpd84t951e/b5997dd125844727b9f026fb54b5e5a3_conversation_tests.md)
* covid_situation_infected: how many positive cases do we have in [Italy]{"entity": "country_code", "value": "IT"}   <!-- predicted: cc_geography: how many positive cases do we have in [Italy]{"entity": "country_code", "value": "IT"} -->
    - slot{"country_code": "IT"}
    - action_search_stats   <!-- predicted: action_default_fallback -->
    - utter_covid_situation_infected   <!-- predicted: utter_fallback_first -->


## covid_situation_infected_critical (/tmp/tmpd84t951e/b5997dd125844727b9f026fb54b5e5a3_conversation_tests.md)
* covid_situation_infected_critical: how many seriously infected people there in the [Spain]{"entity": "country_code", "value": "ES"}?   <!-- predicted: covid_situation_infected_critical: how many seriously infected people there in [the Spain](country_code)? -->
    - slot{"country_code": "the Spain"}
    - action_search_stats
    - utter_covid_situation_infected_critical


## covid_situation_last_update (/tmp/tmpd84t951e/b5997dd125844727b9f026fb54b5e5a3_conversation_tests.md)
* covid_situation_last_update: What are todays values for [Bangladesh]{"entity": "country_code", "value": "BD"}
    - slot{"country_code": "BD"}
    - action_search_stats
    - utter_covid_situation_last_update   <!-- predicted: utter_want_to_add_country -->


## covid_situation_recovered (/tmp/tmpd84t951e/b5997dd125844727b9f026fb54b5e5a3_conversation_tests.md)
* covid_situation_recovered: how many recovered there are in [Russia]{"entity": "country_code", "value": "RU"}?
    - slot{"country_code": "RU"}
    - action_search_stats
    - utter_covid_situation_recovered   <!-- predicted: utter_covid_no_country_current_statistics -->


## covid_situation_tested (/tmp/tmpd84t951e/b5997dd125844727b9f026fb54b5e5a3_conversation_tests.md)
* covid_situation_tested: how many tests were done in [United Kingdom]{"entity": "country_code", "value": "GB"}?
    - slot{"country_code": "GB"}
    - action_search_stats
    - utter_covid_situation_tested   <!-- predicted: utter_want_to_add_country -->


## bot_games (/tmp/tmpd84t951e/b5997dd125844727b9f026fb54b5e5a3_conversation_tests.md)
* bot_games: Do you like video games?
    - utter_bot_games   <!-- predicted: action_default_fallback -->


## greeting_hello (/tmp/tmpd84t951e/b5997dd125844727b9f026fb54b5e5a3_conversation_tests.md)
* greeting_hello: My name is Pankaj Tandia
    - utter_greeting_hello   <!-- predicted: action_check_Bot_Introduced -->


## bot_hobbies (/tmp/tmpd84t951e/b5997dd125844727b9f026fb54b5e5a3_conversation_tests.md)
* bot_hobbies: Tell me any fun activity to do.
    - utter_bot_hobbies   <!-- predicted: action_default_fallback -->


## prevention_medical_attention (/tmp/tmpd84t951e/b5997dd125844727b9f026fb54b5e5a3_conversation_tests.md)
* prevention_medical_attention: My temperature is above 39 degrees. Should I worry?
    - utter_prevention_medical_attention   <!-- predicted: utter_prevenion_medical_attention -->


