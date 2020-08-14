## test_who (/tmp/tmppu_ax5x7/f0613c9ef3ba4a0aae8a6434a0684a2d_conversation_tests.md)
* test_who: How do I get tested   <!-- predicted: test_virus: How do I get tested -->
    - utter_test_who   <!-- predicted: utter_test_virus -->


## bot_music (/tmp/tmppu_ax5x7/f0613c9ef3ba4a0aae8a6434a0684a2d_conversation_tests.md)
* bot_music: Do you like to sing?   <!-- predicted: bot_sing: Do you like to sing? -->
    - utter_bot_music   <!-- predicted: action_default_fallback -->


## user_no_data (/tmp/tmppu_ax5x7/f0613c9ef3ba4a0aae8a6434a0684a2d_conversation_tests.md)
* user_no_data: Unfortunately I have no personal data with me.
    - utter_user_no_data   <!-- predicted: utter_user_no_further_questions -->


## prevention_vaccine (/tmp/tmppu_ax5x7/f0613c9ef3ba4a0aae8a6434a0684a2d_conversation_tests.md)
* prevention_vaccine: Is there a vaccine, drug or treatment for COVID-19?   <!-- predicted: prevention_medicine: Is there a vaccine, drug or treatment for COVID-19? -->
    - utter_prevention_vaccine   <!-- predicted: utter_prevention_medicine -->


## bot_personal_questions (/tmp/tmppu_ax5x7/f0613c9ef3ba4a0aae8a6434a0684a2d_conversation_tests.md)
* bot_personal_questions: Do you sleep Helen?
    - utter_bot_personal_questions   <!-- predicted: action_default_fallback -->


## bot_sing (/tmp/tmppu_ax5x7/f0613c9ef3ba4a0aae8a6434a0684a2d_conversation_tests.md)
* bot_sing: Do you have voice for singing?
    - utter_bot_sing   <!-- predicted: action_default_fallback -->


## bot_sports (/tmp/tmppu_ax5x7/f0613c9ef3ba4a0aae8a6434a0684a2d_conversation_tests.md)
* bot_sports: What is your favorite sports team?
    - utter_bot_sports   <!-- predicted: action_default_fallback -->


## bot_worst_experience (/tmp/tmppu_ax5x7/f0613c9ef3ba4a0aae8a6434a0684a2d_conversation_tests.md)
* bot_worst_experience: Tell me your toughest experience.
    - utter_bot_worst_experience   <!-- predicted: action_default_fallback -->


## cc_deepest_point (/tmp/tmppu_ax5x7/f0613c9ef3ba4a0aae8a6434a0684a2d_conversation_tests.md)
* cc_deepest_point: What is the deepest point on earth?
    - utter_cc_deepest_point   <!-- predicted: action_default_fallback -->


## cc_fun_fact (/tmp/tmppu_ax5x7/f0613c9ef3ba4a0aae8a6434a0684a2d_conversation_tests.md)
* cc_fun_fact: You know interesting facts?
    - utter_cc_fun_fact   <!-- predicted: action_default_fallback -->


## cc_geography (/tmp/tmppu_ax5x7/f0613c9ef3ba4a0aae8a6434a0684a2d_conversation_tests.md)
* cc_geography: Where is America?   <!-- predicted: cc_geography: Where is [America]{"entity": "world_region", "value": "US"}? -->
    - slot{"world_region": "US"}
    - utter_cc_geography   <!-- predicted: action_default_fallback -->


## cc_highest_building (/tmp/tmppu_ax5x7/f0613c9ef3ba4a0aae8a6434a0684a2d_conversation_tests.md)
* cc_highest_building: What is the biggest building on earth?
    - utter_cc_highest_building   <!-- predicted: action_default_fallback -->


## covid_aftereffects_immunity (/tmp/tmppu_ax5x7/f0613c9ef3ba4a0aae8a6434a0684a2d_conversation_tests.md)
* covid_aftereffects_immunity: Can I person get sick twice?   <!-- predicted: covid_immunity: Can I person get sick twice? -->
    - utter_covid_aftereffects_immunity   <!-- predicted: utter_covid_immunity -->


## covid_situation (/tmp/tmppu_ax5x7/f0613c9ef3ba4a0aae8a6434a0684a2d_conversation_tests.md)
* covid_situation: Which country has the highest cases?
    - utter_covid_situation   <!-- predicted: utter_want_to_add_country -->


## covid_situation_deaths (/tmp/tmppu_ax5x7/f0613c9ef3ba4a0aae8a6434a0684a2d_conversation_tests.md)
* covid_situation_deaths: how many covid 19 death cases in [Netherlands]{"entity": "country_code", "value": "NL"}?   <!-- predicted: covid_situation: how many covid 19 death cases in [Netherlands]{"entity": "country_code", "value": "NL"}? -->
    - slot{"country_code": "NL"}
    - action_search_stats
    - utter_covid_situation_deaths   <!-- predicted: utter_want_to_add_country -->


## covid_situation_infected_critical (/tmp/tmppu_ax5x7/f0613c9ef3ba4a0aae8a6434a0684a2d_conversation_tests.md)
* covid_situation_infected_critical: how many seriously infected people there in the [Spain]{"entity": "country_code", "value": "ES"}?
    - slot{"country_code": "ES"}
    - action_search_stats
    - utter_covid_situation_infected_critical   <!-- predicted: utter_covid_situation_infected -->


## covid_situation_last_update (/tmp/tmppu_ax5x7/f0613c9ef3ba4a0aae8a6434a0684a2d_conversation_tests.md)
* covid_situation_last_update: What are todays values for [Bangladesh]{"entity": "country_code", "value": "BD"}
    - slot{"country_code": "BD"}
    - action_search_stats
    - utter_covid_situation_last_update   <!-- predicted: utter_want_to_add_country -->


## bot_games (/tmp/tmppu_ax5x7/f0613c9ef3ba4a0aae8a6434a0684a2d_conversation_tests.md)
* bot_games: Do you like video games?
    - utter_bot_games   <!-- predicted: action_default_fallback -->


## greeting_hello (/tmp/tmppu_ax5x7/f0613c9ef3ba4a0aae8a6434a0684a2d_conversation_tests.md)
* greeting_hello: My name is Pankaj Tandia
    - utter_greeting_hello   <!-- predicted: action_check_Bot_Introduced -->


## myths_conspiracy_fakenews (/tmp/tmppu_ax5x7/f0613c9ef3ba4a0aae8a6434a0684a2d_conversation_tests.md)
* myths_conspiracy_fakenews: They told us that if you eat the fruits like lemons there is a way it fight it.   <!-- predicted: myth_conspiracy_fakenews: They told us that if you eat the fruits like lemons there is a way it fight it. -->
    - utter_myths_conspiracy_fakenews   <!-- predicted: utter_myth_conspiracy_fakenews -->


## bot_hobbies (/tmp/tmppu_ax5x7/f0613c9ef3ba4a0aae8a6434a0684a2d_conversation_tests.md)
* bot_hobbies: Tell me any fun activity to do.
    - utter_bot_hobbies   <!-- predicted: action_default_fallback -->


## prevention_medical_attention (/tmp/tmppu_ax5x7/f0613c9ef3ba4a0aae8a6434a0684a2d_conversation_tests.md)
* prevention_medical_attention: My temperature is above 39 degrees. Should I worry?
    - utter_prevention_medical_attention   <!-- predicted: utter_prevenion_medical_attention -->


