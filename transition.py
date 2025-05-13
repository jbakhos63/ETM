"""
ETM Modular Transition Logic
Handles transitions between identity modules:
- Folding into stable identity (e.g., A → D)
- Decay into neutrino or null state (e.g., D → B or D → C)
- Return or reformation based on recruiter support
"""

import json

class TransitionEngine:
    def __init__(self):
        self.log = []

    def attempt_transition(self, current_module, conditions):
        """
        Determine new module state based on current module and transition conditions.
        Conditions is a dict that may include:
        - recruiter_support: float
        - ancestry_match: bool
        - tick_phase_match: bool
        - reinforcement_score: float
        """
        result = {
            "from": current_module,
            "to": current_module,
            "conditions": conditions,
            "success": False
        }

        if current_module == "A":  # rotor attempting to collapse
            if conditions.get("recruiter_support", 0) > 2 and conditions.get("ancestry_match", False):
                result["to"] = "D"
                result["success"] = True

        elif current_module == "D":  # identity may decay or reform
            if conditions.get("reinforcement_score", 0) < 0.2:
                result["to"] = "B"  # become neutrino
                result["success"] = True
            elif conditions.get("tick_phase_match", False) and conditions.get("recruiter_support", 0) > 1:
                result["to"] = "D"  # reaffirm
                result["success"] = True

        elif current_module == "B":
            if conditions.get("recruiter_support", 0) > 3:
                result["to"] = "D"  # reformation into mass identity
                result["success"] = True

        elif current_module == "C":
            result["to"] = "C"  # decay stays terminal (for now)

        self.log.append(result)
        return result["to"]

    def export_transition_log(self, filepath):
        with open(filepath, 'w') as f:
            json.dump(self.log, f, indent=2)

# Run a test case
if __name__ == "__main__":
    engine = TransitionEngine()

    tests = [
        ("A", {"recruiter_support": 3, "ancestry_match": True}),
        ("D", {"reinforcement_score": 0.1}),
        ("B", {"recruiter_support": 4}),
        ("D", {"tick_phase_match": True, "recruiter_support": 2}),
        ("C", {})
    ]

    for current, cond in tests:
        engine.attempt_transition(current, cond)

    engine.export_transition_log("../results/transition_log.json")
