import streamlit as st
from tools import web_search, scrape_url
from agents import writer_chain, critic_chain

st.set_page_config(page_title="ResearchMate", page_icon="🔎", layout="wide")
st.title("ResearchMate")
st.write("Enter a topic to search the web and generate a research report.")

topic = st.text_input("Research topic", placeholder="e.g. Latest developments in Agentic AI")

if "report" not in st.session_state:
    st.session_state.report = ""
if "feedback" not in st.session_state:
    st.session_state.feedback = ""
if "search_results" not in st.session_state:
    st.session_state.search_results = ""
if "scraped_content" not in st.session_state:
    st.session_state.scraped_content = ""

if st.button("Run Research", type="primary"):
    if not topic.strip():
        st.warning("Please enter a research topic.")
    else:
        st.session_state.report = ""
        st.session_state.feedback = ""
        progress = st.progress(0)
        status = st.empty()

        try:
            status.write("1/3 Searching the web...")
            search_result = web_search.invoke({"query": topic.strip()})
            st.session_state.search_results = str(search_result)
            progress.progress(35)

            status.write("2/3 Reading a relevant source...")
            # Extract URLs without using the re (regular-expression) module.
            urls = []
            for item in st.session_state.search_results.split():
                candidate = item.strip("\"'(<[{,;>")
                if candidate.startswith(("https://", "http://")):
                    urls.append(candidate.rstrip(".,);]}>\"'"))
            scraped = ""
            if urls:
                # Remove common trailing punctuation from extracted URLs.
                url = urls[0].rstrip(".,);]")
                scraped = scrape_url.invoke({"url": url})
            st.session_state.scraped_content = str(scraped) or "No page content could be extracted."
            progress.progress(60)

            status.write("3/3 Generating your report...")
            report = writer_chain.invoke({
                "topic": topic.strip(),
                "research": (
                    f"SEARCH RESULTS:\n{st.session_state.search_results[:5000]}\n\n"
                    f"SCRAPED CONTENT:\n{st.session_state.scraped_content[:5000]}"
                ),
            })
            st.session_state.report = str(report)
            progress.progress(100)
            status.success("Research report generated!")

        except Exception as e:
            status.empty()
            st.error(f"Something went wrong: {e}")

if st.session_state.report:
    st.subheader("Final Research Report")
    st.markdown(st.session_state.report)

    if st.button("Get Critic Feedback"):
        with st.spinner("Critic is reviewing the report..."):
            try:
                st.session_state.feedback = str(
                    critic_chain.invoke({"report": st.session_state.report})
                )
            except Exception as e:
                st.error(f"Could not generate critic feedback: {e}")

    if st.session_state.feedback:
        st.subheader("Critic Feedback")
        st.markdown(st.session_state.feedback)

    with st.expander("Search Results"):
        st.write(st.session_state.search_results)

    with st.expander("Scraped Content"):
        st.write(st.session_state.scraped_content)
