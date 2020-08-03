# cosibot-international

International version of the Cosibot Initiative.
The bot is structured as follows: 

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

To add a new language, add a new folder with the language code and the specific config.yml, domain.yml, nlu.md and lookup tables files. 