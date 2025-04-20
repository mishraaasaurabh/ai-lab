def unify(term1, term2):
    """
    A simple unification function for terms.
    Returns a substitution dictionary if terms can be unified.
    Otherwise, returns None.
    """
    if term1 == term2:
        return {}
    
    if isinstance(term1, str) and term1.startswith("x"):  # variable
        return {term1: term2}
    elif isinstance(term2, str) and term2.startswith("x"):  # variable
        return {term2: term1}
    else:
        return None


def resolution(clause1, clause2):
    """
    Applies resolution on two clauses.
    """
    for literal in clause1:
        if literal.startswith("¬"):
            neg_literal = literal[1:]
            if neg_literal in clause2:
                # Resolve the literal
                new_clause = (set(clause1) | set(clause2)) - {literal, neg_literal}
                return new_clause
    return None


# Facts in the smart home system (like propositions)
facts = [
    {"Door(locked)"},       # Door is locked
    {"¬Door(locked)"},      # Door is not locked (alternative fact)
    {"Condition(sunny)"},   # It's sunny outside
    {"¬Condition(sunny)"},  # It's not sunny outside
]

# Goal: Find if the door is open
goal = {"Door(open)"}

# Clauses for resolution
clause1 = {"Door(locked)", "¬Door(locked)"}
clause2 = {"Condition(sunny)", "Door(open)"}

# Perform unification and resolution
substitution = unify("x", "sunny")

if substitution:
    print(f"Unification successful: {substitution}")
else:
    print("Unification failed!")

# Use resolution to check if the door is open based on the facts and goal
resolved_clause = resolution(clause1, clause2)
if resolved_clause:
    print(f"Resolved clause: {resolved_clause}")
else:
    print("No resolution possible.")

# Check if goal is met
if resolved_clause and goal.issubset(resolved_clause):
    print("The door is open!")
else:
    print("The door is not open!")
