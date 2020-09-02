[![License: MIT](https://img.shields.io/badge/License-GPL-yellow.svg)](https://opensource.org/licenses/GPL-3.0)
[![Build Status](https://github.com/cosibot/cosibot-international/workflows/ci-tests/badge.svg)](https://github.com/cosibot/cosibot-international/actions)

# Cosibot International

<img align="right" width="244" height="245" alt="Helen-wp" src="https://cosibot.org/wp-content/uploads/2020/04/Helen-wp-3.png"></img>
[Cosibot](https://cosibot.org/) – Covid Stay Informed Bot is a non-profit initiative developed by ROBO.AI to provide citizens around the world with credible and up-to-date information on Coronavirus, using different sources and making it available in a single application.

This is the international version, available in English and Brazilian Portuguese.

The bot is structured as follows: 
```
.
├── actions
│   ├── action_change_preferred_language.py
│   ├── action_check_Bot_Introduced.py
│   ├── action_default_fallback.py
│   ├── action_get_date.py
│   ├── action_get_news_request.py
│   ├── action_get_time.py
│   ├── action_search_stats.py
│   └── __init__.py
├── custom
│   ├── components
│   │   └── spacy_nlp
│   │       ├── spacy_nlp_neuralcoref.py
│   │       └── spacy_tokenizer_neuralcoref.py
│   └── policies
│       └── language_detection
│           ├── lang_change_policy.py
│           └── lid.176.ftz
├── languages
|   ├── br
|   │   ├── config.yml
|   │   ├── data
|   │   │   ├── lookup_tables
|   │   │   └── nlu.md
|   │   └── domain.yml
|   ├── en
|   │   ├── config.yml
|   │   ├── data
|   │   │   ├── lookup_tables
|   │   │   └── nlu.md
|   │   └── domain.yml
|   └── stories.md
├── credentials.yml
├── endpoints.yml
└── __init__.py
```
To add a new language, add a new folder with the language code and the specific config.yml, domain.yml, nlu.md and lookup tables files. 