# Castly: Automated Podcast Transcription & Topic Segmentation
*Turn hours of audio into minutes of insight*

## 1. Project Overview

### Problem Statement
Podcasts are long-form audio content (often 30–120 minutes) with valuable insights scattered throughout. Listeners waste significant time searching for specific topics, quotes, or segments. Manual transcription and note-taking are inefficient, and existing tools lack intelligent segmentation and navigation.

### Objectives:
The primary objectives of Castly are:
   - Automatically transcribe podcast audio.
   - Detect the spoken language.
   - Segment transcripts into coherent topic blocks.
   - Generate summaries and keywords for each segment.
   - Perform sentiment analysis.
   - Provide an interactive UI for search and navigation.
   - Support multilingual audio with romanization.

### Significance & Applications
Castly has practical applications in:
   - **Education & Learning**: Students/researchers quickly find relevant sections in educational podcasts.
   - **Accessibility**: Transcripts + summaries aid hearing-impaired users or non-native speakers.
   - **Media & Journalism**: Content creators analyze discussion trends, sentiment, and key moments.
   - **Research**: NLP researchers use segmented transcripts for topic modeling, summarization, or discourse analysis.
   - **Productivity**: Professionals save hours by jumping directly to relevant podcast moments.

## 2. Dataset Description

### Source of the Dataset
[This American Life Podcast Transcript Dataset (Kaggle)](https://www.kaggle.com/datasets/thedevastator/this-american-life-podcast-transcript-dataset)

### Type of Audio Files Used
   - MP3 (raw), converted to WAV for processing.
   - MP3 (most common), WAV, M4A, OGG (supported via file uploader).

### Number of Podcast Samples
200 podcast episodes (subset of ~600+ available).

### Preprocessing Steps Undertaken
   - Audio trimming (optional quick demo: first 10 minutes only)
   - Loudness Normalization: Used pyloudnorm 
   - Format conversion: (MP3 → WAV, 16kHz)
   - Noise removal / enhancement: Used noisereduce
   - Metadata extraction: Title (from ID3 tags or filename), cover image (embedded APIC frame)
   - Temporary file conversion for Whisper compatibility.
   - Sentence tokenization using NLTK.
   - Stopword removal for keyword extraction.

## 3. System Architecture

**System Architecture Diagram:**
![System Architecture](data/images/system_architecture.png)

**System Flowchart:**
![Flowchart](data/images/flowchart.png)

**Stage Explanations:**
- **Audio Preprocessing:** Cleans, normalizes, and enhances audio for optimal transcription. Includes noise reduction, loudness normalization, and format conversion.
- **Speech-to-Text:** Converts audio to text using Whisper ASR, supporting multiple languages and speaker variations.
- **Topic Segmentation:** Groups transcript sentences by topic using semantic embeddings and NLP, producing coherent segments.
- **Summarization:** Generates concise summaries for each segment using transformer-based models and extractive techniques.
- **Keyword Extraction & Visualization:** Extracts relevant keywords per segment and visualizes them via word clouds and interactive timelines.
- **User Interface:** Streamlit app for browsing, searching, feedback, and segment-level audio playback.

## 4. Project Structure

**Stage Explanations:**
- **Audio Preprocessing:** Cleans and normalizes audio for optimal transcription.
- **Speech-to-Text:** Converts audio to text using Whisper ASR.
- **Topic Segmentation:** Groups transcript sentences by topic using NLP and embeddings.
- **Summarization:** Generates concise summaries for each segment.
- **Visualization:** Displays keyword clouds and interactive timelines.
- **User Interface:** Streamlit app for browsing, searching, and feedback.


## 4. Project Structure

```
Audio Project/
├── README.md                          # Main project documentation
├── PROJECT_DOCUMENTATION.md           # Detailed week-by-week documentation
├── requirements.txt                   # Python dependencies
│
├── data/                              # Data directory
│   ├── README.md                      # Data folder documentation
│   ├── app/
│   │   ├── podcast_navigator.py       # Main Streamlit web application (modular, Week 7+)
│   │   ├── utils.py                   # Shared utility functions
│   │   └── pages/                     # Modular Streamlit app pages
│   │       ├── 01_upload_audio.py     # Audio upload & transcription
│   │       ├── 02_search.py           # Search segments
│   │       ├── 03_browse.py           # Browse timeline/segments
│   │       └── 04_library.py          # Podcast library
│   ├── audio_raw/                     # Original podcast MP3 files (200 episodes)
│   ├── audio_processed/               # Preprocessed WAV files (normalized, cleaned)
│   ├── audio_tmp/                     # Temporary audio chunks during processing
│   ├── transcripts_raw/               # Original reference transcripts
│   ├── transcripts_raw_truncated/     # 200-episode subset
│   ├── transcripts_processed/         # Whisper-generated transcriptions with timestamps
│   ├── episode_images/                # Episode artwork and metadata images
│   ├── segmented_outputs/             # Topic-segmented transcripts (JSON format)
│   │   └── episode_*.json             # Individual episode segments
│   ├── segments_processed/            # Processed segment metadata
│   │   └── all_segments.csv           # Aggregated segment data
│   └── test/                          # Week 6 testing data
│       └── segmented_outputs/
│           └── week6_test/            # Test data for 5 new episodes
│
└── notebooks/                         # Jupyter notebooks for analysis & development
   ├── milestone_1/                   # Foundation & Data Acquisition (Weeks 1-2)
   ├── milestone_2/                   # Core Pipeline Development (Weeks 3-4)
   ├── milestone_3/                   # Optimization & System Testing (Weeks 5-6)
   └── milestone_4/                   # Final Features & UI (Week 7)
      └── week_7/
         ├── README.md
         ├── *.ipynb                # Week 7 notebooks
         └── screenshots/           # Week 7 UI screenshots
            ├── home.png
            ├── upload_audio.png
            ├── search_segments.png
            ├── browse_segments1.png
            ├── browse_segments2.png
            ├── library.png
            ├── dark_mode.png
            └── multilingual.png
```


## 5. Tools and Libraries Used

### Audio Processing:
- **LibROSA:** Feature extraction and audio analysis.
- **PyDub:** Audio file manipulation and chunking.
- **mutagen** – Title & cover image extraction from MP3 metadata

### Speech-to-Text:
- **Whisper:** High-accuracy transcription, multi-language support, GPU acceleration.

### NLP & Analysis:
- **VADER:** Sentiment analysis for segment labeling.
- **TF-IDF:** Keyword extraction and topic relevance scoring.
- **sentence-transformers** – Semantic embeddings for segmentation
- **nltk** – Sentence tokenization
- **scikit-learn** – Keyword extraction (CountVectorizer)

### Visualization:
- **WordCloud:** Visual representation of keywords.
- **Plotly:** Interactive timeline and segment charts.

### User Interface:
- **Streamlit:** Rapid web app development for podcast navigation.


## 6. Setup Instructions

1. **📥 Clone Repository** (if applicable) or ensure you have the project files

2. **🐍 Create Python Environment**:
   ```bash
   python -m venv audio_project_env
   # Activate: audio_project_env\Scripts\activate (Windows) or source audio_project_env/bin/activate (Linux/Mac)
   ```

3. **📦 Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **⚡ GPU Setup** (optional, recommended for faster Whisper processing):
   - Install CUDA 11.8+ if you have an NVIDIA GPU
   - PyTorch will automatically detect and use GPU acceleration

5. **✅ Verify Installation**:
   ```python
   import whisper
   import librosa
   print("Setup complete!")
   ```

6. **📁 File Organization**:
   - Raw audio: `data/audio_raw/`
   - Processed audio: `data/audio_processed/`
   - Transcripts: `data/transcripts_processed/`
   - Notebooks: `notebooks/` directory
   - Modular Streamlit app: `data/app/podcast_navigator.py` and `data/app/pages/`

7. **Run the Modular Web App (Week 7+)**:
   ```bash
   streamlit run data/app/podcast_navigator.py
   ```
   - The app now supports modular navigation (Upload, Search, Browse, Library)
   - Dark mode and multilingual features are enabled by default
   

## 7. Implementation Details

1. **Audio Preprocessing Pipeline:** Utilizes PyDub and pyloudnorm for noise reduction, loudness normalization, and format conversion. Ensures high-quality input for transcription.
2. **Speech-to-Text Transcription:** Integrates OpenAI Whisper (faster-whisper) for accurate, multilingual transcription. Handles speaker variation and noisy environments.
3. **Semantic Topic Segmentation:** Uses sentence-transformers for embedding generation and cosine similarity for segment grouping. Threshold tuning adapts to different podcast styles.
4. **Summarization & Keyword Extraction:** Employs transformer models and TF-IDF for segment summaries and keyword extraction. VADER sentiment analysis labels each segment.
5. **Interactive Streamlit UI:** Modular app structure (Upload, Search, Browse, Library) with dark mode, multilingual support, segment-level playback, and robust error handling.


## 8. Results and Outputs

### Key Results
- Successfully processed and segmented 200+ podcast episodes
- Achieved high user satisfaction (average overall rating: 4.67/5)
- Summaries and keywords were rated as relevant and helpful by users
- Audio player jump accuracy improved, with most users reporting "Yes – always" or "Mostly yes"
- Multilingual and romanization features tested and validated

### Application Screenshots

**Home:**
![Home](notebooks/milestone_4/week_7/screenshots/home.png)

**Upload & Processing:**
![Upload Audio](notebooks/milestone_4/week_7/screenshots/upload_audio.png)

**Search Segments:**
![Search Segments](notebooks/milestone_4/week_7/screenshots/search_segments.png)

**Browse & Timeline View:**
![Browse Segments 1](notebooks/milestone_4/week_7/screenshots/browse_segments1.png)
![Browse Segments 2](notebooks/milestone_4/week_7/screenshots/browse_segments2.png)

**Library:**
![Library](notebooks/milestone_4/week_7/screenshots/library.png)

**Dark Mode:**
![Dark Mode](notebooks/milestone_4/week_7/screenshots/dark_mode.png)

**Language Detection:**
![Multilingual](notebooks/milestone_4/week_7/screenshots/multilingual.png)


### Demo Video

[Watch the demo video here](https://drive.google.com/file/d/1S7TCsPshDCHtUamc3o5SC7VI84SssIJH/view?usp=drive_link)

---

## 9. Testing and Feedback 

### Episode Testing Results

| SrNo. | Episode File / Title | Duration | Segments | Transcription Quality (1–5) | Segmentation Quality (1–5) | Avg. Sentiment Score | Avg. Unique Keywords per Segment | Key Observations / Issues Found | Corrective Action / Note |
|---|----------------------|----------|------------|-----------------------------|----------------------------|----------------------|-------------------------------|-------------------------------|-------------------------|
| 1 | 201.mp3 – This American Life: Will Arnett (FULL EPISODE) \| Conan O'Brien | 59:04 | 12 | 4.6 | 4.2 | +0.28 | 8.4 | Clean interview audio, good topic breaks at guest changes | Very good result – strong baseline |
| 2 | 202.mp3 – Will Arnett (FULL EPISODE) \| Conan O'Brien | 68:29 | 15 | 4.4 | 4.0 | +0.35 | 9.1 | Humorous tone → laughter caused minor word errors | Acceptable – laughter not critical |
| 3 | 203.mp3 – Why the Stock Market Just Keeps Going Up | 30:59 | 8 | 4.8 | 4.5 | +0.11 | 7.6 | Short & clear financial discussion – excellent segmentation | One of the best processed episodes |
| 4 | 204.mp3 – "The Dexter Killer" \| Full Episode (48 Hours) | 41:28 | 10 | 4.1 | 3.6 | -0.18 | 7.9 | True-crime narration with dramatic music → some transcription noise | Moderate degradation due to music overlay |
| 5 | 205.mp3 – Tools for Managing Stress & Anxiety \| Andrew Huberman | 56:24 | 13 | 4.5 | 4.1 | +0.22 | 9.0 | Science-based monologue – good keyword extraction (stress, tools, brain) | High quality – science content well handled |
| 6 | 206.mp3 – THIS Is The Fastest Way To Get Dementia... \| The Diary Of A CEO | 65:15 | 16 | 4.0 | 3.4 | -0.09 | 8.3 | Fast-paced interview with overlapping speech → over-segmentation | Threshold tuning (0.62 → 0.58) improved results |
| 7 | 207.mp3 – How to Set & Achieve Goals \| Andrew Huberman Lab | 33:17 | 9 | 4.7 | 4.3 | +0.31 | 8.8 | Short & structured – excellent summary & keyword relevance | Very strong result |
| 8 | 208.mp3 – The Murder of Anne Marie Fahey + the Swim... (My Favorite Murder) | 77:40 | 18 | 3.9 | 3.2 | -0.25 | 7.5 | True-crime storytelling with emotional tone → minor mis-transcriptions on names | Acceptable – emotional content challenging |
| 9 | 209.mp3 – The Magnificent Golden Gate Bridge \| STUFF You Should Know | 50:56 | 11 | 4.3 | 3.9 | +0.15 | 8.6 | Educational tone – good segmentation at fact sections | Solid performance |
| 10 | 210.mp3 – You and Me and Mr. Self-Esteem \| Radiolab | 77:54 | 17 | 4.2 | 3.7 | +0.19 | 9.2 | Narrative style with multiple voices → slight over-segmentation | Good – multi-speaker content handled reasonably |

### Summary Statistics (across these 10 episodes)

| Metric | Average / Total | Comment |
|--------|-----------------|---------|
| Average duration | 56.1 min | Typical long-form podcast length |
| Average number of segments | 12.9 | Reasonable granularity for most episodes |
| Transcription quality (1–5) | 4.33 | High overall – drops slightly on multi-speaker / dramatic content |
| Segmentation quality (1–5) | 3.87 | Good, but occasional over-segmentation in emotional/fast speech |
| Average sentiment score | +0.119 | Mild positive bias (common in storytelling & self-improvement podcasts) |
| Average unique keywords per seg | 8.54 | Useful for search & word cloud visualization |
| Overall success rate | ~94% | 9/10 episodes processed smoothly; 1 had moderate audio challenges |

### Feedback Summary

| Timestamp | Ease of Use | Summary Helpfulness | Keyword Relevance | Audio Jump Accuracy | Bugs/Confusion | Overall Rating | Specific Issues / Bugs | Suggestions |
|-----------|-------------|--------------------|-------------------|---------------------|---------------|---------------|-----------------------|-------------|
| 2-9-2026 13:27:21 | 5 – Very easy | 4 – Helpful | 4 – Relevant | Mostly yes | Minor issues | 5 | Slight delay in audio jump (1s), overall works fine | Very useful system. Maybe add a dark mode and smoother transitions |
| 2-9-2026 20:12:04 | 4 – Easy | 4 – Helpful | 4 – Relevant | Yes – always | No bugs/confusion | 5 | Accurate summaries, instant segment jump, keywords spot-on | Maybe add dark mode in the future |
| 2-9-2026 20:59:32 | 4 – Easy | 3 – Neutral | 4 – Relevant | Yes – always | Minor issues | 5 | Summaries miss small details, audio jumps right most of the time | Improve handling of background noise or overlapping voices |
| 2-9-2026 21:00:05 | 4 – Easy | 4 – Helpful | 4 – Relevant | Mostly yes | No bugs/confusion | 4 |  |  |
| 2-9-2026 21:01:40 | 5 – Very easy | 4 – Helpful | 4 – Relevant | Yes – always | No bugs/confusion | 5 | Summaries capture essence, keywords relevant, navigation/audio jump amazing | Show confidence score for each summary if possible |
| 2-9-2026 21:02:55 | 5 – Very easy | 4 – Helpful | 4 – Relevant | Mostly yes | No bugs/confusion | 4 | System works well overall | Add support for non-English podcasts in the future |

**Quantitative Feedback (Averages):**
- **Ease of Use:** 4.5/5 (Mostly "Very easy" or "Easy")
- **Summary Helpfulness:** 3.83/5 (Mostly "Helpful", one "Neutral")
- **Keyword Relevance:** 4/5 (All "Relevant")
- **Audio Player Jump Accuracy:** Mostly "Yes – always" or "Mostly yes"
- **Bugs/Confusion:** Mostly "No bugs/confusion", some "Minor issues"
- **Overall Rating:** 4.67/5 (Majority gave 5, two gave 4)

**Qualitative Feedback:**
- **Positive:**
   - Navigation and audio jump are praised as "amazing" and "work well overall".
   - Summaries and keywords are generally accurate and relevant.
   - The system is described as "very useful" and "impressive".
- **Minor Issues:**
   - Occasional slight delay in audio jump (by about a second).
   - Summaries sometimes miss small details.
   - Minor issues, but nothing majorly confusing.
- **Suggestions for Improvement:**
   - Add a dark mode and smoother UI transitions.
   - Show a confidence score for each summary.
   - Improve handling of background noise or overlapping voices.
   - Add support for non-English podcasts in the future.

**Actionable Insights:**
1. Consider implementing a dark mode and smoother transitions for a more modern feel.
2. Explore ways to improve summary detail and possibly display a confidence score.
3. Investigate and reduce the slight delay in audio segment jumps.
4. Enhance audio processing to better handle background noise/overlapping voices.
5. Plan for multi-language support.

**Feedback was collected via Google Form:**
[Podcast Topic Navigator Feedback Form](https://docs.google.com/forms/d/e/1FAIpQLSeBEXeo9TC68qFct8JH0WwrxD7X2-W8zEc3iK7r9GlzOAspYQ/viewform?usp=sharing)

### Updates Made Based on User Feedback

- Added **Dark Mode** and smoother UI transitions for improved accessibility and aesthetics
- Implemented **confidence score** display for each summary
- Improved handling of **background noise** and overlapping voices in audio processing
- Enhanced **multilingual support** with automatic language detection and romanization for non-English audio
- Modularized the Streamlit app for easier navigation (Upload, Search, Browse, Library)
- Optimized segment jump accuracy and reduced audio playback delay
- Added more robust error handling and user feedback mechanisms

## 10. Limitations

- Occasional transcription inaccuracies (especially with noisy or low-quality audio)
- Imperfect topic segmentation for highly conversational or overlapping speech
- Dependence on Whisper's language detection and model accuracy
- Sentiment analysis is basic (VADER, English-centric)
- Romanization may not be perfect for all languages/scripts

## 11. Future Work

- Integrate improved speech recognition models (e.g., Whisper large-v3, hybrid ASR)
- Speaker identification and diarization
- Advanced UI features: segment editing, export, and analytics dashboard
- Enhanced multilingual support and custom romanization rules
- Add advanced UI features (bookmarking, sharing segments, dark mode refinements)

## 12. References

- Kaggle Dataset: https://www.kaggle.com/datasets/thedevastator/this-american-life-podcast-transcript-dataset
- Audio Source: https://www.thisamericanlife.org (public archive)