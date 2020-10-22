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

## covid_enem
* covid_enem
  - utter_covid_enem

## covid_eleicao
* covid_eleicao
  - utter_covid_eleicao

## covid_diferenca_testes
* covid_diferenca_testes
  - utter_covid_diferenca_testes

## covid_vacinas_teste
* covid_vacinas_teste
  - utter_covid_vacinas_teste

## covid_covax_vacina
* covid_covax_vacina
  - utter_covid_covax_vacina
  
## covid_oxford_vacina
* covid_oxford_vacina
  - utter_covid_oxford_vacina

## covid_china_vacina
* covid_china_vacina
  - utter_covid_china_vacina

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