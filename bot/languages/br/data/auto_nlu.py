import re, random, unidecode

utters_regions = [
        "- Atualização em @fill\n",
        "- Atualização na @fill\n",
        "- Atualização no @fill\n",
        "- Casos confirmados em @fill\n",
        "- Casos confirmados na @fill\n",
        "- Casos confirmados no @fill\n",
        "- Contagem de infectados ativos em @fill\n",
        "- Contagem de infectados ativos na @fill\n",
        "- Contagem de infectados ativos no @fill\n",
        "- Contagem de infectados no total em @fill\n",
        "- Contagem de infectados no total na @fill\n",
        "- Contagem de infectados no total no @fill\n",
        "- Contagem infectada ativa em @fill\n",
        "- Contagem infectada ativa na @fill\n",
        "- Contagem infectada ativa no @fill\n",
        "- Contagem infectados ativos em @fill\n",
        "- Contagem infectados ativos na @fill\n",
        "- Contagem infectados ativos no @fill\n",
        "- Contagem infectados no total em @fill\n",
        "- Contagem infectados no total na @fill\n",
        "- Contagem infectados no total no @fill\n",
        "- Coronavirus em @fill\n",
        "- Coronavirus na @fill\n",
        "- Coronavirus no @fill\n",
        "- Coronovirus em @fill\n",
        "- Coronovirus no @fill\n",
        "- Covid 19 em @fill\n",
        "- Covid 19 na @fill\n",
        "- Covid 19 no @fill\n",
        "- COVID-19 em @fill\n",
        "- COVID-19 na @fill\n",
        "- COVID-19 no @fill\n",
        "- Dados atualizados em @fill\n",
        "- Dados atualizados na @fill\n",
        "- Dados atualizados no @fill\n",
        "- Número de casos confirmados em @fill\n",
        "- Número de casos confirmados na @fill\n",
        "- Número de casos confirmados no @fill\n",
        "- numeros para hoje @fill\n"
        "- números para hoje em @fill\n"
        "- números para hoje na @fill\n"
        "- números para hoje no @fill\n"
        "- Quantos casos confirmados em @fill\n",
        "- Quantos casos confirmados na @fill\n",
        "- Quantos casos confirmados no @fill\n",
        "- Quantos casos existem em @fill\n",
        "- Quantos casos existem na @fill\n",
        "- Quantos casos existem no @fill\n",
        "- Quantos infectados em @fill\n",
        "- Quantos infectados existem actualmente em @fill\n",
        "- Quantos infectados existem actualmente na @fill\n",
        "- Quantos infectados existem actualmente no @fill\n",
        "- Quantos infectados existem neste momento em @fill\n",
        "- Quantos infectados existem neste momento na @fill\n",
        "- Quantos infectados existem neste momento no @fill\n",
        "- Quantos infectados existno actualmente na @fill\n",
        "- Quantos infectados na @fill\n",
        "- Quantos infectados no @fill\n",
        "- Total de infetados existem em @fill\n",
        "- Total de infetados existem na @fill\n",
        "- Total de infetados existem no @fill\n",
        "- Últimos dados de @fill\n"
    ]

synonym_regions = [
    "Região @fill",
    "Região a @fill"
]

regions = [
    "Centro-Oeste",
    "Nordeste",
    "Norte",
    "Sudeste",
    "Sul"
]


utters_states = [
        "- Atualização em @fill\n",
        "- Atualização na @fill\n",
        "- Atualização no @fill\n",
        "- Casos confirmados em @fill\n",
        "- Casos confirmados na @fill\n",
        "- Casos confirmados no @fill\n",
        "- Contagem de infectados ativos em @fill\n",
        "- Contagem de infectados ativos na @fill\n",
        "- Contagem de infectados ativos no @fill\n",
        "- Contagem de infectados no total em @fill\n",
        "- Contagem de infectados no total na @fill\n",
        "- Contagem de infectados no total no @fill\n",
        "- Contagem infectada ativa em @fill\n",
        "- Contagem infectada ativa na @fill\n",
        "- Contagem infectada ativa no @fill\n",
        "- Contagem infectados ativos em @fill\n",
        "- Contagem infectados ativos na @fill\n",
        "- Contagem infectados ativos no @fill\n",
        "- Contagem infectados no total em @fill\n",
        "- Contagem infectados no total na @fill\n",
        "- Contagem infectados no total no @fill\n",
        "- Coronavirus em @fill\n",
        "- Coronavirus na @fill\n",
        "- Coronavirus no @fill\n",
        "- Coronovirus em @fill\n",
        "- Coronovirus no @fill\n",
        "- Covid 19 em @fill\n",
        "- Covid 19 na @fill\n",
        "- Covid 19 no @fill\n",
        "- COVID-19 em @fill\n",
        "- COVID-19 na @fill\n",
        "- COVID-19 no @fill\n",
        "- Dados atualizados em @fill\n",
        "- Dados atualizados na @fill\n",
        "- Dados atualizados no @fill\n",
        "- Número de casos confirmados em @fill\n",
        "- Número de casos confirmados na @fill\n",
        "- Número de casos confirmados no @fill\n",
        "- numeros para hoje @fill\n"
        "- números para hoje em @fill\n"
        "- números para hoje na @fill\n"
        "- números para hoje no @fill\n"
        "- Quantos casos confirmados em @fill\n",
        "- Quantos casos confirmados na @fill\n",
        "- Quantos casos confirmados no @fill\n",
        "- Quantos casos existem em @fill\n",
        "- Quantos casos existem na @fill\n",
        "- Quantos casos existem no @fill\n",
        "- Quantos infectados em @fill\n",
        "- Quantos infectados existem actualmente em @fill\n",
        "- Quantos infectados existem actualmente na @fill\n",
        "- Quantos infectados existem actualmente no @fill\n",
        "- Quantos infectados existem neste momento em @fill\n",
        "- Quantos infectados existem neste momento na @fill\n",
        "- Quantos infectados existem neste momento no @fill\n",
        "- Quantos infectados existno actualmente na @fill\n",
        "- Quantos infectados na @fill\n",
        "- Quantos infectados no @fill\n",
        "- Total de infetados existem em @fill\n",
        "- Total de infetados existem na @fill\n",
        "- Total de infetados existem no @fill\n",
        "- Últimos dados de @fill\n"
    ]

synonym_states = {
    "AC": "Acre",
    "AL": "Alagoas",
    "AP": "Amapá",
    "AM": "Amazonas",
    "BA": "Bahia",
    "CE": "Ceará",
    "DF": "Distrito Federal",
    "ES": "Espírito Santo",
    "GO": "Goiás",
    "MA": "Maranhão",
    "MT": "Mato Grosso",
    "MS": "Mato Grosso do Sul",
    "MG": "Minas Gerais",
    "PA": "Pará",
    "PB": "Paraíba",
    "PR": "Paraná",
    "PE": "Pernambuco",
    "PI": "Piauí",
    "RJ": "Rio de Janeiro",
    "RN": "Rio Grande do Norte",
    "RS": "Rio Grande do Sul",
    "RO": "Rondônia",
    "RR": "Roraima",
    "SC": "Santa Catarina",
    "SP": "São Paulo",
    "SE": "Sergipe",
    "TO": "Tocantins"
}

# - Total de infetados existem em [Norte]{"entity": "pt_country_region", "value": "Norte"}
# ## synonym:Norte
# - norte
# - Região Norte
# - Região a Norte

with open('nlu_new_new.txt', 'w') as new:
    for utter in utters_regions:
        for region in regions:
            #print(utter, region, "##")
            new.write(utter.replace("@fill", f"[{region}]{{\"entity\": \"country_region\", \"value\": \"{region}\"}}"))
            new.write(utter.replace("@fill", f"[{synonym_regions[random.randrange(0, len(synonym_regions))].replace('@fill', region)}]{{\"entity\": \"country_region\", \"value\": \"{region}\"}}"))
            new.write(utter.replace("@fill", f"[{region.lower()}]{{\"entity\": \"country_region\", \"value\": \"{region}\"}}"))
    new.write("\n")
    for region in regions:
        new.write(f"\n## synonym:{region}\n")
        for x in range(len(synonym_regions)):
            new.write(f"- {synonym_regions[random.randrange(0, len(synonym_regions))].replace('@fill', region)}\n")
            new.write(f"- {synonym_regions[random.randrange(0, len(synonym_regions))].replace('@fill', region).lower()}\n")
        #new.write(f"- {region.lower()}\n")
        new.write(f"- {unidecode.unidecode(region.lower()).replace('-', ' ')}\n")

    new.write("\n\n\n\n")

    for utter in utters_states:
        for state in synonym_states:
            new.write(utter.replace("@fill", f"[{synonym_states[state]}]{{\"entity\": \"country_state\", \"value\": \"{state}\"}}"))
            new.write(utter.replace("@fill", f"[{synonym_states[state].lower()}]{{\"entity\": \"country_state\", \"value\": \"{state}\"}}"))
    for state in synonym_states:
        new.write(f"\n## synonym:{state}\n")
        new.write(f"- {unidecode.unidecode(synonym_states[state].lower()).replace('-', ' ')}\n")