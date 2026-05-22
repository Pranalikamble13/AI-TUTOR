# AI-TUTOR 🤖📚

AI-TUTOR is an AI-powered educational assistant designed to help users learn topics interactively. It can generate structured syllabi, provide tutoring support, and assist with guided learning using AI-based responses.

## Features

- 📖 AI-powered teaching assistant
- 📝 Automatic syllabus generation
- 💬 Interactive learning support
- ⚡ Fast responses using OpenRouter API
- 🧠 Personalized topic guidance
- 🔐 Secure API key handling using `.env`

## Tech Stack

- Python
- OpenRouter API
- Gradio
- Git & GitHub
- Environment Variables (`python-dotenv`)

## Project Structure

```bash
AI-TUTOR/
│── App.py
│── generating_syllabus.py
│── teaching_agent.py
│── run.py
│── .gitignore
│── README.md
```

## Installation & Setup

### 1. Clone Repository
```bash
git clone https://github.com/Pranalikamble13/AI-TUTOR.git
cd AI-TUTOR
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

Activate environment (Windows):
```bash
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Create `.env` File
Add your OpenRouter API key:

```env
OPENROUTER_API_KEY=your_api_key_here
```

### 5. Run Project
```bash
python run.py
```

## Use Cases

- AI-assisted tutoring
- Topic explanation and learning guidance
- Study planning and syllabus creation
- Self-learning support

## Security

This project uses `.env` for secure API key storage. Sensitive credentials are not pushed to GitHub.

## Future Improvements

- Multi-subject support
- Better UI enhancements
- Student progress tracking
- Quiz generation
- Personalized recommendations

## Author

**Pranali Kamble**

