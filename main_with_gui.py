import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2
import pyttsx3
import os


# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
        return text
    except Exception as e:
        messagebox.showerror("Error", f"Failed to extract text from PDF: {e}")
        return ""


# Function to convert text to speech and save it as an audio file
def convert_text_to_audio(text, output_path):
    try:
        # Initialize the text-to-speech engine
        engine = pyttsx3.init()
        engine.save_to_file(text, output_path)
        engine.runAndWait()
        messagebox.showinfo("Success", f"Audio file saved as {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to convert text to audio: {e}")


# Function to handle file selection and processing
def process_pdf():
    # Ask user to select a PDF file
    pdf_file = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if not pdf_file:
        return

    # Extract text from the selected PDF
    text = extract_text_from_pdf(pdf_file)

    if not text:
        return

    # Ask user to specify the location and name of the output audio file
    audio_file = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
    if not audio_file:
        return

    # Convert the extracted text to audio and save it
    convert_text_to_audio(text, audio_file)


# Create the main application window
def create_gui():
    root = tk.Tk()
    root.title("PDF to Audio Converter")
    root.geometry("400x200")

    # Add a label
    label = tk.Label(root, text="PDF to Audio Converter", font=("Arial", 16))
    label.pack(pady=20)

    # Add a button to process the PDF
    convert_button = tk.Button(root, text="Convert PDF to Audio", width=20, command=process_pdf)
    convert_button.pack(pady=20)

    # Start the GUI
    root.mainloop()


# Run the application
if __name__ == "__main__":
    create_gui()
