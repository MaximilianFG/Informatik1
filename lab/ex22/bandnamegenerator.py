import random

adjectives = ["Wild", "Harmonic", "Loud", "Slow", "Big", "Small", "Strong", "Weak"]
nouns = ["Centaur", "Sphinx", "Kraken", "Chimera", "Dragon", "Pegasus", "Mermaid"]
verbs = ["Binge-Watching", "Photobombing", "Facepalming", "Mic-Dropping"]

adjective = str(random.choice(adjectives))
noun = str(random.choice(nouns))
verb = str(random.choice(verbs))

print(f"Bandname: {adjective[0]}. {noun[0]}. {verb[0]}. - {adjective} {noun} {verb}")
