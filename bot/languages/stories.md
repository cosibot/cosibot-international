<!------------------ 
Others

## change_bot
* bot_change_bot{"preferred_lang": "German Cosibot"}
  - action_change_preferred_language
  - slot{"preferred_lang": "de"}
  - utter_command_change_bot
------------------->


<!------------------ 
Greetings 
------------------->
## start1
* start{"bot_introduced": "False"}
  - action_check_Bot_Introduced
  - slot{"bot_introduced": "True"}
  - utter_welcome

## start1_1
* start_dialogue{"bot_introduced": "False"}
  - action_check_Bot_Introduced
  - slot{"bot_introduced": "True"}
  - utter_welcome

## start1_2
* start_dialogue{"bot_introduced": "True"}
  - utter_greeting_hello

## start1_3
* start-dialogue{"bot_introduced": "False"}
  - action_check_Bot_Introduced
  - slot{"bot_introduced": "True"}
  - utter_welcome

## start1_4
* start-dialogue{"bot_introduced": "True"}
  - utter_greeting_hello

## start2
* start{"bot_introduced": "True"}
  - utter_greeting_hello

## greeting_hello1
* greeting_hello
  - action_check_Bot_Introduced
  - slot{"bot_introduced": "True"}
  - utter_welcome

## greeting_hello2
* greeting_hello{"bot_introduced": "True"}
  - utter_greeting_hello

## greeting_goodbye
* greeting_goodbye
  - utter_greeting_goodbye

## greeting_how_are_you
* greeting_how_are_you
  - utter_greeting_how_are_you



<!------------------ 
Traveling 
------------------->
## travel_before
* travel_before
  - utter_travel_before

## travel_while
* travel_while
  - utter_travel_while

## travel_after
* travel_after
  - utter_travel_after



<!------------------ 
About Covid-19 
------------------->
## covid_cosibot
* covid_cosibot
  - utter_covid_cosibot

## covid_current_statistics
* covid_current_statistics
  - action_get_news_request

<!--
## covid_current_statistics
* covid_current_statistics
  - utter_covid_current_statistics


## covid_situation
* covid_situation
  - utter_covid_current_statistics
-->
## coronavirus_info
* coronavirus_info
  - utter_coronavirus_info

## covid_info
* covid_info
  - utter_covid_info

## covid_info
* covid_info{"virus": "COVID"}
  - slot{"virus": "COVID"}
  - utter_covid_info

## covid_meaning
* covid_meaning
  - utter_covid_meaning

## covid_symptoms
* covid_symptoms
  - utter_covid_symptoms

## covid_worry
* covid_worry
  - utter_covid_worry

## covid_sars
* covid_sars
  - utter_covid_sars

## covid_sars
* covid_sars{"virus": "SARS"}
  - slot{"virus": "SARS"}
  - utter_covid_sars

## influenza
* myth_influenza
  - utter_covid_influenza

## covid_incubation
* covid_incubation
  - utter_covid_incubation

## covid_surfaces
* covid_surfaces
  - utter_covid_surfaces

## covid_food
* covid_food
  - utter_covid_food

## covid_crisis_howlong
* covid_crisis_howlong
  - utter_covid_crisis_howlong

## covid_mortality_rate
* covid_mortality_rate
  - utter_covid_mortality_rate

## covid_dangerous
* covid_dangerous
  - utter_covid_dangerous

## covid_procedure_after_infection
* covid_procedure_after_infection
  - utter_covid_procedure_after_infection

## covid_treatment
* covid_treatment
  - utter_covid_treatment

## covid_origins
* covid_origins
  - utter_covid_origins

## covid_duration
* covid_duration
  - utter_covid_duration

## covid_disease_process
* covid_disease_process
  - utter_covid_disease_process

## covid_aftereffects_immunity
* covid_aftereffects_immunity
  - utter_covid_aftereffects_immunity

## covid_preexisting_illness
* covid_preexisting_illness
  - utter_covid_preexisting_illness

## covid_babys_children
* covid_babys_children
  - utter_covid_babys_children

## economy_consequences
* economy_consequences
  - utter_economy_consequences

## covid_pandemic
* covid_pandemic
  - utter_covid_pandemic

## covid_sex
* covid_sex
  - utter_covid_sex



<!------------------ 
COVID-19 Prevention
------------------->
## prevention_general
* prevention_general
  - utter_prevention_general

## prevention_informed
* prevention_informed
  - utter_prevention_informed

## prevention_clean_hands
* prevention_clean_hands
  - utter_prevention_clean_hands

## prevention_distance
* prevention_distance
  - utter_prevention_distance

## prevention_touch
* prevention_touch
  - utter_prevention_touch

## prevention_respiratory_hygiene
* prevention_respiratory_hygiene
  - utter_prevention_respiratory_hygiene

## prevention_medical_attention
* prevention_medical_attention
  - utter_prevenion_medical_attention

## prevention_home
* prevention_home
  - utter_prevention_home

## prevention_medicine
* prevention_medicine
  - utter_prevention_medicine

## prevention_measures
* prevention_measures
  - utter_prevention_measures

## prevention_disinfection
* prevention_disinfection
  - utter_prevention_disinfection



<!------------------ 
Myths
------------------->
## air_conditioning
* myth_air_conditioning{"air_conditioning": "AC"}
  - utter_myth_air_conditioning

## myth_5G
* myth_5G{"5G": "5G"}
    - utter_myth_5g

## hand_dryer
* hand_dryer{"hand_dryer": "hand dryers"}
    - utter_myth_hand_dryer

## uv_lamp
* uv_lamp{"uv_lamp": "uv lamps"}
    - utter_myth_uv_lamps

## thermal_scanner
* thermal_scanner{"thermal_scanner": "thermal scanner"}
  - utter_myth_thermal_scanner

## antibiotics
* antibiotics{"antibiotics": "antibiotics"}
  - utter_myth_antibiotics

## myth_alcohol
* myth_alcohol
  - utter_myth_alcohol

## pneumonia_vaccine
* pneumonia_vaccine{"pneumonia_vaccine": "pneumonia vaccine"}
  - utter_myth_pneumonia_vaccine

## saline
* saline{"saline": "saline solution"}
  - utter_myth_saline

## garlic
* garlic{"garlic": "garlic"}
  - utter_myth_garlic

## sesame_oil
* sesame_oil{"sesame_oil": "sesame oil"}
  - utter_myth_sesame_oil

## myth_packages
* myth_packages
  - utter_myth_packages

## myth_transmission_hot_areas
* myth_transmission_hot_areas
  - utter_myth_transmission_hot_areas

## myth_cold_weather
* myth_cold_weather
  - utter_myth_cold_weather

## myth_hot_bath
* myth_hot_bath
  - utter_myth_hot_bath

## myths_conspiracy_fakenews
* myths_conspiracy_fakenews
  - utter_myths_conspiracy_fakenews



<!------------------ 
COVID-19 Spread
------------------->
## spread_general
* spread_general
  - utter_spread_general

## spread_air
* spread_air
  - utter_spread_air

## spread_no_symptoms
* spread_no_symptoms
  - utter_spread_no_symptoms

## spread_feces
* spread_feces
  - utter_spread_feces

## spread_risk
* spread_risk
  - utter_spread_risk

## spread_animals
* spread_animals
  - utter_spread_animals

## spread_pets
* spread_pets
  - utter_spread_pets

## spread_surfaces_food_objects
* spread_surfaces_food_objects
  - utter_spread_surfaces_food_objects



<!------------------ 
COVID-19 Spread
------------------->
## quarantine_general
* quarantine_general
  - utter_quarantine_general

## quarantine_dogwalking
* quarantine_dogwalking
  - utter_quarantine_dogwalking

## quarantine_when_who_howlong
* quarantine_when_who_howlong
  - utter_quarantine_when_who_howlong

## quaratine_how_it_works
* quaratine_how_it_works
  - utter_quaratine_how_it_works

## quarantine_control
* quarantine_control
  - utter_quarantine_control

## quarantine_dos_and_donts
* quarantine_dos_and_donts
  - utter_quarantine_dos_and_donts

## quarantine_toiletpaper
* quarantine_toiletpaper
  - utter_quarantine_toiletpaper



<!------------------ 
Medical Masks
------------------->
## mask_general
* mask_general
  - utter_mask_general

## mask_use_put
* mask_use_put
  - utter_mask_use_put

## mask_use_after
* mask_use_after
  - utter_mask_use_after

## visors
* visors{"visors":"visors"}
  - utter_mask_visors



<!------------------ 
Tests
------------------->
## test_virus
* test_virus
  - utter_test_virus

## test_who
* test_who
  - utter_test_who



<!------------------ 
Vocative
------------------->
## vocative_help
* vocative_help
  - utter_vocative_help

## vocative_thank_you
* vocative_thank_you
  - utter_vocative_thank_you
  - utter_further_questions

## vocative_you_welcome
* vocative_you_welcome
  - utter_vocative_you_welcome

## vocative_call
* vocative_call
  - utter_vocative_call

## vocative_sorry
* vocative_sorry
  - utter_vocative_sorry

## vocative_yes_no_ooc
* vocative_yes OR vocative_no
  - utter_further_questions



<!------------------ 
Bot Features
------------------->
## features_date
* features_date
    - action_get_date
    - slot{"bot_date_acre": "14/07/2020"}
    - slot{"bot_date_fnoronha": "14/07/2020"}
    - slot{"bot_date_brasilia": "14/07/2020"}
    - slot{"bot_date_amazonas": "14/07/2020"}
    - followup{"name": "utter_features_date"}
    - utter_features_date

* features_time
    - action_get_time
    - slot{"bot_time_acre": "10:53:09"}
    - slot{"bot_time_fnoronha": "13:53:09"}
    - slot{"bot_time_brasilia": "12:53:09"}
    - slot{"bot_time_amazonas": "11:53:09"}
    - followup{"name": "utter_features_time"}
    - utter_features_time



<!------------------ 
Bot Traits
------------------->
## bot_name
* bot_name
  - utter_bot_name

## bot_version
* bot_version
  - utter_bot_version

## bot_origin
* bot_origin
  - utter_bot_origin

## bot_languages
* bot_languages
  - utter_bot_languages

## bot_appearance
* bot_appearance
  - utter_bot_appearance

## bot_capabilities
* bot_capabilities
  - utter_bot_capabilities

## bot_goal
* bot_goal
  - utter_bot_goal

## bot_real
* bot_real
  - utter_bot_real

## bot_availability
* bot_availability
  - utter_bot_availability

## bot_books
* bot_books
  - utter_bot_books

## bot_fear
* bot_fear
  - utter_bot_fear

## bot_movies
* bot_movies
  - utter_bot_movies

## bot_music
* bot_music
  - utter_bot_music

## bot_residence
* bot_residence
  - utter_bot_residence

## bot_personality
* bot_personality
  - utter_bot_personality

## bot_sexual
* bot_sexual
  - utter_bot_sexual



<!------------------ 
Chit-chat
------------------->
## cc_weather
* cc_weather
  - utter_cc_weather

## cc_moon
* cc_moon
  - utter_cc_moon

## cc_chicken_egg
* cc_chicken_egg
  - utter_cc_chicken_egg

## cc_joke
* cc_joke
  - utter_cc_joke

## cc_politics
* cc_politics
  - utter_cc_politics

## cc_religion
* cc_religion
  - utter_cc_religion

## cc_philosophical
* cc_philosophical
  - utter_cc_philosophical

## cc_lets_talk
* cc_lets_talk
  - utter_cc_lets_talk

## cc_newspaper
* cc_newspaper
  - utter_cc_newspaper
  - action_get_news_request



<!------------------ 
User Feelings
------------------->
## user_happy
* user_happy
  - utter_user_happy

## user_friend
* user_friend
  - utter_user_friend

## user_love
* user_love
  - utter_user_love

## user_angry
* user_angry
  - utter_user_angry

## user_scared
* user_scared
  - utter_user_scared

## user_no_further_questions
* user_no_further_questions
  - utter_user_no_further_questions
  - utter_greeting_goodbye

## user_particles
* user_particles
  - utter_user_particles
  - utter_further_questions



<!------------------ 
Comments
------------------->
## comment_positive
* comment_positive
  - utter_comment_positive

## comment_negative
* comment_negative
  - utter_comment_negative

## comment_smart
* comment_smart
  - utter_comment_smart

## comment_offense
* comment_offense
  - utter_comment_offense

## comment_racist
* comment_racist
  - utter_comment_racist



<!------------------ 
Counters
------------------->
<!-- 
Generic requests 
-->
## covid_situation_without_country
* covid_situation OR covid_situation_tested OR covid_situation_recovered OR covid_situation_last_update OR covid_situation_infected_critical OR covid_situation_infected OR covid_situation_deaths 
  - utter_want_to_add_country
* vocative_yes
  - utter_ask_which_country
* country{"country_code" : "Portugal"}
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
  - utter_covid_situation


## covid_situation_without_country2
* covid_situation OR covid_situation_tested OR covid_situation_recovered OR covid_situation_last_update OR covid_situation_infected_critical OR covid_situation_infected OR covid_situation_deaths
  - utter_want_to_add_country
* vocative_no
  - utter_further_questions


## covid_situation_without_country3
* covid_situation OR covid_situation_tested OR covid_situation_recovered OR covid_situation_last_update OR covid_situation_infected_critical OR covid_situation_infected OR covid_situation_deaths
  - utter_want_to_add_country
* country{"country_code" : "Portugal"}
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
  - utter_covid_situation



<!-- 
World Regions 
-->
## covid_situation_tested
* covid_situation_tested{"world_region" : "Europe"}
  - utter_covid_current_statistics

## covid_situation_recovered
* covid_situation_recovered{"world_region" : "Asia"}
  - utter_covid_current_statistics

## covid_situation_last_update
* covid_situation_last_update{"world_region" : "Oceania"}
  - utter_covid_current_statistics

## covid_situation_infected_critical
* covid_situation_infected_critical{"world_region" : "Africa"}
  - utter_covid_current_statistics

## covid_situation_infected
* covid_situation_infected{"world_region" : "Antarctic"}
  - utter_covid_current_statistics

## covid_situation_deaths
* covid_situation_deaths{"world_region" : "World"}
  - utter_covid_current_statistics

## covid_situation
* covid_situation{"world_region" : "America"}
  - utter_covid_current_statistics



<!-- 
GENERAL SITUATION 
-->
## covid_situation_happy 
* covid_situation{"country_code" : "Portugal"}
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
  - utter_covid_situation

## covid_situation_unhappy
* covid_situation{"country_code": "Indonésia"}
  - action_search_stats
  - slot{"search_successful": "not-ok"}
  - utter_covid_current_statistics

## covid_situation_unhappy_with_country
* covid_situation{"country_code" : "Portugal"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_yes
  - utter_ask_which_country
* country{"country_code" : "Portugal"}
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
  - utter_covid_situation

## covid_situation_unhappy_inexistent_country
* covid_situation{"country_code" : "Portugal"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_yes
  - utter_ask_which_country
* country{"country_code" : "Portugal"}
  - action_search_stats
  - slot{"search_successful": "inexistent-country"}
  - utter_covid_no_country_current_statistics

## covid_situation_unhappy_with_dashboard
* covid_situation{"country_code" : "Portugal"}
  - action_search_stats
  - slot{"search_successful": "False"}
  - utter_want_to_add_country
* vocative_no
  - utter_covid_current_statistics

<!-- 
DEATHS
-->

## covid_situation_deaths_happy
* covid_situation_deaths{"country_code":"Suécia"}
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
  - utter_covid_situation_deaths

## covid_situation_deaths_unhappy
* covid_situation_deaths{"country_code": "Indonésia"}
  - action_search_stats
  - slot{"search_successful": "not-ok"}
  - utter_covid_current_statistics

## covid_situation_deaths_unhappy_with_country
* covid_situation_deaths{"country_code":"Suécia"}
  - action_search_stats
  - slot{"search_successful": "False"}
  - utter_want_to_add_country
* vocative_yes
  - utter_ask_which_country
* country{"country_code":"Suécia"}
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
  - utter_covid_situation_deaths

## covid_situation_deaths_unhappy_inexistent_country
* covid_situation_deaths{"country_code" : "Portugal"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_yes
  - utter_ask_which_country
* country{"country_code" : "Portugal"}
  - action_search_stats
  - slot{"search_successful": "inexistent-country"}
  - utter_covid_no_country_current_statistics

## covid_situation_deaths_unhappy_with_dashboard
* covid_situation_deaths{"country_code" : "Suécia"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_no
  - utter_covid_current_statistics

<!-- 
INFECTED
-->

## covid_situation_infected_happy
* covid_situation_infected{"country_code":"Itália"}
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
  - utter_covid_situation_infected

## covid_situation_infected_unhappy
* covid_situation_infected{"country_code": "Indonésia"}
  - action_search_stats
  - slot{"search_successful": "not-ok"}
  - utter_covid_current_statistics

## covid_situation_infected_unhappy_with_country
* covid_situation_infected{"country_code":"Itália"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_yes
  - utter_ask_which_country
* country{"country_code":"Itália"}
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
  - utter_covid_situation_infected

## covid_situation_infected_unhappy_inexistent_country
* covid_situation_infected{"country_code" : "Portugal"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_yes
  - utter_ask_which_country
* country{"country_code" : "Portugal"}
  - action_search_stats
  - slot{"search_successful": "inexistent-country"}
  - utter_covid_no_country_current_statistics

## covid_situation_infected_unhappy_with_dashboard
* covid_situation_infected{"country_code" : "Itália"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_no
  - utter_covid_current_statistics

<!-- 
INFECTED CRITICAL
-->

## covid_situation_infected_critical_happy
* covid_situation_infected_critical{"country_code":"Spain"}
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
  - utter_covid_situation_infected_critical

## covid_situation_infected_critical_unhappy
* covid_situation_infected_critical{"country_code": "Indonésia"}
  - action_search_stats
  - slot{"search_successful": "not-ok"}
  - utter_covid_current_statistics

## covid_situation_infected_critical_unhappy_with_country
* covid_situation_infected_critical{"country_code":"Espanha"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_yes
  - utter_ask_which_country
* country{"country_code":"Espanha"}
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
  - utter_covid_situation_infected_critical

## covid_situation_infected_critical_unhappy_inexistent_country
* covid_situation_infected_critical{"country_code" : "Portugal"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_yes
  - utter_ask_which_country
* country{"country_code" : "Portugal"}
  - action_search_stats
  - slot{"search_successful": "inexistent-country"}
  - utter_covid_no_country_current_statistics

## covid_situation_infected_critical_unhappy_with_dashboard
* covid_situation_infected_critical{"country_code" : "Itália"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_no
  - utter_covid_current_statistics

<!-- 
LAST UPDATE 
-->

## covid_situation_last_update_happy
* covid_situation_last_update{"country_code":"England"}
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
  - utter_covid_situation_last_update

## covid_situation_last_update_unhappy
* covid_situation_last_update{"country_code": "Indonesia"}
  - action_search_stats
  - slot{"search_successful": "not-ok"}
  - utter_covid_current_statistics

## covid_situation_last_update_unhappy_with_country
* covid_situation_last_update{"country_code":"Inglaterra"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_yes
  - utter_ask_which_country
* country{"country_code":"Inglaterra"}
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
  - utter_covid_situation_last_update

## covid_situation_last_update_unhappy_inexistent_country
* covid_situation_last_update{"country_code" : "Portugal"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_yes
  - utter_ask_which_country
* country{"country_code" : "Portugal"}
  - action_search_stats
  - slot{"search_successful": "inexistent-country"}
  - utter_covid_no_country_current_statistics

## covid_situation_last_update_unhappy_with_dashboard
* covid_situation_last_update{"country_code" : "Inglaterra"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_no
  - utter_covid_current_statistics

<!-- 
SITUATION RECOVERED
-->

## covid_situation_recovered_happy
* covid_situation_recovered{"country_code":"Alemanha"}
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
  - utter_covid_situation_recovered

## covid_situation_recovered_unhappy
* covid_situation_recovered{"country_code": "Indonésia"}
  - action_search_stats
  - slot{"search_successful": "not-ok"}
  - utter_covid_current_statistics

## covid_situation_recovered_unhappy_with_country
* covid_situation_recovered{"country_code":"Alemanha"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_yes
  - utter_ask_which_country
* country{"country_code":"Alemanha"}
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
  - utter_covid_situation_recovered

## covid_situation_recovered_unhappy_inexistent_country
* covid_situation_recovered{"country_code" : "Portugal"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_yes
  - utter_ask_which_country
* country{"country_code" : "Portugal"}
  - action_search_stats
  - slot{"search_successful": "inexistent-country"}
  - utter_covid_no_country_current_statistics

## covid_situation_recovered_unhappy_with_dashboard
* covid_situation_recovered{"country_code" : "Inglaterra"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_no
  - utter_covid_current_statistics

<!-- 
TESTED
-->

## covid_situation_tested_happy
* covid_situation_tested{"country_code":"Portugal"}
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
  - utter_covid_situation_tested

## covid_situation_tested_unhappy
* covid_situation_tested{"country_code": "Indonésia"}
  - action_search_stats
  - slot{"search_successful": "not-ok"}
  - utter_covid_current_statistics

## covid_situation_tested_happy
* covid_situation_tested{"country_code":"Portugal"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_yes
  - utter_ask_which_country
* country{"country_code":"Portugal"}
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
  - utter_covid_situation_tested

## covid_situation_tested_unhappy_inexistent_country
* covid_situation_tested{"country_code" : "Portugal"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_yes
  - utter_ask_which_country
* country{"country_code" : "Portugal"}
  - action_search_stats
  - slot{"search_successful": "inexistent-country"}
  - utter_covid_no_country_current_statistics

## covid_situation_tested_unhappy_with_dashboard
* covid_situation_tested{"country_code" : "Inglaterra"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_no
  - utter_covid_current_statistics

## country_wrong
* country{"country_code" : "Inglaterra"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_fallback_first

## country_right
* country{"country_code":"Inglaterra"}
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
  - utter_covid_situation_last_update

## convid_situation_infected_2
* covid_situation_infected
    - utter_want_to_add_country
* vocative_yes
    - utter_ask_which_country
* country{"country_code": "BR"}
    - slot{"country_code": "BR"}
    - action_search_stats
    - slot{"search_successful": "ok"}
    - slot{"country": "Brasil"}
    - slot{"active_cases": 602427}
    - slot{"new_cases": 930}
    - slot{"total_cases": 1888889}
    - slot{"total_recovered": 1213512}
    - slot{"total_deaths": 72950}
    - slot{"total_tests": 4572796}
    - slot{"new_deaths": 29}
    - slot{"total_infected_critical": 8318}
    - utter_covid_situation

## convid_situation_infected_3
* covid_situation_infected{"country_code": "MX"}
    - slot{"country_code": "MX"}
    - action_search_stats
    - slot{"search_successful": "ok"}
    - slot{"country": "México"}
    - slot{"active_cases": 79881}
    - slot{"new_cases": 4685}
    - slot{"total_cases": 304435}
    - slot{"total_recovered": 189063}
    - slot{"total_deaths": 35491}
    - slot{"total_tests": 739922}
    - slot{"new_deaths": 485}
    - slot{"total_infected_critical": 378}
    - utter_covid_situation_infected

## convid_situation_infected_4
* covid_situation_infected{"country_code": "PT"}
    - slot{"country_code": "PT"}
    - action_search_stats
    - slot{"search_successful": "ok"}
    - slot{"country": "Portugal"}
    - slot{"active_cases": 14091}
    - slot{"new_cases": 0}
    - slot{"total_cases": 46818}
    - slot{"total_recovered": 31065}
    - slot{"total_deaths": 1662}
    - slot{"total_tests": 1360164}
    - slot{"new_deaths": 0}
    - slot{"total_infected_critical": 63}
    - utter_covid_situation_infected

## convid_situation_infected_5
* covid_situation_infected
    - utter_want_to_add_country
* vocative_yes
    - utter_ask_which_country
* country{"country_code": "BR"}
    - slot{"country_code": "BR"}
    - action_search_stats
    - slot{"search_successful": "ok"}
    - slot{"country": "Brasil"}
    - slot{"active_cases": 643430}
    - slot{"new_cases": 0}
    - slot{"total_cases": 1931204}
    - slot{"total_recovered": 1213512}
    - slot{"total_deaths": 74262}
    - slot{"total_tests": 4572796}
    - slot{"new_deaths": 0}
    - slot{"total_infected_critical": 8318}
    - utter_covid_situation
* covid_situation_infected
    - utter_want_to_add_country
* vocative_yes
    - utter_ask_which_country
* country{"country_code": "PT"}
    - slot{"country_code": "PT"}
    - action_search_stats
    - slot{"search_successful": "ok"}
    - slot{"country": "Portugal"}
    - slot{"active_cases": 643430}
    - slot{"new_cases": 0}
    - slot{"total_cases": 1931204}
    - slot{"total_recovered": 1213512}
    - slot{"total_deaths": 74262}
    - slot{"total_tests": 4572796}
    - slot{"new_deaths": 0}
    - slot{"total_infected_critical": 8318}
    - utter_covid_situation
* covid_situation_infected{"country_code": "MX"}
    - slot{"country_code": "MX"}
    - action_search_stats
    - slot{"search_successful": "ok"}
    - slot{"country": "México"}
    - slot{"active_cases": 81183}
    - slot{"new_cases": 7051}
    - slot{"total_cases": 311486}
    - slot{"total_recovered": 193976}
    - slot{"total_deaths": 36327}
    - slot{"total_tests": 756137}
    - slot{"new_deaths": 836}
    - slot{"total_infected_critical": 378}
    - utter_covid_situation_infected