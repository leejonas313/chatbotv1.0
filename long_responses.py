import random

R_EATING = "As a procurement bot, I don't handle food orders, but I can help you with supplier details."
R_ADVICE = "For any procurement queries, you can consult the company's procurement policy or ask me here!"



def unknown():
    response = ["I'm not sure I understand. Can you ask about procurement?",
                "I couldn't catch that. Please try rephrasing.",
                "I'm not sure what you're asking. Do you need help with procurement?",
                "That doesn't seem related to procurement. Can you clarify?"][
        random.randrange(4)]
    return response
