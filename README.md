# 🔎 ResearchMate — AI Research Assistant

ResearchMate is a Streamlit app built with LangChain. It takes a research topic, searches the web, reads a relevant source, and writes a structured research report. A critic model can then review the report and score it.

## ✨ Features

- **Web search:** fetches the top 5 results (title, URL and snippet) from the Tavily API
- **Source reading:** scrapes the top result with BeautifulSoup to gather deeper content
- **Report writer:** GPT-4o-mini writes a report with an Introduction, Key Findings, Conclusion and Sources
- **Critic feedback:** on request, a critic scores the report out of 10 with strengths, areas to improve and a one-line verdict
- **Transparent output:** search results and scraped content are available in expandable sections
- **Two ways to run:** a Streamlit web app (`app.py`) and a command-line multi-agent pipeline (`pipeline.py`)

## 🧠 How It Works

```
START ──► search ──► read ──► write ──► END
                                │
                                └──► critic (on request)
```

1. The user enters a research topic in the Streamlit UI and clicks **Run Research**.
2. The `web_search` tool queries Tavily and returns titles, URLs and snippets.
3. The `scrape_url` tool opens the first result and extracts clean page text.
4. The writer chain combines the search results and scraped content into a detailed report.
5. Clicking **Get Critic Feedback** sends the report to the critic chain for a score and review.

`pipeline.py` runs the same flow from the terminal, using a **search agent** and a **reader agent** (built with LangChain `create_agent`) that each decide when to call their tool, followed by the writer and critic.

## 🛠️ Tech Stack

- Python
- LangChain (`langchain`, `langchain-openai`, `langchain-core`)
- OpenAI (gpt-4o-mini)
- Tavily (`tavily-python`) for web search
- BeautifulSoup and requests for scraping
- Streamlit
- python-dotenv

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/prabal-chaurasia/ResearchMate-AI-Research-Assistant.git
cd ResearchMate-AI-Research-Assistant
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set your API keys

The app needs two keys:

- `OPENAI_API_KEY`: https://platform.openai.com/api-keys
- `TAVILY_API_KEY`: https://app.tavily.com/

Create a file named `.env` in the project folder and add:

```
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

### 5. Run the app

```bash
streamlit run app.py
```

Or run the command-line pipeline:

```bash
python pipeline.py
```

## 💡 Example Topics

| Topic | What you get |
|-------|--------------|
| Latest developments in Agentic AI | Report with key findings and sources |
| Impact of electric vehicles on India's economy | Structured report plus critic score |
| How does retrieval-augmented generation work? | Explanatory report from live web sources |

## 📁 Project Structure

```
ResearchMate-AI-Research-Assistant/
├── app.py            # Streamlit UI
├── pipeline.py       # CLI multi-agent pipeline
├── agents.py         # Search/reader agents, writer and critic chains
├── tools.py          # web_search (Tavily) and scrape_url tools
├── requirements.txt
└── README.md
```

## 👤 Author

**Prabal Chaurasia**: [GitHub](https://github.com/prabal-chaurasia) · [LinkedIn](https://www.linkedin.com/in/prabal-chaurasia)
