# TruthSeek AI — Universal Question Answering Agent

TruthSeek AI is an AI-powered question-answering agent designed to answer questions across multiple topics, search the web for relevant evidence, provide source links, and perform mathematical calculations.

## Features

- **AI-powered answers:** Uses the Groq API to generate responses.
- **Web research:** Uses Tavily to retrieve relevant online sources.
- **Evidence-based responses:** Includes source URLs and communicates uncertainty when claims are not independently verified.
- **Safe calculator:** Supports basic arithmetic calculations without executing arbitrary Python code.
- **LangGraph workflow:** Routes questions through different agent steps and tools.
- **FastAPI backend:** Provides REST API endpoints for asking questions and conducting research.
- **Flutter Android app:** Includes a mobile chat interface for interacting with the agent.

## Technology Stack

- Python
- FastAPI
- LangGraph
- Groq API
- Tavily Search API
- Flutter and Dart

## Project Structure

```text
TruthSeek_AI/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── schemas.py
│   │   ├── tools.py
│   │   ├── agent.py
│   │   └── main.py
│   ├── tests/
│   ├── requirements.txt
│   ├── .env.example
│   └── .gitignore
├── flutter_app/
│   ├── lib/
│   ├── test/
│   └── pubspec.yaml
├── .gitignore
└── README.md
```

## Prerequisites

- Python 3.10 or a compatible version supported by the dependencies.
- A Groq API key.
- A Tavily API key.
- Flutter SDK for Android app development.

## Backend Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/truthseek-ai.git
cd truthseek-ai/backend
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file inside the `backend` directory using `.env.example` as a template.

Configure the following variables:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
APP_API_KEY=your_private_api_key
```

Never commit real API keys or secrets to GitHub.

### 5. Start the backend

Run this command from the `backend` directory:

```powershell
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 6. Test the API

Health check:

http://127.0.0.1:8000/health

Interactive API documentation:

http://127.0.0.1:8000/docs

Available endpoints include `/health`, `/ask`, and `/research`.

Requests to protected endpoints must include the correct `X-API-Key` header.

## Flutter Android App

The Flutter application is located in the `flutter_app` directory.

Install Flutter dependencies:

```powershell
flutter pub get
```

If Android platform files have not been generated, run:

```powershell
flutter create --platforms=android .
```

Run the app on a connected Android device or emulator:

```powershell
flutter run
```

Configure the app to use your deployed backend URL and the required API key.

## Deployment

The FastAPI backend can be deployed to a compatible hosting platform such as Render.

Configure the backend directory as the service root, install dependencies from `requirements.txt`, and use the following start command:

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

Add API keys as environment variables in the hosting dashboard. Do not upload the `.env` file.

## Verification and Limitations

TruthSeek AI can retrieve web sources and produce evidence-backed answers. However, retrieved sources do not automatically prove every individual claim. The agent should communicate uncertainty when evidence is insufficient.

The project should be tested in the target deployment environment before production use.

## License

Choose an appropriate open-source license before distributing this project publicly.
