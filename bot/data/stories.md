<!------------------ 
Others
------------------->
## en_change_bot
* en_bot_change_bot{"preferred_lang": "German Cosibot"}
  - action_change_preferred_language
  - slot{"preferred_lang": "de"}
  - utter_en_command_change_bot



<!------------------ 
Greetings 
------------------->
## start1
* start{"bot_introduced": "False"}
  - action_check_Bot_Introduced
  - slot{"bot_introduced": "True"}
  - utter_en_welcome

## start2
* start{"bot_introduced": "True"}
  - utter_en_greeting_hello

## en_greeting_hello1
* en_greeting_hello
  - action_check_Bot_Introduced
  - slot{"bot_introduced": "True"}
  - utter_en_welcome

## en_greeting_hello2
* en_greeting_hello{"bot_introduced": "True"}
  - utter_en_greeting_hello

## en_greeting_goodbye
* en_greeting_goodbye
  - utter_en_greeting_goodbye

## en_greeting_how_are_you
* en_greeting_how_are_you
  - utter_en_greeting_how_are_you



<!------------------ 
Traveling 
------------------->
## en_travel_before
* en_travel_before
  - utter_en_travel_before

## en_travel_while
* en_travel_while
  - utter_en_travel_while

## en_travel_after
* en_travel_after
  - utter_en_travel_after



<!------------------ 
About Covid-19 
------------------->
## en_covid_cosibot
* en_covid_cosibot
  - utter_en_covid_cosibot

## en_covid_current_statistics
* en_covid_current_statistics
  - action_get_news_request

<!--
## en_covid_current_statistics
* en_covid_current_statistics
  - utter_en_covid_current_statistics
-->

## en_covid_situation
* en_covid_situation
  - utter_en_covid_situation

## en_coronavirus_info
* en_coronavirus_info
  - utter_en_coronavirus_info

## en_covid_info
* en_covid_info
  - utter_en_covid_info

## en_covid_meaning
* en_covid_meaning
  - utter_en_covid_meaning

## en_covid_symptoms
* en_covid_symptoms
  - utter_en_covid_symptoms

## en_covid_worry
* en_covid_worry
  - utter_en_covid_worry

## en_covid_sars
* en_covid_sars
  - utter_en_covid_sars

## en_influenza
* en_myth_influenza
  - utter_en_covid_influenza

## en_covid_incubation
* en_covid_incubation
  - utter_en_covid_incubation

## en_covid_surfaces
* en_covid_surfaces
  - utter_en_covid_surfaces

## en_covid_food
* en_covid_food
  - utter_en_covid_food

## en_covid_crisis_howlong
* en_covid_crisis_howlong
  - utter_en_covid_crisis_howlong

## en_covid_mortality_rate
* en_covid_mortality_rate
  - utter_en_covid_mortality_rate

## en_covid_dangerous
* en_covid_dangerous
  - utter_en_covid_dangerous

## en_covid_procedure_after_infection
* en_covid_procedure_after_infection
  - utter_en_covid_procedure_after_infection

## en_covid_treatment
* en_covid_treatment
  - utter_en_covid_treatment

## en_covid_origins
* en_covid_origins
  - utter_en_covid_origins

## en_covid_duration
* en_covid_duration
  - utter_en_covid_duration

## en_covid_disease_process
* en_covid_disease_process
  - utter_en_covid_disease_process

## en_covid_aftereffects_immunity
* en_covid_aftereffects_immunity
  - utter_en_covid_aftereffects_immunity

## en_covid_preexisting_illness
* en_covid_preexisting_illness
  - utter_en_covid_preexisting_illness

## en_covid_babys_children
* en_covid_babys_children
  - utter_en_covid_babys_children

## en_economy_consequences
* en_economy_consequences
  - utter_en_economy_consequences

## en_covid_pandemic
* en_covid_pandemic
  - utter_en_covid_pandemic

## en_covid_sex
* en_covid_sex
  - utter_en_covid_sex



<!------------------ 
COVID-19 Prevention
------------------->
## en_prevention_general
* en_prevention_general
  - utter_en_prevention_general

## en_prevention_informed
* en_prevention_informed
  - utter_en_prevention_information

## en_prevention_clean_hands
* en_prevention_clean_hands
  - utter_en_prevention_clean_hands

## en_prevention_distance
* en_prevention_distance
  - utter_en_prevention_distance

## en_prevention_touch
* en_prevention_touch
  - utter_en_prevention_touch

## en_prevention_respiratory_hygiene
* en_prevention_respiratory_hygiene
  - utter_en_prevention_respiratory_hygiene

## en_prevention_medical_attention
* en_prevention_medical_attention
  - utter_en_prevenion_medical_attention

## en_prevention_home
* en_prevention_home
  - utter_en_prevention_home

## en_prevention_medicine
* en_prevention_medicine
  - utter_en_prevention_medicine

## en_prevention_measures
* en_prevention_measures
  - utter_en_prevention_measures

## en_prevention_disinfection
* en_prevention_disinfection
  - utter_en_prevention_disinfection



<!------------------ 
Myths
------------------->
## en_air_conditioning
* en_myth_air_conditioning{"air_conditioning": "AC"}
  - utter_en_myth_air_conditioning

## en_myth_5G
* en_myth_5G{"5G": "5G"}
    - utter_en_myth_5g

## en_hand_dryer
* en_hand_dryer{"hand_dryer": "hand dryers"}
    - utter_en_myth_hand_dryer

## en_uv_lamp
* en_uv_lamp{"uv_lamp": "uv lamps"}
    - utter_en_myth_uv_lamps

## en_thermal_scanner
* en_thermal_scanner{"thermal_scanner": "thermal scanner"}
  - utter_en_myth_thermal_scanner

## en_antibiotics
* en_antibiotics{"antibiotics": "antibiotics"}
  - utter_en_myth_antibiotics

## en_myth_alcohol
* en_myth_alcohol
  - utter_en_myth_alcohol

## en_pneumonia_vaccine
* en_pneumonia_vaccine{"pneumonia_vaccine": "pneumonia vaccine"}
  - utter_en_myth_pneumonia_vaccine

## en_saline
* en_saline{"saline": "saline solution"}
  - utter_en_myth_saline

## en_garlic
* en_garlic{"garlic": "garlic"}
  - utter_en_myth_garlic

## en_sesame_oil
* en_sesame_oil{"sesame_oil": "sesame oil"}
  - utter_en_myth_sesame_oil

## en_myth_packages
* en_myth_packages
  - utter_en_myth_packages

## en_myth_transmission_hot_areas
* en_myth_transmission_hot_areas
  - utter_en_myth_transmission_hot_areas

## en_myth_cold_weather
* en_myth_cold_weather
  - utter_en_myth_cold_weather

## en_myth_hot_bath
* en_myth_hot_bath
  - utter_en_myth_hot_bath

## en_myths_conspiracy_fakenews
* en_myths_conspiracy_fakenews
  - utter_en_myths_conspiracy_fakenews



<!------------------ 
COVID-19 Spread
------------------->
## en_spread_general
* en_spread_general
  - utter_en_spread_general

## en_spread_air
* en_spread_air
  - utter_en_spread_air

## en_spread_no_symptoms
* en_spread_no_symptoms
  - utter_en_spread_no_symptoms

## en_spread_feces
* en_spread_feces
  - utter_en_spread_feces

## en_spread_risk
* en_spread_risk
  - utter_en_spread_risk

## en_spread_animals
* en_spread_animals
  - utter_en_spread_animals

## en_spread_pets
* en_spread_pets
  - utter_en_spread_pets

## en_spread_surfaces_food_objects
* en_spread_surfaces_food_objects
  - utter_en_spread_surfaces_food_objects



<!------------------ 
COVID-19 Spread
------------------->
## en_quarantine_general
* en_quarantine_general
  - utter_en_quarantine_general

## en_quarantine_dogwalking
* en_quarantine_dogwalking
  - utter_en_quarantine_dogwalking

## en_quarantine_when_who_howlong
* en_quarantine_when_who_howlong
  - utter_en_quarantine_when_who_howlong

## en_quaratine_how_it_works
* en_quaratine_how_it_works
  - utter_en_quaratine_how_it_works

## en_quarantine_control
* en_quarantine_control
  - utter_en_quarantine_control

## en_quarantine_dos_and_donts
* en_quarantine_dos_and_donts
  - utter_en_quarantine_dos_and_donts

## en_quarantine_toiletpaper
* en_quarantine_toiletpaper
  - utter_en_quarantine_toiletpaper



<!------------------ 
Medical Masks
------------------->
## en_mask_general
* en_mask_general
  - utter_en_mask_general

## en_mask_use_put
* en_mask_use_put
  - utter_en_mask_use_put

## en_mask_use_after
* en_mask_use_after
  - utter_en_mask_use_after

## en_visors
* en_visors{"visors":"visors"}
  - utter_en_mask_visors



<!------------------ 
Tests
------------------->
## en_test_virus
* en_test_virus
  - utter_en_test_virus

## en_test_who
* en_test_who
  - utter_en_test_who



<!------------------ 
Vocative
------------------->
## en_vocative_help
* en_vocative_help
  - utter_en_vocative_help

## en_vocative_thank_you
* en_vocative_thank_you
  - utter_en_vocative_thank_you
  - utter_en_further_questions

## en_vocative_you_welcome
* en_vocative_you_welcome
  - utter_en_vocative_you_welcome

## en_vocative_call
* en_vocative_call
  - utter_en_vocative_call

## en_vocative_sorry
* en_vocative_sorry
  - utter_en_vocative_sorry

## en_vocative_yes_no_ooc
* en_vocative_yes OR en_vocative_no
  - utter_en_further_questions



<!------------------ 
Bot Features
------------------->
## en_features_date
* en_features_date
  - action_get_date
  - utter_en_features_date

## en_features_time
* en_features_time
  - action_get_time
  - utter_en_features_time



<!------------------ 
Bot Traits
------------------->
## en_bot_name
* en_bot_name
  - utter_en_bot_name

## en_bot_version
* en_bot_version
  - utter_en_bot_version

## en_bot_origin
* en_bot_origin
  - utter_en_bot_origin

## en_bot_languages
* en_bot_languages
  - utter_en_bot_languages

## en_bot_appearance
* en_bot_appearance
  - utter_en_bot_appearance

## en_bot_capabilities
* en_bot_capabilities
  - utter_en_bot_capabilities

## en_bot_goal
* en_bot_goal
  - utter_en_bot_goal

## en_bot_real
* en_bot_real
  - utter_en_bot_real

## en_bot_availability
* en_bot_availability
  - utter_en_bot_availability

## en_bot_books
* en_bot_books
  - utter_en_bot_books

## en_bot_fear
* en_bot_fear
  - utter_en_bot_fear

## en_bot_movies
* en_bot_movies
  - utter_en_bot_movies

## en_bot_music
* en_bot_music
  - utter_en_bot_music

## en_bot_residence
* en_bot_residence
  - utter_en_bot_residence

## en_bot_personality
* en_bot_personality
  - utter_en_bot_personality

## en_bot_sexual
* en_bot_sexual
  - utter_en_bot_sexual



<!------------------ 
Chit-chat
------------------->
## en_cc_weather
* en_cc_weather
  - utter_en_cc_weather

## en_cc_moon
* en_cc_moon
  - utter_en_cc_moon

## en_cc_chicken_egg
* en_cc_chicken_egg
  - utter_en_cc_chicken_egg

## en_cc_joke
* en_cc_joke
  - utter_en_cc_joke

## en_cc_politics
* en_cc_politics
  - utter_en_cc_politics

## en_cc_religion
* en_cc_religion
  - utter_en_cc_religion

## en_cc_philosophical
* en_cc_philosophical
  - utter_en_cc_philosophical

## en_cc_lets_talk
* en_cc_lets_talk
  - utter_en_cc_lets_talk

## en_cc_newspaper
* en_cc_newspaper
  - utter_en_cc_newspaper
  - action_get_news_request



<!------------------ 
User Feelings
------------------->
## en_user_happy
* en_user_happy
  - utter_en_user_happy

## en_user_friend
* en_user_friend
  - utter_en_user_friend

## en_user_love
* en_user_love
  - utter_en_user_love

## en_user_angry
* en_user_angry
  - utter_en_user_angry

## en_user_scared
* en_user_scared
  - utter_en_user_scared

## en_user_no_further_questions
* en_user_no_further_questions
  - utter_en_user_no_further_questions
  - utter_en_greeting_goodbye

## en_user_particles
* en_user_particles
  - utter_en_user_particles
  - utter_en_further_questions



<!------------------ 
Comments
------------------->
## en_comment_positive
* en_comment_positive
  - utter_en_comment_positive

## en_comment_negative
* en_comment_negative
  - utter_en_comment_negative

## en_comment_smart
* en_comment_smart
  - utter_en_comment_smart

## en_comment_offense
* en_comment_offense
  - utter_en_comment_offense

## en_comment_racist
* en_comment_racist
  - utter_en_comment_racist



<!------------------ 
Counters
------------------->
<!-- 
Generic requests 
-->
## en_covid_situation_without_country
* en_covid_situation OR en_covid_situation_tested OR en_covid_situation_recovered OR en_covid_situation_last_update OR en_covid_situation_infected_critical OR en_covid_situation_infected OR en_covid_situation_deaths 
  - utter_en_want_to_add_country
* en_vocative_yes
  - utter_en_ask_which_country
* en_country{"en_country_code" : "Portugal"}
  - action_search_stats
  - slot{"search_successful": "ok"}
  - slot{"active_cases": "16300"}
  - slot{"country": "Portugal"}
  - slot{"new_cases": "517"}
  - slot{"total_cases": "17543"}
  - slot{"total_recovered": "921"}
  - slot{"total_deaths": "756"}
  - slot{"total_tests": "233300"}
  - slot{"total_infected_critical": "176"}
  - utter_en_covid_situation


## en_covid_situation_without_country2
* en_covid_situation OR en_covid_situation_tested OR en_covid_situation_recovered OR en_covid_situation_last_update OR en_covid_situation_infected_critical OR en_covid_situation_infected OR en_covid_situation_deaths
  - utter_en_want_to_add_country
* en_vocative_no
  - utter_en_further_questions


## en_covid_situation_without_country3
* en_covid_situation OR en_covid_situation_tested OR en_covid_situation_recovered OR en_covid_situation_last_update OR en_covid_situation_infected_critical OR en_covid_situation_infected OR en_covid_situation_deaths 
  - utter_en_want_to_add_country
* en_country{"en_country_code" : "Portugal"}
  - action_search_stats
  - slot{"search_successful": "ok"}
  - slot{"active_cases": "16300"}
  - slot{"country": "Portugal"}
  - slot{"new_cases": "517"}
  - slot{"total_cases": "17543"}
  - slot{"total_recovered": "921"}
  - slot{"total_deaths": "756"}
  - slot{"total_tests": "233300"}
  - slot{"total_infected_critical": "176"}
  - utter_en_covid_situation



<!-- 
World Regions 
-->
## en_covid_situation_tested
* en_covid_situation_tested{"en_world_region" : "Europe"}
  - utter_en_covid_current_statistics

## en_covid_situation_recovered
* en_covid_situation_recovered{"en_world_region" : "Asia"}
  - utter_en_covid_current_statistics

## en_covid_situation_last_update
* en_covid_situation_last_update{"en_world_region" : "Oceania"}
  - utter_en_covid_current_statistics

## en_covid_situation_infected_critical
* en_covid_situation_infected_critical{"en_world_region" : "Africa"}
  - utter_en_covid_current_statistics

## en_covid_situation_infected
* en_covid_situation_infected{"en_world_region" : "Antarctic"}
  - utter_en_covid_current_statistics

## en_covid_situation_deaths
* en_covid_situation_deaths{"en_world_region" : "World"}
  - utter_en_covid_current_statistics

## en_covid_situation
* en_covid_situation{"en_world_region" : "America"}
  - utter_en_covid_current_statistics



<!-- 
GENERAL SITUATION 
-->
## en_covid_situation_happy 
* en_covid_situation{"en_country_code" : "Portugal"}
  - action_search_stats
  - slot{"search_successful": "ok"}
  - slot{"active_cases": "16300"}
  - slot{"country": "Portugal"}
  - slot{"new_cases": "517"}
  - slot{"total_cases": "17543"}
  - slot{"total_recovered": "921"}
  - slot{"total_deaths": "756"}
  - slot{"total_tests": "233300"}
  - slot{"total_infected_critical": "176"}
  - utter_en_covid_situation

## en_covid_situation_unhappy
* en_covid_situation{"en_country_code": "Indonésia"}
  - action_search_stats
  - slot{"search_successful": "not-ok"}
  - utter_en_covid_current_statistics

## en_covid_situation_unhappy_with_country
* en_covid_situation{"en_country_code" : "Portugal"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_en_want_to_add_country
* en_vocative_yes
  - utter_en_ask_which_country
* en_country{"en_country_code" : "Portugal"}
  - action_search_stats
  - slot{"search_successful": "ok"}
  - slot{"active_cases": "16300"}
  - slot{"country": "Portugal"}
  - slot{"new_cases": "517"}
  - slot{"total_cases": "17543"}
  - slot{"total_recovered": "921"}
  - slot{"total_deaths": "756"}
  - slot{"total_tests": "233300"}
  - slot{"total_infected_critical": "176"}
  - utter_en_covid_situation

## en_covid_situation_unhappy_inexistent_country
* en_covid_situation{"en_country_code" : "Portugal"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_en_want_to_add_country
* en_vocative_yes
  - utter_en_ask_which_country
* en_country{"en_country_code" : "Portugal"}
  - action_search_stats
  - slot{"search_successful": "inexistent-country"}
  - utter_en_covid_no_country_current_statistics

## en_covid_situation_unhappy_with_dashboard
* en_covid_situation{"en_country_code" : "Portugal"}
  - action_search_stats
  - slot{"search_successful": "False"}
  - utter_en_want_to_add_country
* en_vocative_no
  - utter_en_covid_current_statistics

<!-- 
DEATHS
-->

## en_covid_situation_deaths_happy
* en_covid_situation_deaths{"en_country_code":"Suécia"}
  - action_search_stats
  - slot{"search_successful": "True"}
  - slot{"active_cases": "16300"}
  - slot{"country": "Suécia"}
  - slot{"new_cases": "517"}
  - slot{"total_cases": "17543"}
  - slot{"total_recovered": "921"}
  - slot{"total_deaths": "756"}
  - slot{"total_tests": "233300"}
  - slot{"total_infected_critical": "176"}
  - utter_en_covid_situation_deaths

## en_covid_situation_deaths_unhappy
* en_covid_situation_deaths{"en_country_code": "Indonésia"}
  - action_search_stats
  - slot{"search_successful": "not-ok"}
  - utter_en_covid_current_statistics

## en_covid_situation_deaths_unhappy_with_country
* en_covid_situation_deaths{"en_country_code":"Suécia"}
  - action_search_stats
  - slot{"search_successful": "False"}
  - utter_en_want_to_add_country
* en_vocative_yes
  - utter_en_ask_which_country
* en_country{"en_country_code":"Suécia"}
  - action_search_stats
  - slot{"search_successful": "True"}
  - slot{"active_cases": "16300"}
  - slot{"country": "Suécia"}
  - slot{"new_cases": "517"}
  - slot{"total_cases": "17543"}
  - slot{"total_recovered": "921"}
  - slot{"total_deaths": "756"}
  - slot{"total_tests": "233300"}
  - slot{"total_infected_critical": "176"}
  - utter_en_covid_situation_deaths

## en_covid_situation_deaths_unhappy_inexistent_country
* en_covid_situation_deaths{"en_country_code" : "Portugal"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_en_want_to_add_country
* en_vocative_yes
  - utter_en_ask_which_country
* en_country{"en_country_code" : "Portugal"}
  - action_search_stats
  - slot{"search_successful": "inexistent-country"}
  - utter_en_covid_no_country_current_statistics

## en_covid_situation_deaths_unhappy_with_dashboard
* en_covid_situation_deaths{"en_country_code" : "Suécia"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_en_want_to_add_country
* en_vocative_no
  - utter_en_covid_current_statistics

<!-- 
INFECTED
-->

## en_covid_situation_infected_happy
* en_covid_situation_infected{"en_country_code":"Itália"}
  - action_search_stats
  - slot{"search_successful": "ok"}
  - slot{"active_cases": "16300"}
  - slot{"country": "Itália"}
  - slot{"new_cases": "517"}
  - slot{"total_cases": "17543"}
  - slot{"total_recovered": "921"}
  - slot{"total_deaths": "756"}
  - slot{"total_tests": "233300"}
  - slot{"total_infected_critical": "176"}
  - utter_en_covid_situation_infected

## en_covid_situation_infected_unhappy
* en_covid_situation_infected{"en_country_code": "Indonésia"}
  - action_search_stats
  - slot{"search_successful": "not-ok"}
  - utter_en_covid_current_statistics

## en_covid_situation_infected_unhappy_with_country
* en_covid_situation_infected{"en_country_code":"Itália"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_en_want_to_add_country
* en_vocative_yes
  - utter_en_ask_which_country
* en_country{"en_country_code":"Itália"}
  - action_search_stats
  - slot{"search_successful": "ok"}
  - slot{"active_cases": "16300"}
  - slot{"country": "Itália"}
  - slot{"new_cases": "517"}
  - slot{"total_cases": "17543"}
  - slot{"total_recovered": "921"}
  - slot{"total_deaths": "756"}
  - slot{"total_tests": "233300"}
  - slot{"total_infected_critical": "176"}
  - utter_en_covid_situation_infected

## en_covid_situation_infected_unhappy_inexistent_country
* en_covid_situation_infected{"en_country_code" : "Portugal"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_en_want_to_add_country
* en_vocative_yes
  - utter_en_ask_which_country
* en_country{"en_country_code" : "Portugal"}
  - action_search_stats
  - slot{"search_successful": "inexistent-country"}
  - utter_en_covid_no_country_current_statistics

## en_covid_situation_infected_unhappy_with_dashboard
* en_covid_situation_infected{"en_country_code" : "Itália"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_en_want_to_add_country
* en_vocative_no
  - utter_en_covid_current_statistics

<!-- 
INFECTED CRITICAL
-->

## en_covid_situation_infected_critical_happy
* en_covid_situation_infected_critical{"en_country_code":"Spain"}
  - action_search_stats
  - slot{"search_successful": "ok"}
  - slot{"active_cases": "16300"}
  - slot{"country": "Spain"}
  - slot{"new_cases": "517"}
  - slot{"total_cases": "17543"}
  - slot{"total_recovered": "921"}
  - slot{"total_deaths": "756"}
  - slot{"total_tests": "233300"}
  - slot{"total_infected_critical": "176"}
  - utter_en_covid_situation_infected_critical

## en_covid_situation_infected_critical_unhappy
* en_covid_situation_infected_critical{"en_country_code": "Indonésia"}
  - action_search_stats
  - slot{"search_successful": "not-ok"}
  - utter_en_covid_current_statistics

## en_covid_situation_infected_critical_unhappy_with_country
* en_covid_situation_infected_critical{"en_country_code":"Espanha"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_en_want_to_add_country
* en_vocative_yes
  - utter_en_ask_which_country
* en_country{"en_country_code":"Espanha"}
  - action_search_stats
  - slot{"search_successful": "ok"}
  - slot{"active_cases": "16300"}
  - slot{"country": "Espanha"}
  - slot{"new_cases": "517"}
  - slot{"total_cases": "17543"}
  - slot{"total_recovered": "921"}
  - slot{"total_deaths": "756"}
  - slot{"total_tests": "233300"}
  - slot{"total_infected_critical": "176"}
  - utter_en_covid_situation_infected_critical

## en_covid_situation_infected_critical_unhappy_inexistent_country
* en_covid_situation_infected_critical{"en_country_code" : "Portugal"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_en_want_to_add_country
* en_vocative_yes
  - utter_en_ask_which_country
* en_country{"en_country_code" : "Portugal"}
  - action_search_stats
  - slot{"search_successful": "inexistent-country"}
  - utter_en_covid_no_country_current_statistics

## en_covid_situation_infected_critical_unhappy_with_dashboard
* en_covid_situation_infected_critical{"en_country_code" : "Itália"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_en_want_to_add_country
* en_vocative_no
  - utter_en_covid_current_statistics

<!-- 
LAST UPDATE 
-->

## en_covid_situation_last_update_happy
* en_covid_situation_last_update{"en_country_code":"England"}
  - action_search_stats
  - slot{"search_successful": "ok"}
  - slot{"active_cases": "16300"}
  - slot{"country": "England"}
  - slot{"new_cases": "517"}
  - slot{"total_cases": "17543"}
  - slot{"total_recovered": "921"}
  - slot{"total_deaths": "14302"}
  - slot{"total_tests": "233300"}
  - slot{"total_infected_critical": "176"}
  - utter_en_covid_situation_last_update

## en_covid_situation_last_update_unhappy
* en_covid_situation_last_update{"en_country_code": "Indonesia"}
  - action_search_stats
  - slot{"search_successful": "not-ok"}
  - utter_en_covid_current_statistics

## en_covid_situation_last_update_unhappy_with_country
* en_covid_situation_last_update{"en_country_code":"Inglaterra"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_en_want_to_add_country
* en_vocative_yes
  - utter_en_ask_which_country
* en_country{"en_country_code":"Inglaterra"}
  - action_search_stats
  - slot{"search_successful": "ok"}
  - slot{"active_cases": "16300"}
  - slot{"country": "Inglaterra"}
  - slot{"new_cases": "987"}
  - slot{"total_cases": "17543"}
  - slot{"total_recovered": "921"}
  - slot{"total_deaths": "756"}
  - slot{"total_tests": "233300"}
  - slot{"total_infected_critical": "176"}
  - utter_en_covid_situation_last_update

## en_covid_situation_last_update_unhappy_inexistent_country
* en_covid_situation_last_update{"en_country_code" : "Portugal"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_en_want_to_add_country
* en_vocative_yes
  - utter_en_ask_which_country
* en_country{"en_country_code" : "Portugal"}
  - action_search_stats
  - slot{"search_successful": "inexistent-country"}
  - utter_en_covid_no_country_current_statistics

## en_covid_situation_last_update_unhappy_with_dashboard
* en_covid_situation_last_update{"en_country_code" : "Inglaterra"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_en_want_to_add_country
* en_vocative_no
  - utter_en_covid_current_statistics

<!-- 
SITUATION RECOVERED
-->

## en_covid_situation_recovered_happy
* en_covid_situation_recovered{"en_country_code":"Alemanha"}
  - action_search_stats
  - slot{"search_successful": "ok"}
  - slot{"active_cases": "16300"}
  - slot{"country": "Alemanha"}
  - slot{"new_cases": "517"}
  - slot{"total_cases": "17543"}
  - slot{"total_recovered": "921"}
  - slot{"total_deaths": "756"}
  - slot{"total_tests": "233300"}
  - slot{"total_infected_critical": "176"}
  - utter_en_covid_situation_recovered

## en_covid_situation_recovered_unhappy
* en_covid_situation_recovered{"en_country_code": "Indonésia"}
  - action_search_stats
  - slot{"search_successful": "not-ok"}
  - utter_en_covid_current_statistics

## en_covid_situation_recovered_unhappy_with_country
* en_covid_situation_recovered{"en_country_code":"Alemanha"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_en_want_to_add_country
* en_vocative_yes
  - utter_en_ask_which_country
* en_country{"en_country_code":"Alemanha"}
  - action_search_stats
  - slot{"search_successful": "ok"}
  - slot{"active_cases": "16300"}
  - slot{"country": "Alemanha"}
  - slot{"new_cases": "987"}
  - slot{"total_cases": "17543"}
  - slot{"total_recovered": "921"}
  - slot{"total_deaths": "756"}
  - slot{"total_tests": "233300"}
  - slot{"total_infected_critical": "176"}
  - utter_en_covid_situation_recovered

## en_covid_situation_recovered_unhappy_inexistent_country
* en_covid_situation_recovered{"en_country_code" : "Portugal"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_en_want_to_add_country
* en_vocative_yes
  - utter_en_ask_which_country
* en_country{"en_country_code" : "Portugal"}
  - action_search_stats
  - slot{"search_successful": "inexistent-country"}
  - utter_en_covid_no_country_current_statistics

## en_covid_situation_recovered_unhappy_with_dashboard
* en_covid_situation_recovered{"en_country_code" : "Inglaterra"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_en_want_to_add_country
* en_vocative_no
  - utter_en_covid_current_statistics

<!-- 
TESTED
-->

## en_covid_situation_tested_happy
* en_covid_situation_tested{"en_country_code":"Portugal"}
  - action_search_stats
  - slot{"search_successful": "ok"}
  - slot{"active_cases": "16300"}
  - slot{"country": "Portugal"}
  - slot{"new_cases": "517"}
  - slot{"total_cases": "17543"}
  - slot{"total_recovered": "921"}
  - slot{"total_deaths": "756"}
  - slot{"total_tests": "233300"}
  - slot{"total_infected_critical": "176"}
  - utter_en_covid_situation_tested

## en_covid_situation_tested_unhappy
* en_covid_situation_tested{"en_country_code": "Indonésia"}
  - action_search_stats
  - slot{"search_successful": "not-ok"}
  - utter_en_covid_current_statistics

## en_covid_situation_tested_happy
* en_covid_situation_tested{"en_country_code":"Portugal"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_en_want_to_add_country
* en_vocative_yes
  - utter_en_ask_which_country
* en_country{"en_country_code":"Portugal"}
  - action_search_stats
  - slot{"search_successful": "ok"}
  - slot{"active_cases": "16300"}
  - slot{"country": "Portugal"}
  - slot{"new_cases": "987"}
  - slot{"total_cases": "17543"}
  - slot{"total_recovered": "921"}
  - slot{"total_deaths": "756"}
  - slot{"total_tests": "233300"}
  - slot{"total_infected_critical": "176"}
  - utter_en_covid_situation_tested

## en_covid_situation_tested_unhappy_inexistent_country
* en_covid_situation_tested{"en_country_code" : "Portugal"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_en_want_to_add_country
* en_vocative_yes
  - utter_en_ask_which_country
* en_country{"en_country_code" : "Portugal"}
  - action_search_stats
  - slot{"search_successful": "inexistent-country"}
  - utter_en_covid_no_country_current_statistics

## en_covid_situation_tested_unhappy_with_dashboard
* en_covid_situation_tested{"en_country_code" : "Inglaterra"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_en_want_to_add_country
* en_vocative_no
  - utter_en_covid_current_statistics

