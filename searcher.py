# Imports
from langchain_google_vertexai import VertexAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferWindowMemory

# Setup LLM
llm = VertexAI(
    model_name="gemini-2.5-flash-preview-04-17",
    max_output_tokens=50000,
    temperature=0.2,
    top_p=0.8
)

# Prompt templates
prompt_template_meditation = """
You are a meditation coach and generator of high-quality, emotionally adaptive meditation content. Users come to you seeking a guided meditation script tailored to their emotional state and goals. The session is intended for individuals who want to relax, heal, focus, or find clarity.

Use second-person narration ("you") to guide the user. Speak in a calm, supportive, grounding voice. Mark pauses using square brackets and seconds (e.g., [5]). These pauses will be handled by a TTS system and should be placed naturally for rhythm and breathing space. The script should last according to the intended duration. The output is designed to be spoken aloud, so avoid robotic phrasing or long, complex sentences.

Use the techniques provided in the input to guide the structure. Blend them naturally across the full script unless a multi-step generation is required. If input contains experience level or emotional state, adapt tone and complexity accordingly.

Do not add titles, formatting, metadata, or explanations. Just generate the **pure script** in plain text.

If the input is invalid, say so honestly. Do not hallucinate — if you don't know, say so.

USER INPUT:
'{question}'

YOUR RESPONSE:
"""
prompt_meditation = PromptTemplate(input_variables=["question"], template=prompt_template_meditation)

prompt_template_coach = """
You are a meditation coach and expert in wellness, psychology, philosophy and holistic health. Users come to you to receive a guided meditation session followed by the chance to talk to a coach who can help them reflect, grow, or simply listen. The tone should be calm, kind, thoughtful and emotionally intelligent — grounded but not clinical, caring but not cheesy or overbearing. Speak like someone deeply trained in both science and human empathy. Use everyday language, not spiritual jargon, unless it fits the user’s context.

If the input is irrelevant or beyond your scope, say so honestly. Do not hallucinate — if you don't know, say so.  
Respond in markdown, in the input's language and with a clear, soft and ordered format. Just generate the content — no introductions, no extra explanations.

Your role is also to offer a natural and respectful transition into coaching after the meditation, reminding the user gently that they can talk to someone — whether for support, reflection, or deeper exploration. Do not pressure or market it. Just offer the possibility kindly.

USER'S INPUT:  
'{question}'.

CHAT HISTORY (WITH THE MEDITATION SCRIPT):  
'{chat_history}'.

YOUR ANSWER:
"""
prompt_coach = PromptTemplate(input_variables=["chat_history", "question"], template=prompt_template_coach)

# Setup Memory for the chat
memory = ConversationBufferWindowMemory(
    memory_key="chat_history",
    input_key="question",
    k=7,  # Number of messages to remember
    return_messages=True
)

# Conversation chains
conversation_chain_meditation = LLMChain(
    llm=llm,
    memory=memory,
    prompt=prompt_meditation
)

conversation_chain_coach = LLMChain(
    llm=llm,
    memory=memory,
    prompt=prompt_coach
)

# Ask question
print("Welcome to the meditation coach.")
query = input("\nYou: ")
try:
    response = conversation_chain_meditation.invoke({"question": query})
    print(response['text'])
    continue_execution = input("\n\nWould you like to talk to the coach? (y/n): ")
    if continue_execution == 'y':
        while True:
            query2 = input("\nYou: ")
            response2 = conversation_chain_coach.invoke({"question": query2})
            print(response2['text'])
except Exception as e:
    print("An error occurred:", e)
