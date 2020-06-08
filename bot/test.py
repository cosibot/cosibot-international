import spacy 
from typing import Text

# std_english = spacy.load("en")
# doc_2 = std_english(u'my sister has a dog. she loves him.')

# nlp = spacy.load("en_neuralcoref")
# doc = nlp(u'my sister has a sony tv. it is nice.')  

from os.path import join

# from rasa.core.interpreter import RasaNLUHttpInterpreter

# # where model_directory points to the model folder
# interpreter = RasaNLUHttpInterpreter("models/20200603-171627.tar.gz")
# interpreter.parse(u"The text I want to understand")

from rasa.nlu.model import Interpreter
from rasa.nlu.training_data import Message, TrainingData

model_dir = Text('/home/marta/two-impulse/cosibot/cosibot-international/bot/models/nlu')

metadata_file = join(model_dir, "metadata.json")
print(metadata_file)
interpreter = Interpreter.load(model_dir) ## this should be an extracted model
# result = interpreter.parse('my sister has a dog. she loves it',only_output_properties=False)

message = Message(Text('why should i wear a mask? where can i buy it?'))

# for component in interpreter.pipeline:
#     component.process(message, **interpreter.context)

spacy_nlp_neural_coref = interpreter.pipeline[0]
spacy_nlp_neural_coref.process(message, **interpreter.context)

spacy_tokenizer = interpreter.pipeline[1]
spacy_tokenizer.process(message, **interpreter.context)

spacy_ent_extractor = interpreter.pipeline[2]
spacy_ent_extractor.process(message, **interpreter.context)

dense_featurizer = interpreter.pipeline[3]
dense_featurizer.process(message, **interpreter.context)

message = Message(Text('where can i buy it?'))

# for component in interpreter.pipeline:
#     component.process(message, **interpreter.context)

spacy_nlp_neural_coref = interpreter.pipeline[0]
spacy_nlp_neural_coref.process(message, **interpreter.context)

spacy_tokenizer = interpreter.pipeline[1]
spacy_tokenizer.process(message, **interpreter.context)

spacy_ent_extractor = interpreter.pipeline[2]
spacy_ent_extractor.process(message, **interpreter.context)

dense_featurizer = interpreter.pipeline[3]
dense_featurizer.process(message, **interpreter.context)

print("")