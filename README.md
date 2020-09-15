[![License: MIT](https://img.shields.io/badge/License-GPL-teal.svg)](https://opensource.org/licenses/GPL-3.0)
[![Build Status](https://github.com/cosibot/cosibot-international/workflows/ci-tests/badge.svg)](https://github.com/cosibot/cosibot-international/actions)

# Cosibot International

<img align="right" width="200" height="201" alt="Helen-wp" src="https://cosibot.org/wp-content/uploads/2020/04/Helen-wp-3.png"></img>
[Cosibot](https://cosibot.org/) – Covid Stay Informed Bot is a non-profit initiative developed by [ROBO.AI](https://robo-ai.com/) to provide citizens around the world with credible and up-to-date information on Coronavirus, using different sources and making it available in a single application.

This is the international version, available in English and Brazilian Portuguese.

## Add Cosibot to your website
You can add the Cosibot Corona Virus Chatbot as a popup to your website. It is straightforward and it can be done in just three simple steps:
1. [Ask for an API key](https://cosibot.org/contact)
2. Ask your web developer to add the code snippet to your website - you can choose to add the International version or one of the Country bots available.
```javascript
<script src="https://cdn.cosibot.org/widget/cosibot.js"></script>
<script>
var config = {
   bot: 'covid-int-en',
   key: '<Your API key>',
   language: 'en'
}
Cosibot.init(config);
</script>
```
3. Ta-da, The Cosibot is there. Tell the world about it!

## This is an open source project - Contribute!
### Structure
Because this is a multi-language bot, it is structured as follows: 
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
You can also create stories for a specific bot. For that you just need to add a stories file inside the bot data folder (i.e. bot/languages/en/data/).

### Train the bot
If you want to train the bot to test it locally, you can do it by running the following command (inside the bot folder): 
```bash
rasa train --config languages/en/config.yml --domain languages/en/domain.yml
           --data languages/en/data languages/stories.md
           --out languages/en/models --fixed-model-name model-en
```
Note: you can replace 'en' with another language code as long as it's implemented in the bot.

### Interact with the bot
To interact with the bot locally you can run:
```bash
rasa run actions
```
```bash
rasa shell --model languages/en/models/model-en.tar.gz
```

## Get in contact
For any queries you might have, you can contact us [here](https://cosibot.org/contact).
You can also find us on [Facebook](https://www.facebook.com/cosibot), [Twitter](https://twitter.com/cosibot) and [Linkedin](https://www.linkedin.com/company/cosibot/).