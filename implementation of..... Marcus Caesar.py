# Defining Facts and Rules

class KnowledgeBase:
    def __init__(self):
        self.facts = {}
        self.rules = []

    def add_fact(self, fact):
        self.facts[fact] = True

    def add_rule(self, rule):
        self.rules.append(rule)

    def get_fact(self, fact):
        return self.facts.get(fact, False)

# Knowledge Base (KB)
kb = KnowledgeBase()

# Facts (in KB)
kb.add_fact('Man(Marcus)')
kb.add_fact('Pompeian(Marcus)')
kb.add_fact('Ruler(Caesar)')
kb.add_fact('TriedToAssassinate(Marcus, Caesar)')

# Rule 1: All Pompeians are Romans
def rule_pompeians_are_romans():
    if kb.get_fact('Pompeian(Marcus)'):
        kb.add_fact('Roman(Marcus)')

# Rule 2: All Romans are either loyal to Caesar or hate him
def rule_romans_loyal_or_hate():
    if kb.get_fact('Roman(Marcus)'):
        if not kb.get_fact('LoyalTo(Marcus, Caesar)'):
            kb.add_fact('Hates(Marcus, Caesar)')

# Rule 3: People try to assassinate rulers they are not loyal to
def rule_assassination_reason():
    if kb.get_fact('TriedToAssassinate(Marcus, Caesar)'):
        kb.add_fact('¬LoyalTo(Marcus, Caesar)')

# Adding all the rules
kb.add_rule(rule_pompeians_are_romans)
kb.add_rule(rule_romans_loyal_or_hate)
kb.add_rule(rule_assassination_reason)

# Applying rules to populate facts
for rule in kb.rules:
    rule()

# Inference for the question: Did Marcus hate Caesar?
def did_marcus_hate_caesar():
    # Check if the fact Hates(Marcus, Caesar) is in the KB
    return kb.get_fact('Hates(Marcus, Caesar)')

# Run inference
result = did_marcus_hate_caesar()
print("Did Marcus hate Caesar? ", result)
