# 🧘 AIMeditationCoach - Your Personalized AI Meditation Guide 🧠

This project provides an interactive AI meditation experience. It leverages a large language model and RAG with a Qdrant database to generate personalized guided meditation scripts based on user input and offers a follow-up coaching session for reflection and support.

## Overview 🧐

The core functionality of this project includes:

* **Emotionally Adaptive Meditation Generation:** Takes user input about their emotional state or goals to generate tailored guided meditation scripts.
* **Natural Guidance:** The generated scripts use second-person narration with a calm, supportive tone and incorporate natural pauses for a more immersive experience.
* **Post-Meditation Coaching:** Offers an optional follow-up conversation with an AI coach for reflection, growth, or simply listening.
* **Contextual Awareness:** Maintains a short-term memory of the conversation to provide more relevant and coherent responses during the coaching session.

## Technologies Used 💻

* **Python**
* **Langchain**
    * **QdrantVectorStore**
    * **HuggingFaceEmbeddings**
    * **VertexAI (Gemini)**
    * **Prompt Engineering**
    * **ConversationBufferWindowMemory:** For maintaining context during the coaching session.
* **Own dataset:** [Link Text](https://huggingface.co/datasets/AlbertoB12/GuidedMeditations1)
  * Data Augmentation and Synthetic Data Generation starting from an already existing dataset: [Link Text](https://huggingface.co/datasets/BuildaByte/Meditation-miniset-v0.1)

## Key Features ✨

* **Personalized Meditations:** Generates meditation scripts tailored to individual needs.
* **Natural and Supportive Tone:** Uses a calming and encouraging voice for guidance.
* **Incorporates Pauses:** Marks pauses naturally for a better spoken experience.
* **Follow-Up AI Coaching:** Provides an opportunity for reflection and conversation after meditation.
* **Contextual Chat:** Remembers recent interactions for more coherent coaching.
* **Potential for Knowledge Retrieval:** Includes setup for a vector store, suggesting future capability to incorporate specific meditation techniques or information.

## Potential Improvements ✨

* **Text-to-Speech integration**
* **User Interface:** Create a more user-friendly interface using FastAPI.
