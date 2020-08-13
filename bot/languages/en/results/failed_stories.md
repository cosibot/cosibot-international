## test_who (/tmp/tmpn78xj0rf/7a0eb8d009cc4c5b89be5e92cb6de4e0_conversation_tests.md)
* test_who: How do I get tested   <!-- predicted: test_virus: How do I get tested -->
    - utter_test_who   <!-- predicted: action_default_fallback -->


## bot_music (/tmp/tmpn78xj0rf/7a0eb8d009cc4c5b89be5e92cb6de4e0_conversation_tests.md)
* bot_music: Do you like to sing?   <!-- predicted: bot_sing: Do you like to sing? -->
    - utter_bot_music   <!-- predicted: action_default_fallback -->


## user_no_data (/tmp/tmpn78xj0rf/7a0eb8d009cc4c5b89be5e92cb6de4e0_conversation_tests.md)
* user_no_data: Unfortunately I have no personal data with me.
    - utter_user_no_data   <!-- predicted: utter_user_no_further_questions -->


## vocative_thank_you (/tmp/tmpn78xj0rf/7a0eb8d009cc4c5b89be5e92cb6de4e0_conversation_tests.md)
* vocative_thank_you: thanks, Helen!
    - utter_vocative_thank_you
    - action_listen   <!-- predicted: utter_further_questions -->


## bot_personal_questions (/tmp/tmpn78xj0rf/7a0eb8d009cc4c5b89be5e92cb6de4e0_conversation_tests.md)
* bot_personal_questions: Do you sleep Helen?
    - utter_bot_personal_questions   <!-- predicted: action_default_fallback -->


## bot_sing (/tmp/tmpn78xj0rf/7a0eb8d009cc4c5b89be5e92cb6de4e0_conversation_tests.md)
* bot_sing: Do you have voice for singing?
    - utter_bot_sing   <!-- predicted: action_default_fallback -->


## bot_sports (/tmp/tmpn78xj0rf/7a0eb8d009cc4c5b89be5e92cb6de4e0_conversation_tests.md)
* bot_sports: What is your favorite sports team?
    - utter_bot_sports   <!-- predicted: action_default_fallback -->


## bot_worst_experience (/tmp/tmpn78xj0rf/7a0eb8d009cc4c5b89be5e92cb6de4e0_conversation_tests.md)
* bot_worst_experience: Tell me your toughest experience.
    - utter_bot_worst_experience   <!-- predicted: action_default_fallback -->


## cc_deepest_point (/tmp/tmpn78xj0rf/7a0eb8d009cc4c5b89be5e92cb6de4e0_conversation_tests.md)
* cc_deepest_point: What is the deepest point on earth?
    - utter_cc_deepest_point   <!-- predicted: action_default_fallback -->


## cc_fun_fact (/tmp/tmpn78xj0rf/7a0eb8d009cc4c5b89be5e92cb6de4e0_conversation_tests.md)
* cc_fun_fact: You know interesting facts?
    - utter_cc_fun_fact   <!-- predicted: action_default_fallback -->


## cc_geography (/tmp/tmpn78xj0rf/7a0eb8d009cc4c5b89be5e92cb6de4e0_conversation_tests.md)
* cc_geography: Where is America?   <!-- predicted: cc_geography: Where is [America]{"entity": "world_region", "value": "US"}? -->
    - slot{"world_region": "US"}
    - utter_cc_geography   <!-- predicted: action_default_fallback -->


## cc_highest_building (/tmp/tmpn78xj0rf/7a0eb8d009cc4c5b89be5e92cb6de4e0_conversation_tests.md)
* cc_highest_building: What is the biggest building on earth?
    - utter_cc_highest_building   <!-- predicted: action_default_fallback -->


## cc_newspaper (/tmp/tmpn78xj0rf/7a0eb8d009cc4c5b89be5e92cb6de4e0_conversation_tests.md)
* cc_newspaper: Tell me the news
    - utter_cc_newspaper
    - action_listen   <!-- predicted: action_get_news_request -->


## covid_current_statistics (/tmp/tmpn78xj0rf/7a0eb8d009cc4c5b89be5e92cb6de4e0_conversation_tests.md)
* covid_current_statistics: What can you tell me about the most recent news?
    - utter_covid_current_statistics   <!-- predicted: action_get_news_request -->


## covid_dangerous (/tmp/tmpn78xj0rf/7a0eb8d009cc4c5b89be5e92cb6de4e0_conversation_tests.md)
* covid_dangerous: How contagious is this novel corona virus?   <!-- predicted: spread_risk: How contagious is this novel corona virus? -->
    - utter_covid_dangerous   <!-- predicted: utter_spread_risk -->


## covid_origins (/tmp/tmpn78xj0rf/7a0eb8d009cc4c5b89be5e92cb6de4e0_conversation_tests.md)
* covid_origins: Where did Corona started   <!-- predicted: covid_info: Where did Corona started -->
    - utter_covid_origins   <!-- predicted: utter_covid_info -->


## covid_schools (/tmp/tmpn78xj0rf/7a0eb8d009cc4c5b89be5e92cb6de4e0_conversation_tests.md)
* covid_schools: When is school opening
    - utter_covid_schools   <!-- predicted: action_default_fallback -->


## covid_situation (/tmp/tmpn78xj0rf/7a0eb8d009cc4c5b89be5e92cb6de4e0_conversation_tests.md)
* covid_situation: Which country has the highest cases?
    - utter_covid_situation   <!-- predicted: utter_want_to_add_country -->


## covid_situation_deaths (/tmp/tmpn78xj0rf/7a0eb8d009cc4c5b89be5e92cb6de4e0_conversation_tests.md)
* covid_situation_deaths: how many covid 19 death cases in [Netherlands]{"entity": "country_code", "value": "NL"}?   <!-- predicted: covid_situation: how many covid 19 death cases in [Netherlands]{"entity": "country_code", "value": "NL"}? -->
    - slot{"country_code": "NL"}
    - action_search_stats
    - utter_covid_situation_deaths   <!-- predicted: action_default_fallback -->


## covid_situation_infected_critical (/tmp/tmpn78xj0rf/7a0eb8d009cc4c5b89be5e92cb6de4e0_conversation_tests.md)
* covid_situation_infected_critical: how many seriously infected people there in the [Spain]{"entity": "country_code", "value": "ES"}?   <!-- predicted: covid_situation_infected_critical: how many seriously infected people there in the Spain? -->
    - action_search_stats
    - utter_covid_situation_infected_critical


## covid_situation_last_update (/tmp/tmpn78xj0rf/7a0eb8d009cc4c5b89be5e92cb6de4e0_conversation_tests.md)
* covid_situation_last_update: What are todays values for [Bangladesh]{"entity": "country_code", "value": "BD"}   <!-- predicted: cc_politics: What are todays values for [Bangladesh]{"entity": "country_code", "value": "BD"} -->
    - slot{"country_code": "BD"}
    - action_search_stats   <!-- predicted: action_default_fallback -->
    - utter_covid_situation_last_update


## covid_situation_tested (/tmp/tmpn78xj0rf/7a0eb8d009cc4c5b89be5e92cb6de4e0_conversation_tests.md)
* covid_situation_tested: how many tests were done in [United Kingdom]{"entity": "country_code", "value": "GB"}?
    - slot{"country_code": "GB"}
    - action_search_stats
    - utter_covid_situation_tested   <!-- predicted: action_default_fallback -->


## bot_games (/tmp/tmpn78xj0rf/7a0eb8d009cc4c5b89be5e92cb6de4e0_conversation_tests.md)
* bot_games: Do you like video games?
    - utter_bot_games   <!-- predicted: action_default_fallback -->


## features_date (/tmp/tmpn78xj0rf/7a0eb8d009cc4c5b89be5e92cb6de4e0_conversation_tests.md)
* features_date: Can you tell me which is the date?
    - utter_features_date   <!-- predicted: action_get_date -->


## features_time (/tmp/tmpn78xj0rf/7a0eb8d009cc4c5b89be5e92cb6de4e0_conversation_tests.md)
* features_time: Tell me the time.
    - utter_features_time   <!-- predicted: action_get_time -->


## greeting_hello (/tmp/tmpn78xj0rf/7a0eb8d009cc4c5b89be5e92cb6de4e0_conversation_tests.md)
* greeting_hello: My name is Pankaj Tandia
    - utter_greeting_hello   <!-- predicted: action_check_Bot_Introduced -->


## bot_hobbies (/tmp/tmpn78xj0rf/7a0eb8d009cc4c5b89be5e92cb6de4e0_conversation_tests.md)
* bot_hobbies: Tell me any fun activity to do.
    - utter_bot_hobbies   <!-- predicted: action_default_fallback -->


## prevention_medical_attention (/tmp/tmpn78xj0rf/7a0eb8d009cc4c5b89be5e92cb6de4e0_conversation_tests.md)
* prevention_medical_attention: My temperature is above 39 degrees. Should I worry?
    - utter_prevention_medical_attention   <!-- predicted: utter_prevenion_medical_attention -->


