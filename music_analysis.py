import os
import google.generativeai as genai
import tkinter as tk
from tkinter import filedialog, scrolledtext
import threading

def analyze_music_gemini(audio_data, file_name):
    """
    Analyzes music using the Gemini model from Google Generative AI.
    
    Args:
        audio_data (bytes): Audio file content in bytes.
        file_name (str): Name of the audio file.
    
    Returns:
        str: Analysis result or error message.
    """
    try:
        # Configure the API client with your API key
        genai.configure(api_key="AIzaSyBtzfntQ8hfcpR6JG7d0xXxQjN1zSdcILw")  # Replace with your actual API key
        
        # Instantiate the model (adjust model name if needed based on availability)
        model = genai.GenerativeModel("gemini-2.0-flash-thinking-exp-01-21")  # Updated to a known model
        
        # Define the prompt for analyzing Indian classical music
        prompt_text = """
        First, briefly describe what you hear in the audio (e.g., instruments, mood).
Then, analyze the musical characteristics of the audio.
Assume this audio is Indian classical music...
        Analyze the musical characteristics of the audio. 
        Assume this audio is Indian classical music.
        Identify and extract the following musical elements:

        - Music Tradition (Hindustani or Carnatic)
        - Raga 
        - Thala 
        - Tempo (e.g., slow, medium, fast, or specific terms like Vilambit, Madhya, Drut)
        - Ornaments (Are ornaments present? YES/NO. If YES, try to name a few prominent ones if possible).
note:- try you best to extract every attribute, and dont give false analysis at all i want accurate and best output and also dont repeat any answers wantedly 
finally try to explore only with only core and fundamental  popular ragas ans thalas which are recognizable if any variation or deviation from original try to mention . 
try to listen upto 20 to 30 times and then conclude at single answer so that it should be same if i uploaded the same audio file again 
and also try to find ornaments in music with accuracy and also mention if corrections in current music so that user can able to know the mistake
        Output the extracted details in the following format:

        -------------------
        EXTRACTED DETAILS

        MUSIC TRADITION :- [Tradition]
        instruments:-
        mood:-
        RAGA :- [Raga Name]
        THALA :- [Thala Name ]
        TEMPO :- [Tempo description ]
        ORNAMENTS :- [YES/NO]
        [If YES, list ornament names: ...]
        Correction:-[if needed]
        -------------
        """
    
        # Determine MIME type based on file extension
        mime_type = "audio/mpeg" if file_name.lower().endswith(".mp3") else "audio/wav"
        
        # Build contents as a list of dictionaries with parts
        contents = [{
            "parts": [
                {"text": prompt_text},
                {"inline_data": {"data": audio_data, "mime_type": mime_type}}
            ]
        }]
        
        # Define generation configuration as a dictionary (fixes the error)
        generate_content_config = {
            "temperature": 0.0,
            "top_p": 0.9,
            "top_k": 32,
            "max_output_tokens": 2048,
        }
        
        # Define safety settings
        safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_NONE",
            }
        ]
        
        # Generate content
        response = model.generate_content(
            contents=contents,
            generation_config=generate_content_config,
            safety_settings=safety_settings
        )
        return response.text

    except Exception as e:
        return f"Error during analysis: {str(e)}"


def open_file_dialog_and_analyze():
    """Opens a file dialog, analyzes the selected audio file, and displays output."""
    file_path = filedialog.askopenfilename(
        title="Select Audio File",
        filetypes=(("Audio files", "*.mp3;*.wav"), ("All files", "*.*")),
    )

    if file_path:
        try:
            with open(file_path, "rb") as audio_file:
                audio_data = audio_file.read()

            output_text_area.config(state=tk.NORMAL)
            output_text_area.delete("1.0", tk.END)
            output_text_area.insert(tk.END, "Analyzing music...\n")
            root.update_idletasks()

            threading.Thread(
                target=perform_analysis_threaded,
                args=(audio_data, os.path.basename(file_path))
            ).start()

        except Exception as e:
            display_analysis_output(f"Error reading audio file: {e}")


def perform_analysis_threaded(audio_data, file_name):
    """Performs analysis in a thread and updates the GUI."""
    analysis_result = analyze_music_gemini(audio_data, file_name)
    display_analysis_output(analysis_result)


def display_analysis_output(analysis_result):
    """Displays the analysis output in the GUI."""
    output_text_area.config(state=tk.NORMAL)
    output_text_area.delete("1.0", tk.END)
    output_text_area.insert(tk.END, analysis_result)
    output_text_area.config(state=tk.DISABLED)


# GUI Setup
root = tk.Tk()
root.title("Music Analysis Tool")

button_select_file = tk.Button(
    root, text="Select Audio File", command=open_file_dialog_and_analyze
)
button_select_file.pack(pady=20)

output_text_area = scrolledtext.ScrolledText(
    root, wrap=tk.WORD, height=20, width=80, state=tk.DISABLED
)
output_text_area.pack(padx=20, pady=20)

if __name__ == "__main__":
    root.mainloop()