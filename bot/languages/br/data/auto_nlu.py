import re, random, unidecode

utters_regions = [
        "- Total de infetados existem em @fill\n",
        "- Contagem infectados no total em @fill\n",
        "- Contagem infectada ativa em @fill\n",
        "- Contagem infectada ativa na @fill\n",
        "- Casos confirmados em @fill\n",
        "- Contagem infectados no total em @fill\n",
        "- Contagem infectada ativa em @fill\n",
        "- Atualização em @fill\n",
        "- Dados atualizados em @fill\n",
        "- Últimos dados de @fill\n",
        "- Quantos casos existem em @fill\n",
        "- Quantos infectados existem neste momento em @fill\n",
        "- Coronavirus em @fill\n",
        "- Quantos infectados existem neste momento no @fill\n",
        "- Quantos infectados existem neste momento na @fill\n",
        "- Coronavirus na @fill\n",
        "- numeros para hoje @fill\n"
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
        "- Casos confirmados em @fill\n",
        "- Contagem infectada ativa em @fill\n",
        "- Contagem infectados no total em @fill\n",
        "- Qual é o número de casos confirmados em @fill\n",
        "- Atualização em @fill\n",
        "- Dados atualizados em @fill\n",
        "- Quantos mais infetados em @fill\n",
        "- Últimos dados de @fill\n",
        "- Dados de hoje de novos infetados @fill\n",
        "- Dados de hoje em @fill\n",
        "- Dados de hoje de casos em @fill\n",
        "- Quantos casos existem em @fill ?\n",
        "- Quantos infectados existem neste momento em @fill ?\n",
        "- Quantos infetados tem a @fill ?\n",
        "- Quantos infetados tem @fill ?\n",
        "- quantos casos há em @fill ?\n",
        "- Coronavirus em @fill ?\n",
        "- Situação actual em @fill ?\n",
        "- Situação @fill ?\n",
        "- Informações sobre @fill ?\n",
        "- Situação actualizada em @fill ?\n",
        "- número de infetados em @fill ?\n"
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