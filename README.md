# AI Mentor Assistant – Module-Focused Learning Chatbot

## Project Overview
AI Mentor Assistant is a Streamlit-based AI chatbot designed to act as a dedicated mentor for specific technical modules. Unlike generic chatbots, this system strictly confines discussions to a user-selected domain, ensuring focused and distraction-free learning.

If a user asks a question outside the chosen module, the chatbot intentionally refuses to answer, reinforcing domain discipline and improving conceptual clarity.

## Key Objectives
- Provide module-specific mentoring
- Prevent topic drift during learning sessions
- Enable structured and controlled AI interactions
- Offer downloadable learning conversations for revision

## Supported Learning Modules
- Python
- SQL
- Power BI
- Exploratory Data Analysis (EDA)
- Machine Learning (ML)
- Deep Learning (DL)
- Generative AI (Gen AI)
- Agentic AI

## How It Works
1. Module Selection  
   The user selects a learning module before starting the session.

2. Strict Domain Enforcement  
   The AI mentor responds only to questions related to the selected module.

3. Out-of-Scope Handling  
   If a question is unrelated, the AI replies:  
   "Sorry, I don’t know about this question. Please ask something related to the selected module."

4. Interactive Chat Interface  
   Real-time chat experience using Streamlit’s chat components.

5. Session Control  
   - End conversation manually  
   - Download the complete discussion as a .txt file  
   - Restart or switch modules anytime

## Tech Stack
- Frontend: Streamlit
- LLM: Google Gemini (gemini-2.5-flash)
- Framework: LangChain
- Environment Management: python-dotenv
- Language: Python

## Prompt Engineering Strategy
The system prompt is dynamically generated based on the selected module and enforces single-domain expertise, zero hallucination outside scope, and clear, concise mentor-style explanations.

This ensures high reliability and controlled AI behavior.

## Features
- Module-restricted AI mentoring
- Clean and intuitive user interface
- Session-based chat history
- Conversation download support
- Topic-violation protection
- Beginner-friendly and professional design

## Use Cases
- Focused self-learning
- Technical interview preparation
- Academic mentoring support
- Structured AI tutoring systems
- AI safety and scope-control demonstrations

## Future Enhancements
- Quiz generation per module
- Progress tracking
- Multi-language support
- Voice-based mentoring
- Authentication and user profiles

## Author
Kishore S  
Aspiring AI Engineer | Data Science | Generative AI Enthusiast
