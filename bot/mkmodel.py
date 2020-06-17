import spacy
# Add neural coref to SpaCy's pipe
from neuralcoref import NeuralCoref
from spacy.language import Language

from spacy.pipeline import EntityRuler

if __name__ == "__main__":
    nlp = spacy.load('en_core_web_sm')
    # nlp = spacy.load('en_core_web_sm', disable = ['ner', 'parser', 'tagger'])
    nlp.add_pipe(nlp.create_pipe('sentencizer'), first=True)
    print(nlp.pipeline)
    coref = NeuralCoref(nlp.vocab)
    nlp.add_pipe(coref, name='neuralcoref')

    # Language.factories['neuralcoref'] = lambda nlp, **cfg: coref(nlp.vocab, **cfg)
    # ruler = EntityRuler(nlp)
    # nlp.add_pipe(ruler, name='nlp_neuralcoref')
    # define the name of the model as a package
    nlp.meta["name"] = "neuralcoref"
    # save the model to disk
    nlp.to_disk(nlp.meta["name"])
    print(f"spaCy model saved over at {nlp.meta['name']}.") 
