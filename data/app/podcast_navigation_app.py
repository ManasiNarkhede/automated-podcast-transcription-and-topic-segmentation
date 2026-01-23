
# ─────────────────────────────────────────────────────────────────────────────
# IMPORTS
# ─────────────────────────────────────────────────────────────────────────────
import streamlit as st
import json
import os
import pandas as pd

# ─────────────────────────────────────────────────────────────────────────────
# PAGE CONFIGURATION
# ─────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Podcast Topic Navigator",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────────────────────────────────────────
# PATHS
# ─────────────────────────────────────────────────────────────────────────────
BASE_PATH   = "/content/drive/MyDrive/podcast-project"
SEGMENT_DIR = f"{BASE_PATH}/data/segmented_outputs"
AUDIO_DIR   = f"{BASE_PATH}/data/audio_raw"

# ─────────────────────────────────────────────────────────────────────────────
# LOAD DATA
# ─────────────────────────────────────────────────────────────────────────────
# Cache the function so data loads faster on reruns
@st.cache_data
def load_all_segments():
    rows = []

    # Loop through all segment JSON files
    for file in os.listdir(SEGMENT_DIR):
        if file.endswith("_segment.json"):
            with open(os.path.join(SEGMENT_DIR, file), "r", encoding="utf-8") as f:
                ep = json.load(f)
                ep_id = ep["episode_id"]

                # Extract each segment from the episode
                for seg in ep["segments"]:
                    rows.append({
                        "episode_id": ep_id,
                        "segment_id": seg["segment_id"],
                        "summary": seg["summary"],
                        "keywords": ", ".join(seg.get("keywords", [])),
                        "text_preview": seg["text_preview"],
                        "start_time_sec": seg.get("start_time_sec", 0.0),
                        "num_sentences": seg["num_sentences"]
                    })
    return pd.DataFrame(rows)   # Convert list of rows into a DataFrame

# Load data and replace missing values with empty strings
df = load_all_segments().fillna("")

# ─────────────────────────────────────────────────────────────────────────────
# SORT EPISODES & SEGMENTS NUMERICALLY
# ─────────────────────────────────────────────────────────────────────────────
# Extract episode number from episode_id
df["episode_number"] = df["episode_id"].str.extract(r"(\d+)").astype(int)

# Extract segment number from segment_id
df["segment_number"] = df["segment_id"].astype(str).str.extract(r"(\d+)").astype(int)

# Sort episodes first, then segments
df = df.sort_values(["episode_number", "segment_number"])

# ─────────────────────────────────────────────────────────────────────────────
# HELPER FUNCTION: HIGHLIGHT KEYWORDS
# ─────────────────────────────────────────────────────────────────────────────
# Make keywords bold inside the transcript preview
def highlight_keywords(text, keywords):
    for kw in keywords.split(","):
        kw = kw.strip()
        if kw:
            text = text.replace(kw, f"**{kw}**")
    return text

# ─────────────────────────────────────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────────────────────────────────────
st.sidebar.title("🎧 Podcast Navigator")
st.sidebar.markdown(
    """
    **Topic Navigation UI**

    Navigate podcast content efficiently:
    - Search topics globally  
    - Browse episodes sequentially  
    - Jump to relevant segments  
    """
)

st.sidebar.divider()

# Mode selector
mode = st.sidebar.radio(
    "Navigation Mode",
    ["🔍 Search Topics", "📂 Browse Episodes"]
)

# Episode list (used in browse mode)
episode_list = (
    df[["episode_id", "episode_number"]]
    .drop_duplicates()
    .sort_values("episode_number")
    ["episode_id"]
    .tolist()
)

# ─────────────────────────────────────────────────────────────────────────────
# MAIN HEADER
# ─────────────────────────────────────────────────────────────────────────────
st.markdown(
    """
    # 🎙️ Podcast Topic Navigator  
    Explore podcast episodes by **topic segments** without scrolling
    through long transcripts.
    """
)

st.divider()

# ─────────────────────────────────────────────────────────────────────────────
# 🔍 SEARCH MODE
# ─────────────────────────────────────────────────────────────────────────────
if mode == "🔍 Search Topics":
    # Input box for search query
    search_query = st.text_input(
        "Search by keyword or summary (across all episodes)",
        placeholder="e.g. intro, background, discussion, summary"
    )

    if search_query:
        # Filter segments that match the search text
        df_search = df[
            df["summary"].str.contains(search_query, case=False, na=False) |
            df["keywords"].str.contains(search_query, case=False, na=False)
        ]

        st.subheader(f"Search Results ({len(df_search)} segments)")

        if df_search.empty:
            st.info("No matching segments found. Try a different keyword.")
        else:
            # Show each matching segment
            for _, row in df_search.iterrows():
                with st.expander(
                    f"Episode {row.episode_number} | "
                    f"Segment {row.segment_number} — {row.summary[:70]}..."
                ):
                    st.markdown("### 📝 Summary")
                    st.write(row.summary)

                    st.markdown("### 🏷️ Keywords")
                    st.write(row.keywords)

                    st.markdown("### 📄 Transcript")
                    st.markdown(
                        highlight_keywords(row.text_preview, row.keywords)
                    )

                    # Show progress within the episode
                    st.progress(
                        row.segment_number /
                        df[df["episode_id"] == row.episode_id]["segment_number"].max()
                    )

                    st.caption(
                        f"Episode {row.episode_number} • "
                        f"Segment {row.segment_number} • "
                        f"{row.num_sentences} sentences • "
                        f"Start {row.start_time_sec:.1f}s"
                    )

                    # Play audio if file exists
                    audio_path = os.path.join(
                        AUDIO_DIR, f"{row.episode_number}.mp3"
                    )
                    if os.path.exists(audio_path):
                        st.audio(audio_path)

# ─────────────────────────────────────────────────────────────────────────────
# 📂 BROWSE MODE
# ─────────────────────────────────────────────────────────────────────────────
else:
    selected_episode = st.sidebar.selectbox(
        "Select Episode",
        episode_list
    )

    df_ep = df[df["episode_id"] == selected_episode]

    st.subheader(f"Episode {df_ep.iloc[0].episode_number}")

    # Segment selector
    segment_map = {
        f"Segment {row.segment_number}: {row.summary[:70]}": row
        for _, row in df_ep.iterrows()
    }

    selected_segment_label = st.selectbox(
        "Select Topic Segment",
        list(segment_map.keys())
    )

    row = segment_map[selected_segment_label]

    st.markdown(
        f"""
        ## 🎯 Selected Segment  
        **Episode {row.episode_number} – Segment {row.segment_number}**
        """
    )

    col1, col2 = st.columns([3, 1])   # Layout: main content and info panel

    with col1:
        st.markdown("### 📝 Summary")
        st.write(row.summary)

        st.markdown("### 🏷️ Keywords")
        st.write(row.keywords)

        st.markdown("### 📄 Transcript")
        st.markdown(
            highlight_keywords(row.text_preview, row.keywords)
        )

        st.progress(
            row.segment_number /
            df_ep["segment_number"].max()
        )

    with col2:
        st.markdown("### ℹ️ Info")
        st.caption(f"Sentences: {row.num_sentences}")
        st.caption(f"Start time: {row.start_time_sec:.1f}s")

        audio_path = os.path.join(
            AUDIO_DIR, f"{row.episode_number}.mp3"
        )
        if os.path.exists(audio_path):
            st.audio(audio_path)

# ─────────────────────────────────────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────────────────────────────────────
st.divider()
st.caption(
    "Podcast Topic Navigation • Built with Streamlit • © Manasi Narkhede "
)
