import json

# Etsii esimerkit kovakoodatusta tiedostosta (esim. ilman FAISSia aluksi)
def retrieve_examples(prompt):
    with open("examples.jsonl", "r", encoding="utf-8") as f:
        examples = [json.loads(line) for line in f]
    # Palautetaan yksinkertaisesti 2 ensimmäistä esimerkkiä (voit parantaa myöhemmin)
    return examples[:13]
