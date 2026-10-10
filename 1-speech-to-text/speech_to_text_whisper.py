import whisper 
import nltk
import pandas as pd

# Make sure punkit is available once 
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)

def main(audio_file: str, outputfile: str = "sentences.csv"):
    """
     Transcribe a MP3 file into a csv using whisperAI where each sentence is seperated
    """
    # load whisper model
    model = whisper.load_model("small").to("cuda")

    # Transcribe
    result = model.transcribe(audio_file)
    transcript = result["text"]

    # Split the transcription into sentences
    sentences = nltk.sent_tokenize(transcript)

    # save to a csv file 
    outputfile = "transcribed_data_whisper.csv"
    df = pd.DataFrame(sentences, columns=["Sentence"])
    df.to_csv(outputfile, index=False, encoding="utf-8")

    print(f"Saved {len(sentences)} sentences → {outputfile}")

if __name__ == "__main__":
    main("Clear Divide  Survivor Aus S04 EP22  Full Episode  Survivor Official.mp3")
