import json
import os

# Define the path to the interactions storage file
INTERACTIONS_FILE = 'interactions.json'

def save_interaction(prompt, response):
    """Save a prompt-response interaction to the storage file."""
    interactions = load_interactions()
    interactions.append({"prompt": prompt, "response": response})

    with open(INTERACTIONS_FILE, 'w') as file:
        json.dump(interactions, file, indent=4)

def load_interactions():
    """Load all interactions from the storage file."""
    if not os.path.exists(INTERACTIONS_FILE):
        return []
    with open(INTERACTIONS_FILE, 'r') as file:
        return json.load(file)
