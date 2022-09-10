import random

verbs = ['Leverage', 'Buy', 'Sell' , 'Go long', 'Go Short', 'Drink', 'Meditate', 'Surrender', 'Manifest', 'Stop']
adjectives = ['Cute', 'Adorable', 'Beautiful', 'Serene', 'Lovely', 'Smart', 'Studious']
nouns = ['Rain', 'Snow', 'Fire', 'Water', 'Wind', 'Earth', 'Light', 'Love']
verb = random.choice(verbs)
adjective = random.choice(adjectives)
noun = random.choice(nouns)
phrase = verb + ' ' + adjective + ' ' + noun
print(phrase)
