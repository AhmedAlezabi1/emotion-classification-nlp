# Emotion Classification Pipeline  
**Video → Transcript → Translate → Classify → CSV**

This guide explains how to **run the pipeline end-to-end**. Keep everything (the three scripts, the models, and your video/audio file) **in the same folder as your pipeline notebook** (or adjust paths inside the scripts).

---

## What this pipeline does
1. **Transcribe** your audio/video with AssemblyAI → `transcribed_data_assemblyAI.xlsx`
2. **Translate** EN → NL → EN → `translated_data.xlsx`
3. **Classify** emotions on `Translation_EN` → `final_emotion_output.csv` (+ prints label distribution)

---

## One-time setup
Download this folder and put it in the **same directory as this notebook**:

- **Pipeline Pack (model checkpoints, ~GBs, not included in this repository; available on request)**

It contains:
- RoBERTa-Large emotion classifier checkpoint
- EN→NL translation model
- NL→EN translation model
- requirements.txt

> **All required folders and files (models, scripts, data) must reside in the **same folder as the pipeline notebook** (or update the script paths accordingly).**

---

## Step-by-step usage

### 1. Run the transcription cell
- This cell will ask you to paste the video/audio file path.
- Output file created: transcribed_data_assemblyAI.xlsx
  
### 2. Run the translation cell
- This cell reads the transcription file and generates translated_data.xlsx

### 3. Run the emotion-classification cell
- This cell reads the translated file, classifies emotions, and outputs: final_emotion_output.csv
- It will also print the distribution of predicted emotions.

## Notes

- All required files & model folders must be in the same folder as the notebook
  - RoBERTa_Large_weighted/
  - en_nl/
  - nl_en/
  - requirements.txt/

- Do not change file names unless you also update them in the notebook
