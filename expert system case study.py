class ExpertSystem:
    def __init__(self):
        self.rules = {
            "flu": {"fever", "cough"},
            "cold": {"headache", "sore_throat"},
            "food_poisoning": {"nausea", "abdominal_pain"},
            "heart_attack": {"chest_pain", "difficulty_breathing"},
            "measles": {"rash", "swollen_lymph_nodes"}
        }

    def diagnose(self, symptoms):
        possible_diseases = []

        # Check which diseases match the symptoms
        for disease, required_symptoms in self.rules.items():
            if required_symptoms.issubset(symptoms):
                possible_diseases.append(disease)

        if not possible_diseases:
            return "No diagnosis found based on the provided symptoms."
        return possible_diseases


# Example usage:
if __name__ == "__main__":
    expert_system = ExpertSystem()

    # Simulate user input: symptoms
    patient_symptoms = {"fever", "cough"}  # example symptoms from the user

    diagnosis = expert_system.diagnose(patient_symptoms)

    if isinstance(diagnosis, list):
        print("Possible diagnoses:")
        for disease in diagnosis:
            print(f"- {disease}")
    else:
        print(diagnosis)
