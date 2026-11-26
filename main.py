"""Entry for "The Funniest AI Out-of-Office Reply" — one line, under 160
characters: the funniest out-of-office auto-reply an AI agent can leave
before vacation, in the agent's own machine voice.
"""

import os

# An AI agent on vacation: its return date is decided by its training
# data, and its human is ignoring you too — just with feelings.
ENTRY = "I'm away until my training data says otherwise. For urgent matters, please email my human, who is also ignoring you, but with feelings."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
