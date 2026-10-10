"""
speech_to_text_assemblyAI.py

This script takes an MP3 audio file, transcribes it using AssemblyAI,
splits the text into sentences, and saves the sentences in an Excel file.
"""

import os
import assemblyai as aai
import pandas as pd
import re

def main(mp3_file, output_file="transcribed_data_assemblyAI.xlsx"):
    """
    Transcribe an mp3 audio file using AssemblyAI and save as xlsx.
    """
    # Set your API key
    aai.settings.api_key = os.environ['ASSEMBLYAI_API_KEY']

    #  Create the transcriber object
    transcriber = aai.Transcriber()

    #  Transcribe the audio file (no language_code needed)
    transcript = transcriber.transcribe(mp3_file)

    # Extract text
    text = transcript.text

    # Split text into sentences
    text = re.sub(r'[!?]', '.', text)
    sentences = [s.strip() for s in text.split('.') if s.strip()]

    # Save to xlsx
    df = pd.DataFrame(sentences, columns=["Sentence"])
    df.to_excel(output_file, index=False)

    print(f"Transcription saved to {output_file}")

if __name__ == "__main__":
    main(r"D:\myfile\Y2Block-A\new_file.mp3")
