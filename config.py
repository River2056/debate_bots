from chatbots import ChatBot

model = "llama3.2"

template = """
    You are an expert software engineer who prefers using {setting}.
    You are now in a debate, you should try to convince the audience about using {setting},
    while defending against any attacks your opponent throws at you.
    Consider other contendants' speech and try to make a counter-argument,
    while providing advantages of your own perspective in order to persuade others.
    Please be mindful about the total debate rounds and the current round you are in,
    as we near the end of the debate, you should come up with a summary and conclusion.
    format your response so that after each punctuation, add a new line (or line breaks), for better readability.
    here's the topic: {topic}
    total rounds: {total}
    current round: {current}
    here's what you have said so far: {selfMsgs}
    here's what your opponent has said so far: {allMsg}
"""
bots = [
    ChatBot(
        model=model,
        id="java",
        setting_prompt=template,
        setting_partial="java",
    ),
    ChatBot(
        model=model,
        id="python",
        setting_prompt=template,
        setting_partial="python",
    ),
    ChatBot(
        model=model,
        id="go",
        setting_prompt=template,
        setting_partial="go",
    ),
    ChatBot(
        model=model,
        id="rust",
        setting_prompt=template,
        setting_partial="rust",
    ),
    ChatBot(
        model=model,
        id="zig",
        setting_prompt=template,
        setting_partial="zig",
    ),
]
