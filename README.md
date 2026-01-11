# ZENOX CORE

ZENOX CORE is a high-performance Command-Line Interface (CLI) for interacting with Google's Gemini models. It provides a structured, low-latency environment for developers to interface with Large Language Models (LLMs) directly from the terminal.

## Technical Specifications

- **Engine**: Google Gemini 1.5/2.x/3.x 
- **Interface**: Rich Text Protocol (Python)
- **Configuration**: Environment-based (.env)
- **Features**: Real-time response streaming, dynamic model recovery, and markdown rendering.

## Project Structure

```text
ZENOX-CLI/
├── main.py            # Primary application logic and UI engine
├── .env               # Local configuration (excluded from version control)
├── requirements.txt   # Dependency definitions
└── README.md          # Documentation
