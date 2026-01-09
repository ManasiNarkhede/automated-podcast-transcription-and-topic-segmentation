# Automated Podcast Transcription and Topic Segmentation

**AI-powered system for transcribing long-form podcast audio and automatically segmenting it into topical sections**

## Project Overview

The goal of this project is to develop an AI-powered system that automatically transcribes podcast audio recordings and segments them into distinct topical sections.  

Leveraging advances in speech-to-text technology (ASR) and natural language processing (NLP), the system enables users to navigate podcasts efficiently by browsing topics, key discussion points, and compact summaries without listening to the entire episode.

### Key Outcomes

- Understand speech recognition techniques for converting audio to text

- Implement NLP methods to identify topic changes and segment transcripts

- Build an end-to-end pipeline: audio ingestion → preprocessing → transcription → segmentation → indexing

- Visualize segment boundaries, extract keywords, and generate compact summaries for each topic

- Prepare comprehensive documentation and final presentation describing methodology, challenges, and user benefits

### Model Architecture

```
Podcast Audio
      ↓
User Interface (Web App) ──→ Backend REST API
      ↓
Audio Preprocessing & Speech-to-Text Model (Whisper)
      ↓
Topic Segmentation & Summarization (NLP)
      ↓
Segmented Transcript & Topics
      ↓
User Interface (Navigation, Search, Visualization)
```

## Dataset

**Chosen Dataset:**  

**This American Life Podcast Transcript Dataset** (Kaggle)  

- Link: https://www.kaggle.com/datasets/thedevastator/this-american-life-podcast-transcript-dataset  

- ~600+ episodes  

- High-quality aligned transcripts with timestamps and speaker information  

- **Matching audio files** legally downloaded from the official archive: https://www.thisamericanlife.org/archive

**Current working subset:** 200 episodes (transcripts + downloaded MP3 audio)

## Project Milestones & Timeline (8 Weeks)

| Milestone | Weeks       | Notebooks Folder                        | Main Deliverables                                      |
|-----------|-------------|-----------------------------------------|--------------------------------------------------------|
| 1         | 1–2         | `week1_milestone/`                     | Dataset acquisition, exploration, audio preprocessing |
| 2         | 3–4         | `week2_milestone/` & `week3_milestone/` | Initial transcription (Whisper), topic segmentation algorithms |
| 3         | 5–6         | `week4_milestone/` & `week5_milestone/` | Keyword extraction, summarization, visualizations     |
| 4         | 7–8         | `week7-8_milestone/`                   | UI development (Streamlit), documentation, presentation|

## Technologies Used

- **Environment**: Google Colab (GPU runtime recommended for Whisper)

- **Audio Processing**: librosa, pydub, soundfile, pyloudnorm

- **Speech-to-Text**: OpenAI Whisper (base/small/medium models)

- **NLP & Segmentation**: pandas, scikit-learn, spaCy, sentence-transformers

- **Visualization & UI**: matplotlib, plotly, Streamlit (planned)

- **Python Version**: 3.10+

## Setup Instructions (Colab)

1. **Open Google Colab** → Create new notebook

2. **Mount Google Drive** (recommended – to store audio & processed files)

   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```

3. **Install dependencies** (run in first cell):

   ```bash
   !pip install -q pydub librosa soundfile pyloudnorm openai-whisper torch torchaudio pandas tqdm scikit-learn spacy sentence-transformers streamlit
   !python -m spacy download en_core_web_sm
   ```

4. **Change runtime type** → GPU (T4 or better if available)

5. **Place files in Drive**:

   - Raw MP3s: `/content/drive/MyDrive/podcast-project/data/audio_raw`

   - Transcripts: `/content/drive/MyDrive/podcast-project/data/transcripts_processed`

   - Processed audio: `/content/drive/MyDrive/podcast-project/data/audio_processed/`

## Project Structure

```
podcast-project/
├── README.md
├── requirements.txt
├── data/
│   ├── README.md
│   ├── audio_processed/          (Preprocessed audio files)
│   ├── audio_raw/                (Original podcast MP3s)
│   ├── audio_tmp/                (Temporary audio processing files)
│   ├── transcripts_processed/
│   │   ├── episode_1_whisper.json
│   │   ├── episode_2_whisper.json
│   │   └── ... (30 episodes)
│   ├── transcripts_raw/
│   │   ├── episode_info_clean.csv
│   │   └── lines_clean.csv
│   └── transcripts_raw_truncated/
│       ├── episode_info_clean_200.csv
│       └── lines_clean_200.csv
└── notebooks/
    └── milestone_1/
        ├── week_1/
        │   ├── project_init_and_dataset_acquisition.ipynb
        │   └── README.md
        └── week_2/
            ├── audio_preprocessing_and_speech_to_text.ipynb
            ├── transcript_quality_evaluation.ipynb
            └── README.md
```

## Current Status 

- Dataset acquired: 200 episodes (transcripts + audio)

- Environment setup completed in Colab (GPU)

- Week 1 & Week 2 notebooks updated (exploration & preprocessing)

- Whisper transcription tested on subset

## Future Work

- Automate full pipeline

- Advanced segmentation (BERT embeddings + speaker cues + TextTiling)

- Streamlit web interface for interactive navigation & search

- Comprehensive evaluation (Word Error Rate, segmentation precision/recall)

- Final presentation & documentation

## References

- Kaggle Dataset: https://www.kaggle.com/datasets/thedevastator/this-american-life-podcast-transcript-dataset

- Audio Source: https://www.thisamericanlife.org (public archive)

