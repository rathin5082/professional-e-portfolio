import streamlit as st
import subprocess
from search_books import search

st.title("Book Search Engine Dashboard")

# Sidebar for actions
st.sidebar.header("Actions")
action = st.sidebar.selectbox("Select an action", ["Search", "Re-index Data", "Evaluation"])

if action == "Re-index Data":
    st.header("Re-indexing Data")
    st.write("Starting data indexing. This may take a moment...")
    # Run the indexing script (assuming index_books.py is in the same directory)
    result = subprocess.run(["python3", "index_books.py", "books.json"], capture_output=True, text=True)
    # Display the output from the indexing script
    st.code(result.stdout)
    if result.returncode == 0:
        st.success("Indexing complete!")
    else:
        st.error("Indexing encountered an error. Check the logs for details.")

elif action == "Search":
    st.header("Search the Book Index")
    query = st.text_input("Enter your search query:")
    
    if query:
        with st.spinner("Searching..."):
            results = search(query)
        hits = results.get("hits", {}).get("hits", [])
        if hits:
            st.subheader("Search Results")
            for hit in hits:
                source = hit["_source"]
                title       = source.get("Title", "N/A")
                author      = source.get("Author", "N/A")
                publisher   = source.get("Publisher", "N/A")
                timestamp   = source.get("timestamp", "N/A")
                rating      = source.get("Average_Rating", "N/A")
                description = source.get("Description", "N/A")
                book_format = source.get("Format", "N/A")
                score       = hit.get("_score", 0)
                
                st.markdown(f"**Title:** {title}")
                st.markdown(f"**Author:** {author}")
                st.markdown(f"**Publisher:** {publisher}")
                st.markdown(f"**Timestamp:** {timestamp}")
                st.markdown(f"**Rating:** {rating}")
                st.markdown(f"**Description:** {description}")
                st.markdown(f"**Format:** {book_format}")
                st.markdown(f"**Score:** {score:.2f}")
                st.markdown("---")
        else:
            st.warning("No results found for your query.")

elif action == "Evaluation":
    st.header("Evaluation Results")
    # Use a spinner to show the evaluation is running
    with st.spinner("Running evaluation..."):
        result = subprocess.run(["python3", "evaluate.py"], capture_output=True, text=True)
    st.text_area("Evaluation Output", result.stdout, height=400)
    if result.returncode != 0:
        st.error("Evaluation encountered an error. Check the logs for details.")
    else:
        st.success("Evaluation complete!")