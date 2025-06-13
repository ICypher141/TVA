import spacy

# Load custom celestial NER model
nlp = spacy.load("models/custom_celestial_ner")

def parse_command(command):
    doc = nlp(command)
    intent = None
    object_name = None

    for token in doc:
        if token.lemma_ in ["find", "point", "show", "give"]:
            intent = token.lemma_

    for ent in doc.ents:
        if ent.label_ == "CELESTIAL_OBJECT":
            object_name = ent.text

    return intent, object_name
