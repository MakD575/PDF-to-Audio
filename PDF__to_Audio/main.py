import PyPDF2
from gtts import gTTS

def pdf_to_audio(pdf_path, audio_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''

            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + '\n'
                else:
                    print("No text found on one of the pages.")

            if not text.strip():
                print("No extractable text found in the PDF.")
                return

            tts = gTTS(text=text, lang='en')
            tts.save(audio_path)
            print(f"Audio saved to {audio_path}")

    except FileNotFoundError:
        print("The specified PDF file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    pdf_path = 'sample.pdf'  # Replace with your PDF file path
    audio_path = 'output.mp3'  # Desired output audio file path
    pdf_to_audio(pdf_path, audio_path)
