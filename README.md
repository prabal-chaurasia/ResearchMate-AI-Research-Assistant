# ResearchMate – AI Research Assistant

Enter a topic and ResearchMate searches the web, reads a relevant source, writes a structured research report, and (on request) has a critic model review it.

![ResearchMate UI](docs/ui.png)

## How it works

1. **Search** – Tavily web search returns titles, URLs and snippets.
2. **Read** – the top result is scraped (BeautifulSoup) for deeper content.
3. **Write** – a writer chain (GPT-4o-mini) produces a report: Introduction, Key Findings, Conclusion, Sources.
4. **Critique** – a critic chain scores the report out of 10 with strengths, areas to improve and a one-line verdict.

Two ways to run it:

- `app.py` – Streamlit UI with progress steps, expandable search results / scraped content, and a "Get Critic Feedback" button.
- `pipeline.py` – command-line version of the full multi-agent flow, where a **search agent** and a **reader agent** (built with LangChain `create_agent`) each choose and call their own tool before the writer and critic run.

## Tech stack

Python · LangChain · OpenAI (gpt-4o-mini) · Tavily · BeautifulSoup · Streamlit

## Project structure

```
├── app.py            # Streamlit UI
├── pipeline.py       # CLI multi-agent pipeline
├── agents.py         # Search/reader agents, writer and critic chains
├── tools.py          # web_search (Tavily) and scrape_url tools
├── requirements.txt
└── .env.example
```

## Setup

```bash
git clone https://github.com/prabal-chaurasia/ResearchMate.git
cd ResearchMate
pip install -r requirements.txt
cp .env.example .env      # then add your OPENAI_API_KEY and TAVILY_API_KEY
```

Run the web app:

```bash
streamlit run app.py
```

Or the CLI pipeline:

```bash
python pipeline.py
```

## Author

Prabal Chaurasia · [LinkedIn](https://www.linkedin.com/in/prabal-chaurasia) · [GitHub](https://github.com/prabal-chaurasia)
