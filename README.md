# 🧘 AIMeditationCoach - Your Personalized AI Meditation Guide 🧠

This project provides an interactive AI meditation experience. It leverages a large language model and LangChain to generate personalized guided meditation scripts based on user input and offers a follow-up coaching session for reflection and support.

The idea for the project arose from my own dataset:
* **Own dataset:** [Link Text](https://huggingface.co/datasets/AlbertoB12/GuidedMeditations1)
  * Data Augmentation and Synthetic Data Generation starting from an already existing dataset: [Link Text](https://huggingface.co/datasets/BuildaByte/Meditation-miniset-v0.1)
  * To check how the dataset was generated, see the code (Dataset_creation.ipynb).
This project is an attempt to create an economically viable application, avoiding the high costs of creating a sufficient dataset, fine-tuning a custom model, and hosting the model in the cloud. To do this, it relies on frontier models and prompt engineering.

## Overview 🧐

The core functionality of this project includes:

* **Emotionally Adaptive Meditation Generation:** Takes user input about their emotional state or goals to generate tailored guided meditation scripts.
* **Natural Guidance:** The generated scripts use second-person narration with a calm, supportive tone and incorporate natural pauses for a more immersive experience.
* **Post-Meditation Coaching:** Offers an optional follow-up conversation with an AI coach for reflection, growth, or simply listening.
* **Contextual Awareness:** Maintains a short-term memory of the conversation to provide more relevant and coherent responses during the coaching session.

## Technologies Used 💻

* **Python**
* **Langchain**
    * **VertexAI (Gemini)**
    * **Prompt Engineering**
    * **ConversationBufferWindowMemory:** For maintaining context during the coaching session.

## Key Features ✨

* **Personalized Meditations:** Generates meditation scripts tailored to individual needs.
* **Natural and Supportive Tone:** Uses a calming and encouraging voice for guidance.
* **Incorporates Pauses:** Marks pauses naturally for a better spoken experience.
* **Follow-Up AI Coaching:** Provides an opportunity for reflection and conversation after meditation.
* **Contextual Chat:** Remembers recent interactions for more coherent coaching.

## Potential Improvements ✨

* **Text-to-Speech integration**
* **User Interface:** Create a more user-friendly interface using FastAPI.
