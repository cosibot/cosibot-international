<!------------------ 
Others

## change_bot
* bot_change_bot: 
  - action_change_preferred_language
  - slot{"preferred_lang": "de"}
  - utter_command_change_bot
------------------->


<!------------------ 
Greetings 
------------------->
## start1
* start: /start dialogue
  - action_check_Bot_Introduced

## start2
* start-dialogue: 
  - action_check_Bot_Introduced

## greeting_hello
* greeting_hello: Hola yo soy
  - action_check_Bot_Introduced

<!--
## start1
* start: /start
  - action_check_Bot_Introduced
  - slot{"bot_introduced": "True"}
  - utter_welcome

## start1_1
* start_dialogue: 
  - action_check_Bot_Introduced
  - slot{"bot_introduced": "True"}
  - utter_welcome

## start1_2
* start_dialogue: 
  - action_check_Bot_Introduced
  - utter_greeting_hello

## start1_3
* start-dialogue: 
  - action_check_Bot_Introduced
  - slot{"bot_introduced": "True"}
  - utter_welcome

## start1_4
* start-dialogue: 
  - action_check_Bot_Introduced
  - utter_greeting_hello

## start2
* start: /start dialogue
  - action_check_Bot_Introduced
  - utter_greeting_hello

## greeting_hello1
* greeting_hello: Inicia
  - action_check_Bot_Introduced
  - slot{"bot_introduced": "True"}
  - utter_welcome

## greeting_hello2
* greeting_hello: Hola cosibot
  - action_check_Bot_Introduced
  - utter_greeting_hello
-->
## greeting_goodbye
* greeting_goodbye: Aaaaadios
  - utter_greeting_goodbye

## greeting_how_are_you
* greeting_how_are_you: Como estas querida
  - utter_greeting_how_are_you



<!------------------ 
Traveling 
------------------->

## travel_before
* travel_before: Precauciones de viaje.
  - utter_travel_before

## travel_while
* travel_while: ¿Cómo comportarse durante el viaje?
  - utter_travel_while

## travel_after
* travel_after: Cómo proceder al regresar de viajar.
  - utter_travel_after



<!------------------ 
About Covid-19 
------------------->

## covid_new_strain
* covid_new_strain: Variantes del coronavirus
  - utter_covid_new_strain

## covid_cosibot
* covid_cosibot: Cosibot
  - utter_covid_cosibot

## covid_current_statistics
* covid_current_statistics: Cuántas personas están hospitalizadas en [Bogotá]{"entity": "geography", "value": "town"}?
  - action_get_news_request

<!--
## covid_current_statistics
* covid_current_statistics: Cómo es la situación en [Quito]{"entity": "geography", "value": "town"}?
  - utter_covid_current_statistics


## covid_situation
* covid_situation: Puedes darme estadísticas?
  - utter_covid_current_statistics
-->

## coronavirus_info
* coronavirus_info: No sé que es un coronavirus
  - utter_coronavirus_info

## covid_info
* covid_info: Información sobre COVID2019
  - utter_covid_info

## covid_info
* covid_info: nuevo coronavirus
  - slot{"virus": "COVID"}
  - utter_covid_info

## covid_meaning
* covid_meaning: Covid significado
  - utter_covid_meaning

## covid_symptoms
* covid_symptoms: Dolor de cabeza y dolor de espalda son síntomas de covid-19?
  - utter_covid_symptoms

## covid_worry
* covid_worry: Tengo miedo
  - utter_covid_worry

## covid_sars
* covid_sars: Acerca del nuevo coronavirus y el SARS
  - utter_covid_sars

## covid_sars
* covid_sars: SARS y COVID.
  - slot{"virus": "SARS"}
  - utter_covid_sars

## covid_influenza
* covid_influenza: influenza
  - utter_covid_influenza

## covid_incubation
* covid_incubation: Periodo de incubación 2019-nCoV.
  - utter_covid_incubation

## covid_surfaces
* covid_surfaces: Cuanto tiempo se mantiene el COVID-19 En superficies?
  - utter_covid_surfaces

## covid_food
* covid_food: Puedo infectarme de coronavirus con el agua o la comida?
  - utter_covid_food

## covid_crisis_howlong
* covid_crisis_howlong: Cuando se irá esta enfermedad?
  - utter_covid_crisis_howlong

## covid_mortality_rate
* covid_mortality_rate: El covid-19 mata?
  - utter_covid_mortality_rate

## covid_dangerous
* covid_dangerous: Es muy contagioso el covid?
  - utter_covid_dangerous

## covid_procedure_after_infection
* covid_procedure_after_infection: Estoy infectado
  - utter_covid_procedure_after_infection

## covid_treatment
* covid_treatment: Hay algún tratamiento?
  - utter_covid_treatment

## covid_origins
* covid_origins: De qué país proviene el coronavirus?
  - utter_covid_origins

## covid_duration
* covid_duration: ¿Cuánto tiempo lleva enfermo alguien infectado?
  - utter_covid_duration

## covid_disease_process
* covid_disease_process: Avance de la enfermedad
  - utter_covid_disease_process

## covid_aftereffects
* covid_aftereffects: Los pulmones se recuperan después de la infección
  - utter_covid_aftereffects

## covid_immunity
* covid_immunity: Alguien que se ha recuperado es ahora inmune?
  - utter_covid_immunity

## covid_preexisting_illness
* covid_preexisting_illness: Edades que requieren más cuidados
  - utter_covid_preexisting_illness

## covid_babys_children
* covid_babys_children: los niños contagian el covid.19?
  - utter_covid_babys_children

## economy_consequences
* economy_consequences: Consecuencias económicas
  - utter_economy_consequences

## covid_pandemic
* covid_pandemic: Qué significa pandemia?
  - utter_covid_pandemic

## covid_sex
* covid_sex: Relaciones sexuales y la transmisión
  - utter_covid_sex

## covid_schools
* covid_schools: Acerca de las escuelas
  - utter_covid_schools

## covid_ebola
* covid_ebola: Ebola
  - utter_covid_ebola


<!------------------ 
COVID-19 Prevention
------------------->

## prevention_general
* prevention_general: como bamos a prevenirnos
  - utter_prevention_general

## prevention_informed
* prevention_informed: ¿Debo seguir las noticias con regularidad?
  - utter_prevention_informed

## prevention_clean_hands
* prevention_clean_hands: Importancia de lavarse las manos
  - utter_prevention_clean_hands

## prevention_distance
* prevention_distance: Distancia con personas tosiendo
  - utter_prevention_distance

## prevention_touch
* prevention_touch: No tocar la nariz
  - utter_prevention_touch

## prevention_respiratory_hygiene
* prevention_respiratory_hygiene: Cubrirse la boca y la nariz al toser.
  - utter_prevention_respiratory_hygiene

## prevention_medical_attention
* prevention_medical_attention: Estoy enfermo
  - utter_prevenion_medical_attention

## prevention_home
* prevention_home: Respuesta equivocada
  - utter_prevention_home

## prevention_medicine
* prevention_medicine: ¿Hay algún tratamiento todavía?
  - utter_prevention_medicine

## prevention_measures
* prevention_measures: ¿Debo tomar remedios herbales tradicionales para prevenir COVID-2019?
  - utter_prevention_measures

## prevention_disinfection
* prevention_disinfection: Los sanitizantes son 100% efectivos contra el virus?
  - utter_prevention_disinfection

## prevention_vaccine
* prevention_vaccine: ¿Dónde está la vacuna del virus corona?
  - utter_prevention_vaccine

## vaccine_pfizer_about
* vaccine_pfizer_about: Más sobre la vacuna Pfizer-BioNTech
  - utter_vaccine_pfizer_about

## vaccine_moderna_about
* vaccine_moderna_about: vacuna moderna
  - utter_vaccine_moderna_about

## vaccine_take_or_not
* vaccine_take_or_not: Yo tampoco sé o no tomar la vacuna
  - utter_vaccine_take_or_not

## vaccine_when
* vaccine_when: Cuando habrá una vacuna para todos?
  - utter_vaccine_when

## vaccine_ingredients
* vaccine_ingredients: Componentes de la vacuna
  - utter_vaccine_ingredients

## vaccine_administration
* vaccine_administration: Como administran la vacuna?
  - utter_vaccine_administration


<!------------------ 
Myths
------------------->

## myth_air_conditioning
* myth_air_conditioning: el aire acondicionado
  - utter_myth_air_conditioning

## myth_5G
* myth_5G: red 5g
    - utter_myth_5g

## myth_hand_dryer
* myth_hand_dryer: secadores de manos
    - utter_myth_hand_dryer

## myth_uv_lamps
* myth_uv_lamps: lampara ultravioleta
    - utter_myth_uv_lamps

## myth_thermal_scanner
* myth_thermal_scanner: escáneres térmicos
  - utter_myth_thermal_scanner

## myth_antibiotics
* myth_antibiotics: antibióticos
  - utter_myth_antibiotics

## myth_alcohol
* myth_alcohol: Rociando cloro matas al virus?
  - utter_myth_alcohol

## myth_pneumonia_vaccine
* myth_pneumonia_vaccine: vacuna neumonía
  - utter_myth_pneumonia_vaccine

## myth_saline
* myth_saline: solución salina
  - utter_myth_saline

## myth_garlic
* myth_garlic: El ajo puede curar el covid?
  - utter_myth_garlic

## myth_sesame_oil
* myth_sesame_oil: aceite de sésamo
  - utter_myth_sesame_oil

## myth_packages
* myth_packages: Paquetes que vienen de lugares infectados
  - utter_myth_packages

## myth_transmission_hot_areas
* myth_transmission_hot_areas: ¿Se transmite el virus de la enfermedad en áreas con climas cálidos y húmedos?
  - utter_myth_transmission_hot_areas

## myth_cold_weather
* myth_cold_weather: El clima frío puede matar al COVID-19?
  - utter_myth_cold_weather

## myth_hot_bath
* myth_hot_bath: El baño caliente mata el virus.
  - utter_myth_hot_bath

## myth_conspiracy_fakenews
* myth_conspiracy_fakenews: El coronavirus si existe?
  - utter_myth_conspiracy_fakenews


## myth_mosquitoes
* myth_mosquitoes: Los mosquitos propagan la enfermedad?
  - utter_myth_mosquitoes

<!------------------ 
COVID-19 Spread
------------------->

## spread_general
* spread_general: Propagación del coronavirus.
  - utter_spread_general

## spread_air
* spread_air: ¿El virus que causa COVID-19 se propaga por el aire?
  - utter_spread_air

## spread_no_symptoms
* spread_no_symptoms: ¿Se puede contagiar el virus a una persona que no presenta síntomas?
  - utter_spread_no_symptoms

## spread_feces
* spread_feces: Contraer el virus a través de las heces.
  - utter_spread_feces

## spread_risk
* spread_risk: ¿Cuáles son las posibilidades de contraer COVID-19?
  - utter_spread_risk

## spread_animals
* spread_animals: ¿Puedo contraer el virus de un animal?
  - utter_spread_animals

## spread_pets
* spread_pets: ¿Puede mi animal de compañía transmitir la enfermedad?
  - utter_spread_pets

## spread_surfaces_food_objects
* spread_surfaces_food_objects: Puedo contagiarme de covid con la comida o el agua?
  - utter_spread_surfaces_food_objects



<!------------------ 
COVID-19 Spread
------------------->

## quarantine_general
* quarantine_general: Que es cuarentena?
  - utter_quarantine_general

## quarantine_dogwalking
* quarantine_dogwalking: Que deberia hacer en cuarentena con mi perro? Puedo salir a pasear?
  - utter_quarantine_dogwalking

## quarantine_when_who_howlong
* quarantine_when_who_howlong: Quien debería pasar o hacer cuarentena?
  - utter_quarantine_when_who_howlong

## quaratine_how_it_works
* quaratine_how_it_works: ¿Cómo hacer una cuarentena adecuada?
  - utter_quaratine_how_it_works

## quarantine_control
* quarantine_control: Como es el control de la cuarentena?
  - utter_quarantine_control

## quarantine_dos_and_donts
* quarantine_dos_and_donts: Que está prohibido hacer en la cuarentena?
  - utter_quarantine_dos_and_donts

## quarantine_toiletpaper
* quarantine_toiletpaper: Papel de baño
  - utter_quarantine_toiletpaper



<!------------------ 
Medical Masks
------------------->

## mask_general
* mask_general: llevar puesto cubrebocas previene el covid?
  - utter_mask_general

## mask_use_put
* mask_use_put: ¿Qué hacer antes de usar una mascarilla desechable?
  - utter_mask_use_put

## mask_use_after
* mask_use_after: ¿Cómo proceder después de usar una mascarilla?
  - utter_mask_use_after

## mask_visors
* mask_visors: Caretas de acrílico
  - utter_mask_visors



<!------------------ 
Tests
------------------->

## test_virus
* test_virus: puedo hacerme una prueba
  - utter_test_virus

## test_who
* test_who: ¿Cómo me hago la prueba de covid?
  - utter_test_who



<!------------------ 
Vocative
------------------->

## vocative_help
* vocative_help: puedo pedirte ayuda
  - utter_vocative_help

## vocative_thank_you
* vocative_thank_you: Gracias x tu ayuda
  - utter_vocative_thank_you
  - utter_further_questions

## vocative_you_welcome
* vocative_you_welcome: No es ninguna molestia
  - utter_vocative_you_welcome

## vocative_call
* vocative_call: Me escuchas?
  - utter_vocative_call

## vocative_sorry
* vocative_sorry: Discúlpame
  - utter_vocative_sorry

## vocative_yes_no_ooc
* vocative_yes: Sí claro
  - utter_further_questions



<!------------------ 
Bot Features
------------------->

## features_date
* features_date: Dame la fecha de hoy
    - action_get_date
    - slot{"bot_date_acre": "14/07/2020"}
    - slot{"bot_date_fnoronha": "14/07/2020"}
    - slot{"bot_date_brasilia": "14/07/2020"}
    - slot{"bot_date_amazonas": "14/07/2020"}
    - followup{"name": "utter_features_date"}
    - utter_features_date

* features_time: Quiero saber que hora es
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
* bot_name: No pregunté tu nombre
  - utter_bot_name

## bot_version
* bot_version: Cuentame tus malas experiencias
  - utter_bot_version

## bot_origin
* bot_origin: Tu origen
  - utter_bot_origin

## bot_languages
* bot_languages: Más idiomas
  - utter_bot_languages

## bot_appearance
* bot_appearance: Tu apariencia física.
  - utter_bot_appearance

## bot_capabilities
* bot_capabilities: En que puedes ayudarme?
  - utter_bot_capabilities

## bot_goal
* bot_goal: Cuáles son tus objetivos personales?
  - utter_bot_goal

## bot_real
* bot_real: Creo que eres artificial
  - utter_bot_real

## bot_availability
* bot_availability: Enséñame tu disponibilidad.
  - utter_bot_availability

## bot_books
* bot_books: Te gusta leer?
  - utter_bot_books

## bot_fear
* bot_fear: Te gusta juegar juegos de computadora?
  - utter_bot_fear

## bot_movies
* bot_movies: Disfrutas alguna película?
  - utter_bot_movies

## bot_music
* bot_music: Cuál es tu album favorito?
  - utter_bot_music

## bot_residence
* bot_residence: Dime donde se ubica tu casa
  - utter_bot_residence

## bot_personality
* bot_personality: Qué forma de ser tienes?
  - utter_bot_personality

## bot_personal_questions
* bot_personal_questions: Cuál es la cosa más loca que le hiciste a alguien?
  - utter_bot_personal_questions

## bot_sexual
* bot_sexual: Quiero tener sexo contigo
  - utter_bot_sexual



<!------------------ 
Chit-chat
------------------->

## cc_weather
* cc_weather: Clima
  - utter_cc_weather

## cc_moon
* cc_moon: Dime que tan lejos queda la luna
  - utter_cc_moon

## cc_chicken_egg
* cc_chicken_egg: ¿Qué fue primero? ¿Huevo o pollo?
  - utter_cc_chicken_egg

## cc_joke
* cc_joke: Conoces algún chiste?
  - utter_cc_joke

## cc_politics
* cc_politics: Quién es el líder del partido?
  - utter_cc_politics

## cc_religion
* cc_religion: Dios nos salvará a todos?
  - utter_cc_religion

## cc_philosophical
* cc_philosophical: Hay una fuerza o energía superior?
  - utter_cc_philosophical

## cc_lets_talk
* cc_lets_talk: Estamos chateando?
  - utter_cc_lets_talk

## cc_newspaper
* cc_newspaper: Cuáles son las noticias?
  - utter_cc_newspaper
  - action_get_news_request



<!------------------ 
User Feelings
------------------->

## user_happy
* user_happy: Me siento como una persona eufórica.
  - utter_user_happy

## user_friend
* user_friend: ¿Puedo tener el placer de tenerte como mi amigo?
  - utter_user_friend

## user_love
* user_love: Me estoy derritiendo por ti
  - utter_user_love

## user_angry
* user_angry: ¡En este momento estoy echando espuma por la boca!
  - utter_user_angry

## user_scared
* user_scared: TENGO MIEDO
  - utter_user_scared

## user_no_further_questions
* user_no_further_questions: No tengo más preguntas, gracias.
  - utter_user_no_further_questions
  - utter_greeting_goodbye

## user_particles
* user_particles: Ah
  - utter_user_particles
  - utter_further_questions



<!------------------ 
Comments
------------------->

## comment_positive
* comment_positive: Eres bonitica
  - utter_comment_positive

## comment_negative
* comment_negative: Sigues preguntándome lo mismo
  - utter_comment_negative

## comment_smart
* comment_smart: Tu eres inteligente
  - utter_comment_smart

## comment_offense
* comment_offense: Perdedora
  - utter_comment_offense

## comment_racist
* comment_racist: Nigga
  - utter_comment_racist



<!------------------ 
Counters
------------------->
<!-- 
Generic requests 
-->

## covid_situation_without_country
* covid_situation: Cuál es la situación en el mundo?
  - utter_want_to_add_country
* vocative_yes: Sin falta
  - utter_ask_which_country
* country: [moldova]{"entity": "country_code", "value": "MD"}
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
* covid_situation: muertes en [Alemania]{"entity": "country_code", "value": "DE"}
  - utter_want_to_add_country
* vocative_no: Nooo
  - utter_further_questions


## covid_situation_without_country3
* covid_situation: Cuánta gente murió?
  - utter_want_to_add_country
* country: [Kingdom of Bhutan]{"entity": "country_code", "value": "BT"}
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
* covid_situation_tested: Cuántos han llevado un test en [Ecuador]{"entity": "country_code", "value": "EC"}?
  - utter_covid_current_statistics

## covid_situation_recovered
* covid_situation_recovered: Cuántas personas se han recuperado en [Vietnam]{"entity": "country_code", "value": "VN"}?
  - utter_covid_current_statistics

## covid_situation_last_update
* covid_situation_last_update: Situación en [Portugal]{"entity": "country_code", "value": "PT"}
  - utter_covid_current_statistics

## covid_situation_infected_critical
* covid_situation_infected_critical: Casos de gravedad
  - utter_covid_current_statistics

## covid_situation_infected
* covid_situation_infected: Cuántos casos activos hay en [Paraguay]{"entity": "country_code", "value": "PY"}?
  - utter_covid_current_statistics

## covid_situation_deaths
* covid_situation_deaths: Cuántos casos de muerte por covid 19 en [Nicaragua]{"entity": "country_code", "value": "NI"}?
  - utter_covid_current_statistics

## covid_situation
* covid_situation: Número de infectados a nivel mundial
  - utter_covid_current_statistics



<!-- 
GENERAL SITUATION 
-->

## covid_situation_happy 
* covid_situation: En total cuantos casos positivos hay
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
* covid_situation: Cuál es el número de muertes?
  - action_search_stats
  - slot{"search_successful": "not-ok"}
  - utter_covid_current_statistics

## covid_situation_unhappy_with_country
* covid_situation: Cuál es el númer de personas infectadas?
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_yes: De acuerdo
  - utter_ask_which_country
* country: [República da Zâmbia]{"entity": "country_code", "value": "ZM"}
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
* covid_situation: Cuántos casos existen en el mundo?
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_yes: Ok Helen
  - utter_ask_which_country
* country: [samoa]{"entity": "country_code", "value": "WS"}
  - action_search_stats
  - slot{"search_successful": "inexistent-country"}
  - utter_covid_no_country_current_statistics

## covid_situation_unhappy_with_dashboard
* covid_situation: Cuantas muertes hay en el mundo
  - action_search_stats
  - slot{"search_successful": "False"}
  - utter_want_to_add_country
* vocative_no: De ninguna manera
  - utter_covid_current_statistics

<!-- 
DEATHS
-->

## covid_situation_deaths_happy
* covid_situation_deaths: Cuantos han muerto hasta el momento en [Francia]{"entity": "country_code", "value": "FR"}?
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
* covid_situation_deaths: Cuantos han muerto hasta el momento en [Francia]{"entity": "country_code", "value": "FR"}?
  - action_search_stats
  - slot{"search_successful": "not-ok"}
  - utter_covid_current_statistics

## covid_situation_deaths_unhappy_with_country
* covid_situation_deaths: Número de muertes hasta ahora en la [India]{"entity": "country_code", "value": "IN"}?
  - action_search_stats
  - slot{"search_successful": "False"}
  - utter_want_to_add_country
* vocative_yes: yup
  - utter_ask_which_country
* country: [Nicaragua]{"entity": "country_code", "value": "NI"}
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
* covid_situation_deaths: Número de muertes hasta ahora en la [India]{"entity": "country_code", "value": "IN"}?
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_yes: Sip
  - utter_ask_which_country
* country: [Saint Martin French part]{"entity": "country_code", "value": "MF"}
  - action_search_stats
  - slot{"search_successful": "inexistent-country"}
  - utter_covid_no_country_current_statistics

## covid_situation_deaths_unhappy_with_dashboard
* covid_situation_deaths: Cuantas personas han fallecido en [Corea del Sur]{"entity": "country_code", "value": "KR"}?
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_no: Los cerdos pueden volar
  - utter_covid_current_statistics

<!-- 
INFECTED
-->

## covid_situation_infected_happy
* covid_situation_infected: Cuantos casos de coronavirus hay en California
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
* covid_situation_infected: Cuántas personas se han infectado o contraído el virus en los países de Africa?
  - action_search_stats
  - slot{"search_successful": "not-ok"}
  - utter_covid_current_statistics

## covid_situation_infected_unhappy_with_country
* covid_situation_infected: Cuantós infectados hay en [Japón]{"entity": "country_code", "value": "JP"}?
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_yes: aprobado
  - utter_ask_which_country
* country: [Taneẓroft Tutrimt]{"entity": "country_code", "value": "EH"}
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
* covid_situation_infected: Cuantos casos de coronavirus hay en California
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_yes: Ok ok
  - utter_ask_which_country
* country: [el salvador]{"entity": "country_code", "value": "SV"}
  - action_search_stats
  - slot{"search_successful": "inexistent-country"}
  - utter_covid_no_country_current_statistics

## covid_situation_infected_unhappy_with_dashboard
* covid_situation_infected: Cuantos se han infectado en toda Europa?
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_no: Nooo000!!!
  - utter_covid_current_statistics

<!-- 
INFECTED CRITICAL
-->

## covid_situation_infected_critical_happy
* covid_situation_infected_critical: Cuántos infectados están en casos críticos en el [Estado de Mexico]{"entity": "country_code", "value": "MX"}?
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
* covid_situation_infected_critical: Críticos en [Brasil]{"entity": "country_code", "value": "BR"}
  - action_search_stats
  - slot{"search_successful": "not-ok"}
  - utter_covid_current_statistics

## covid_situation_infected_critical_unhappy_with_country
* covid_situation_infected_critical: Hay casos de gravedad en [Argentina]{"entity": "country_code", "value": "AR"}?
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_yes: De acuerdo
  - utter_ask_which_country
* country: [united states minor outlying islands]{"entity": "country_code", "value": "UM"}
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
* covid_situation_infected_critical: Casos críticos en el [Reino Unido]{"entity": "country_code", "value": "GB"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_yes: Ok Helen
  - utter_ask_which_country
* country: [Benin]{"entity": "country_code", "value": "BJ"}
  - action_search_stats
  - slot{"search_successful": "inexistent-country"}
  - utter_covid_no_country_current_statistics

## covid_situation_infected_critical_unhappy_with_dashboard
* covid_situation_infected_critical: Cuántos casos críticos hay en [España]{"entity": "country_code", "value": "ES"}?
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_no: Ne
  - utter_covid_current_statistics

<!-- 
LAST UPDATE 
-->

## covid_situation_last_update_happy
* covid_situation_last_update: Datos de hoy en [Venezuela]{"entity": "country_code", "value": "VE"}
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
* covid_situation_last_update: Nuevos casos y muertes en la [India]{"entity": "country_code", "value": "IN"}
  - action_search_stats
  - slot{"search_successful": "not-ok"}
  - utter_covid_current_statistics

## covid_situation_last_update_unhappy_with_country
* covid_situation_last_update: Me gustaría conocer el número de casos actuales de covid en el [Reino Unido]{"entity": "country_code", "value": "GB"} y en [Estados Unidos]{"entity": "country_code", "value": "US"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_yes: Muy bien
  - utter_ask_which_country
* country: [Trinidad and Tobago]{"entity": "country_code", "value": "TT"}
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
* covid_situation_last_update: Datos actualizados de [USA]{"entity": "country_code", "value": "US"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_yes: aprobado
  - utter_ask_which_country
* country: [senegal]{"entity": "country_code", "value": "SN"}
  - action_search_stats
  - slot{"search_successful": "inexistent-country"}
  - utter_covid_no_country_current_statistics

## covid_situation_last_update_unhappy_with_dashboard
* covid_situation_last_update: Que numeros se reportan hoy en [Venezuela]{"entity": "country_code", "value": "VE"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_no: No realmente
  - utter_covid_current_statistics

<!-- 
SITUATION RECOVERED
-->

## covid_situation_recovered_happy
* covid_situation_recovered: Cuántos se han recuperado en la República de [Cabo Verde]{"entity": "country_code", "value": "CV"}?
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
* covid_situation_recovered: Número total de recuperados en [Argentina]{"entity": "country_code", "value": "AR"}
  - action_search_stats
  - slot{"search_successful": "not-ok"}
  - utter_covid_current_statistics

## covid_situation_recovered_unhappy_with_country
* covid_situation_recovered: Cuántas personas se han recuperado en [Vietnam]{"entity": "country_code", "value": "VN"}?
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_yes: Sipi
  - utter_ask_which_country
* country: [jersey]{"entity": "country_code", "value": "JE"}
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
* covid_situation_recovered: Recuperadas en [España]{"entity": "country_code", "value": "ES"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_yes: Seguramente
  - utter_ask_which_country
* country: [Namibia]{"entity": "country_code", "value": "NA"}
  - action_search_stats
  - slot{"search_successful": "inexistent-country"}
  - utter_covid_no_country_current_statistics

## covid_situation_recovered_unhappy_with_dashboard
* covid_situation_recovered: Cuántos se han recuperado en [Reino Unido]?
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_no: Bajo ninguna circunstancia
  - utter_covid_current_statistics

<!-- 
TESTED
-->

## covid_situation_tested_happy
* covid_situation_tested: Cuántos tienen diagnóstico en [México]{"entity": "country_code", "value": "MX"}?
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
* covid_situation_tested: Pruebas en [Puerto Rico]{"entity": "country_code", "value": "PR"}
  - action_search_stats
  - slot{"search_successful": "not-ok"}
  - utter_covid_current_statistics

## covid_situation_tested_happy
* covid_situation_tested: Cuántos test en [Argentina]{"entity": "country_code", "value": "AR"}?
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_yes: Ahuevo
  - utter_ask_which_country
* country: [RSA]{"entity": "country_code", "value": "ZA"}
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
* covid_situation_tested: Pruebas en [Puerto Rico]{"entity": "country_code", "value": "PR"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_yes: aprobado
  - utter_ask_which_country
* country: [malvinas]{"entity": "country_code", "value": "FK"}
  - action_search_stats
  - slot{"search_successful": "inexistent-country"}
  - utter_covid_no_country_current_statistics

## covid_situation_tested_unhappy_with_dashboard
* covid_situation_tested: A cuántas personas les han hecho el test en la [India]{"entity": "country_code", "value": "IN"}?
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_no: de ningún modo
  - utter_covid_current_statistics

## country_wrong
* country: [Grenada]{"entity": "country_code", "value": "GD"}
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_fallback_first

## country_right
* country: [Guiana]{"entity": "country_code", "value": "GY"}
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
* covid_situation_infected: Cuántos están infectados en [China]{"entity": "country_code", "value": "CN"}?
    - utter_want_to_add_country
* vocative_yes: De acuerdo
    - utter_ask_which_country
* country: [Burma]{"entity": "country_code", "value": "MM"}
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
* covid_situation_infected: A qué número de casos activos asciende el número en los [Estados Unidos]{"entity": "country_code", "value": "US"}?
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
* covid_situation_infected: Cuantós infectados hay en [Japón]{"entity": "country_code", "value": "JP"}?
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
* covid_situation_infected: Qué cantidad de personas tienen covid en [Ecuador]{"entity": "country_code", "value": "EC"}?
    - utter_want_to_add_country
* vocative_yes: Por supuesto
    - utter_ask_which_country
* country: [Western Sahara]{"entity": "country_code", "value": "EH"}
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
* covid_situation_infected: Cuantos casos en
    - utter_want_to_add_country
* vocative_yes: Seguramente sí
    - utter_ask_which_country
* country: [Sancta Sedes]{"entity": "country_code", "value": "VA"}
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
* covid_situation_infected: Cuantos casos en
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

## current_statistics_migation1
* covid_situation: Números actuales
    - utter_want_to_add_country
* covid_current_statistics: Noticias al momento en [Alemania]{"entity": "country_code", "value": "DE"}
    - slot{"country_code": "PT"}
    - action_search_stats
    - slot{"search_successful": "ok"}
    - slot{"country": "Portugal"}
    - slot{"active_cases": 12424}
    - slot{"new_cases": 0}
    - slot{"total_cases": 52945}
    - slot{"total_recovered": 38760}
    - slot{"total_deaths": 1761}
    - slot{"total_tests": 1753524}
    - slot{"new_deaths": 0}
    - slot{"total_infected_critical": 29}
    - utter_covid_situation