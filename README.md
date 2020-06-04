# cosibot-international


## How to create a custom SpaCy component based on hugging face's neuralcoref

It is recommended that you install the neuralcoref package from their git repo. 
Follow the instructions here: https://github.com/huggingface/neuralcoref

On the bot directory run
```bash
python mkmodel.py
```
This will save the spaCy model on disk. 

```bash
python -m spacy package neuralcoref . --force
```
This will create a package for our model. 

At this point we need to change the __init__.py file inside our packaged model like the following. 

```python
# coding: utf8
from __future__ import unicode_literals

from pathlib import Path
from spacy.util import load_model_from_init_py, get_model_meta
from spacy.language import Language
from neuralcoref import NeuralCoref

__version__ = get_model_meta(Path(__file__).parent)['version']


def load(**overrides):
    Language.factories['neuralcoref'] = lambda nlp, **cfg: NeuralCoref(nlp.vocab, **cfg)
    return load_model_from_init_py(__file__, **overrides)
```

We needed to do this because we're adding a new component to the pipeline and since SpaCy has no prior knowledge of it we need to declare it with the Language.factories statement above. 

```bash
cd en_neuralcoref
python setup.py sdist
cd .. 
```
This will create a tar file that we can later pip install. 

```bash
python -m pip install en_neuralcoref-2.1.0/dist/en_proglang-2.2.5.tar.gz
```
This will install the model as a package. 

Based on https://blog.rasa.com/custom-spacy-components/ and adapted to our needs. 