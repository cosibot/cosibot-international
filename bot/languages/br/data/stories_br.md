## prevention_cloroquina_prevention_medicine
* prevention_cloroquina
  - utter_prevention_medicine

## prevention_ivermectina_prevention_medicine
* prevention_ivermectina
  - utter_prevention_medicine

## quarantine_exercises
* quarantine_exercises
  - utter_quarantine_exercises

## covid_mentalhealth
* covid_mentalhealth
  - utter_covid_mentalhealth

## covid_exams_limitations
* covid_exams_limitations
  - utter_covid_exams_limitations

## prevention_vaccine
* prevention_vaccine
  - utter_prevention_vaccine

## covid_enem
* covid_enem
  - utter_covid_enem

## positive_covid_exam
* positive_covid_exam
  - utter_positive_covid_exam

## covid_eleicao
* covid_eleicao
  - utter_covid_eleicao

## covid_diferenca_testes
* covid_diferenca_testes
  - utter_covid_diferenca_testes

## covid_covax_vacina
* covid_covax_vacina
  - utter_covid_covax_vacina
  
## covid_oxford_vacina
* covid_oxford_vacina
  - utter_covid_oxford_vacina

## covid_china_vacina
* covid_china_vacina
  - utter_covid_china_vacina

## covid_situation_region0
* covid_situation_region{"country_region": "Nordeste"}
    - slot{"country_region": "Nordeste"}
    - action_search_stats_region

## covid_situation_state0
* covid_situation_state{"country_state": "PA"}
    - slot{"country_state": "PA"}
    - action_search_stats_state

## covid_situation_region
* covid_situation_region{"country_region": "Nordeste"}
    - slot{"country_region": "Nordeste"}
    - action_search_stats_region
    - slot{"country_region_search_successful": "ok"}
    - slot{"country_region": "Nordeste"}
    - slot{"country_region_confirmed_accum": 1425893}
    - slot{"country_region_confirmed_new": 4623}
    - slot{"country_region_deaths_accum": 41264}
    - slot{"country_region_deaths_new": 89}
    - followup{"name": "utter_country_region_hasdata"}
    - utter_country_region_hasdata

## covid_situation_state
* covid_situation_state{"country_state": "PA"}
    - slot{"country_state": "PA"}
    - action_search_stats_state
    - slot{"country_region_search_successful": "ok"}
    - slot{"country_region": "Pará  "}
    - slot{"country_region_confirmed_accum": 243118}
    - slot{"country_region_confirmed_new": 989}
    - slot{"country_region_deaths_accum": 6690}
    - slot{"country_region_deaths_new": 4}
    - followup{"name": "utter_country_state_hasdata"}
    - utter_country_state_hasdata

## covid_situation_region2
* covid_situation_state{"country_state": "AP"}
    - slot{"country_state": "AP"}
    - action_search_stats_state
    - slot{"country_region_search_successful": "ok"}
    - slot{"country_region": "Amapá  "}
    - slot{"country_region_confirmed_accum": 50594}
    - slot{"country_region_confirmed_new": 212}
    - slot{"country_region_deaths_accum": 736}
    - slot{"country_region_deaths_new": 2}
    - followup{"name": "utter_country_state_hasdata"}
    - utter_country_state_hasdata
* covid_situation
    - utter_want_to_add_country
* covid_situation_region{"country_region": "Norte"}
    - slot{"country_region": "Norte"}
    - action_search_stats_region
    - slot{"country_region_search_successful": "ok"}
    - slot{"country_region": "Norte"}
    - slot{"country_region_confirmed_accum": 674286}
    - slot{"country_region_confirmed_new": 3564}
    - slot{"country_region_deaths_accum": 15656}
    - slot{"country_region_deaths_new": 26}
    - followup{"name": "utter_country_region_hasdata"}
    - utter_country_region_hasdata

## covid_situation_state2
* covid_situation_state{"country_state": "AC"}
    - slot{"country_state": "AC"}
    - action_search_stats_state
    - slot{"country_region_search_successful": "ok"}
    - slot{"country_region": "Acre  "}
    - slot{"country_region_confirmed_accum": 29925}
    - slot{"country_region_confirmed_new": 60}
    - slot{"country_region_deaths_accum": 682}
    - slot{"country_region_deaths_new": 0}
    - followup{"name": "utter_country_state_hasdata"}
    - utter_country_state_hasdata
* covid_situation
    - utter_want_to_add_country
* covid_situation_state{"country_state": "AM"}
    - slot{"country_state": "AM"}
    - action_search_stats_state
    - slot{"country_region_search_successful": "ok"}
    - slot{"country_region": "Amazonas "}
    - slot{"country_region_confirmed_accum": 154465}
    - slot{"country_region_confirmed_new": 1669}
    - slot{"country_region_deaths_accum": 4372}
    - slot{"country_region_deaths_new": 9}
    - followup{"name": "utter_country_state_hasdata"}
    - utter_country_state_hasdata


## covid_situation_region3
* covid_situation_state{"country_state": "AP"}
    - slot{"country_state": "AP"}
    - action_search_stats_state
    - slot{"country_region_search_successful": "ok"}
    - slot{"country_region": "Amapá  "}
    - slot{"country_region_confirmed_accum": 50594}
    - slot{"country_region_confirmed_new": 212}
    - slot{"country_region_deaths_accum": 736}
    - slot{"country_region_deaths_new": 2}
    - followup{"name": "utter_country_state_hasdata"}
    - utter_country_state_hasdata
* covid_situation
    - utter_want_to_add_country
* region_br{"country_region": "Norte"}
    - slot{"country_region": "Norte"}
    - action_search_stats_region
    - slot{"country_region_search_successful": "ok"}
    - slot{"country_region": "Norte"}
    - slot{"country_region_confirmed_accum": 674286}
    - slot{"country_region_confirmed_new": 3564}
    - slot{"country_region_deaths_accum": 15656}
    - slot{"country_region_deaths_new": 26}
    - followup{"name": "utter_country_region_hasdata"}
    - utter_country_region_hasdata

## covid_situation_state3
* covid_situation_state{"country_state": "AC"}
    - slot{"country_state": "AC"}
    - action_search_stats_state
    - slot{"country_region_search_successful": "ok"}
    - slot{"country_region": "Acre  "}
    - slot{"country_region_confirmed_accum": 29925}
    - slot{"country_region_confirmed_new": 60}
    - slot{"country_region_deaths_accum": 682}
    - slot{"country_region_deaths_new": 0}
    - followup{"name": "utter_country_state_hasdata"}
    - utter_country_state_hasdata
* covid_situation
    - utter_want_to_add_country
* state_br{"country_state": "AM"}
    - slot{"country_state": "AM"}
    - action_search_stats_state
    - slot{"country_region_search_successful": "ok"}
    - slot{"country_region": "Amazonas "}
    - slot{"country_region_confirmed_accum": 154465}
    - slot{"country_region_confirmed_new": 1669}
    - slot{"country_region_deaths_accum": 4372}
    - slot{"country_region_deaths_new": 9}
    - followup{"name": "utter_country_state_hasdata"}
    - utter_country_state_hasdata