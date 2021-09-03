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
* start
  - action_check_Bot_Introduced

## start2
* start-dialogue
  - action_check_Bot_Introduced

## greeting_hello
* greeting_hello
  - action_check_Bot_Introduced

<!--
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
  - action_check_Bot_Introduced
  - utter_greeting_hello

## start1_3
* start-dialogue{"bot_introduced": "False"}
  - action_check_Bot_Introduced
  - slot{"bot_introduced": "True"}
  - utter_welcome

## start1_4
* start-dialogue{"bot_introduced": "True"}
  - action_check_Bot_Introduced
  - utter_greeting_hello

## start2
* start{"bot_introduced": "True"}
  - action_check_Bot_Introduced
  - utter_greeting_hello

## greeting_hello1
* greeting_hello
  - action_check_Bot_Introduced
  - slot{"bot_introduced": "True"}
  - utter_welcome

## greeting_hello2
* greeting_hello{"bot_introduced": "True"}
  - action_check_Bot_Introduced
  - utter_greeting_hello
-->
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

## covid_new_strain
* covid_new_strain
  - utter_covid_new_strain

## covid_delta
* covid_delta
  - utter_covid_delta

## covid_cosibot
* covid_cosibot
  - utter_covid_cosibot

## covid_current_statistics
* covid_current_statistics
  - utter_covid_current_statistics


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

## covid_influenza
* covid_influenza
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

## covid_aftereffects
* covid_aftereffects
  - utter_covid_aftereffects

## covid_immunity
* covid_immunity
  - utter_covid_immunity

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

## covid_schools
* covid_schools
  - utter_covid_schools

## covid_ebola
* covid_ebola
  - utter_covid_ebola

## covid_after_vaccine
* covid_after_vaccine
  - utter_covid_after_vaccine


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

## prevention_vaccine
* prevention_vaccine
  - utter_prevention_vaccine

## vaccine_pfizer_about
* vaccine_pfizer_about
  - utter_vaccine_pfizer_about

## vaccine_moderna_about
* vaccine_moderna_about
  - utter_vaccine_moderna_about

## vaccine_take_or_not
* vaccine_take_or_not
  - utter_vaccine_take_or_not

## vaccine_when
* vaccine_when
  - utter_vaccine_when

## vaccine_ingredients
* vaccine_ingredients
  - utter_vaccine_ingredients

## vaccine_administration
* vaccine_administration
  - utter_vaccine_administration

## vaccine_con_covid
* vaccine_con_covid
  - utter_vaccine_con_covid

## vaccine_after_covid
* vaccine_after_covid
  - utter_vaccine_after_covid

## vaccine_mix
* vaccine_mix
  - utter_vaccine_mix

## vaccine_effectiveness
* vaccine_effectiveness
  - utter_vaccine_effectiveness

## vaccine_side_effects
* vaccine_side_effects
 - utter_vaccine_side_effects

## vaccine_safety
* vaccine_safety
  - utter_vaccine_safety

<!------------------ 
Myths
------------------->

## myth_air_conditioning
* myth_air_conditioning{"air_conditioning": "AC"}
  - utter_myth_air_conditioning

## myth_5G
* myth_5G{"5G": "5G"}
    - utter_myth_5g

## myth_hand_dryer
* myth_hand_dryer{"hand_dryer": "hand dryers"}
    - utter_myth_hand_dryer

## myth_uv_lamps
* myth_uv_lamps{"uv_lamp": "uv lamps"}
    - utter_myth_uv_lamps

## myth_thermal_scanner
* myth_thermal_scanner{"thermal_scanner": "thermal scanner"}
  - utter_myth_thermal_scanner

## myth_antibiotics
* myth_antibiotics{"antibiotics": "antibiotics"}
  - utter_myth_antibiotics

## myth_alcohol
* myth_alcohol
  - utter_myth_alcohol

## myth_pneumonia_vaccine
* myth_pneumonia_vaccine{"pneumonia_vaccine": "pneumonia vaccine"}
  - utter_myth_pneumonia_vaccine

## myth_saline
* myth_saline{"saline": "saline solution"}
  - utter_myth_saline

## myth_garlic
* myth_garlic{"garlic": "garlic"}
  - utter_myth_garlic

## myth_sesame_oil
* myth_sesame_oil{"sesame_oil": "sesame oil"}
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

## myth_conspiracy_fakenews
* myth_conspiracy_fakenews
  - utter_myth_conspiracy_fakenews


## myth_mosquitoes
* myth_mosquitoes
  - utter_myth_mosquitoes

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

<!--
## quarantine_when_who_howlong
* quarantine_when_who_howlong
  - utter_quarantine_when_who_howlong
-->

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

## mask_visors
* mask_visors{"visors":"visors"}
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

## bot_personal_questions
* bot_personal_questions
  - utter_bot_personal_questions

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
  - utter_covid_current_statistics

## covid_situation_without_country2
* covid_situation OR covid_situation_tested OR covid_situation_recovered OR covid_situation_last_update OR covid_situation_infected_critical OR covid_situation_infected OR covid_situation_deaths
  - utter_want_to_add_country
* vocative_no
  - utter_further_questions


## covid_situation_without_country3
* covid_situation OR covid_situation_tested OR covid_situation_recovered OR covid_situation_last_update OR covid_situation_infected_critical OR covid_situation_infected OR covid_situation_deaths
  - utter_want_to_add_country
* country{"country_code" : "Portugal"}
  - utter_covid_current_statistics



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

## covid_situation
* covid_situation
  - utter_covid_current_statistics

## covid_situation_happy 
* covid_situation{"country_code" : "Portugal"}
  - utter_covid_current_statistics

<!-- 
DEATHS
-->

## covid_situation_deaths
* covid_situation_deaths
  - utter_covid_current_statistics

## covid_situation_deaths_happy
* covid_situation_deaths{"country_code":"Suécia"}
  - utter_covid_current_statistics
<!-- 
INFECTED
-->

## covid_situation_infected
* covid_situation_infected
  - utter_covid_current_statistics

## covid_situation_infected_happy
* covid_situation_infected{"country_code":"Itália"}
  - utter_covid_current_statistics

<!-- 
INFECTED CRITICAL
-->

## covid_situation_infected_critical
* covid_situation_infected_critical
  - utter_covid_current_statistics

## covid_situation_infected_critical_happy
* covid_situation_infected_critical{"country_code":"Spain"}
  - utter_covid_current_statistics

<!-- 
LAST UPDATE 
-->

## covid_situation_last_update
* covid_situation_last_update
  - utter_covid_current_statistics

## covid_situation_last_update_happy
* covid_situation_last_update{"country_code":"England"}
  - utter_covid_current_statistics

<!-- 
SITUATION RECOVERED
-->

## covid_situation_recovered
* covid_situation_recovered
  - utter_covid_current_statistics

## covid_situation_recovered_happy
* covid_situation_recovered{"country_code":"Alemanha"}
  - utter_covid_current_statistics
<!-- 
TESTED
-->

## covid_situation_tested
* covid_situation_tested
  - utter_covid_current_statistics

## covid_situation_tested_happy
* covid_situation_tested{"country_code":"Portugal"}
  - utter_covid_current_statistics


