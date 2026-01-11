![image alt](https://github.com/AymennX/Zenox-AI/blob/main/zenox.png?raw=true)

# ZENOX-CLI v3.0

**ZENOX is a high-performance, terminal-based artificial intelligence interface engineered for Google Gemini models. It provides a low-latency, streamlined environment for interfacing with LLMs directly via the command line.**

---

## Technical Specifications

ZENOX provides a robust architecture for developer-centric AI interaction:

* **Dynamic Model Recovery:** Automatically polls the API to identify and utilize the most capable available model (Gemini 2.5, 3.0, or 1.5-Flash) based on regional availability.
* **Stream Rendering:** Features a real-time word-by-word streaming engine for reduced perceived latency.
* **Context Preservation:** Maintains session state for coherent multi-turn conversations.
* **Rich Markdown Integration:** Renders full Markdown syntax, including code blocks with syntax highlighting, directly in the terminal.
* **Environment Security:** Utilizes `.env` decoupling to ensure API credentials remain secure and separate from version control.

---

## Commands & Usage

ZENOX is optimized for efficiency. Once the neural link is established, use the following protocol:

### Operating the Interface:
1. **Input:** Type your query directly into the `YOU >` prompt.
2. **Execute:** Press `Enter` to transmit the prompt to the Gemini backend.
3. **Interrupt:** Use `Ctrl + C` to stop a live transmission or force an emergency shutdown.

### System Commands:
* **Exit:** Type `exit`, `quit`, or `shutdown` to terminate the session and clear the memory cache.

---

## Requirements

### Prerequisites
* **Python 3.10+**: Ensure Python is correctly mapped to your system's PATH.
* **Gemini API Key**: A valid API key from Google AI Studio is required for authentication.
* **Internet Connection**: A stable connection is necessary for real-time model communication.

---

## Installation Guide

**IMPORTANT:** Make sure you make your own `.env` to put your own Gemini API Key

### 1. Clone the Repository
```bash
git clone https://github.com/AymennX/Zenox-AI.git
cd Zenox-AI
```
### 2. 2. Install Dependencies
````bash
pip install -r requirements.txt
````

### 3. Configure Environment
Create a .env file in the root directory and add your key:
````
GEMINI_API_KEY=your_key_here
````
### 4. Initialization
````Bash
python zenox_main.py
````
---

## Contribution Guidelines
Community contributions are encouraged. Please follow the standard GitHub workflow: fork the repository, create a feature branch, and submit a pull request for technical review. For significant architecture changes, please open a discussion issue first.

## Licensing
This project is distributed under the MIT License. See the LICENSE file for full legal details.
