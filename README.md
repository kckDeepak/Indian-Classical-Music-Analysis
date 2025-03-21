# Music Analysis using Gemini - Indian Classical Music

## Overview

This project is a collaborative effort by **Chaitanya** and **Yajju Hemanth** to develop a music analysis system using the **Gemini model from Google Generative AI**. The system focuses on accurately analyzing Indian classical music and extracting essential attributes related to **Hindustani and Carnatic traditions**.

## Features

The model will analyze and extract the following attributes:

1. **Music Tradition**: Identify whether the given music belongs to **Hindustani** or **Carnatic** traditions.
2. **Raga Identification**: Recognize the core and fundamental **popular ragas**.
3. **Thala Detection**: Identify the **Thala** used in the composition.
4. **Tempo Analysis**: Categorize the tempo as:
   - Slow (e.g., **Vilambit** in Hindustani, **Chowka** in Carnatic)
   - Medium (e.g., **Madhya** in Hindustani, **Madhyama** in Carnatic)
   - Fast (e.g., **Drut** in Hindustani, **Durita** in Carnatic)
5. **Ornaments (Gamakas and Embellishments)**:
   - Detect whether ornaments (gamakas, meends, etc.) are present (**YES/NO**).
   - If present, list a few prominent ones.
6. **Accuracy & Consistency**:
   - Ensures high accuracy by analyzing the audio **20-30 times** before concluding.
   - Prevents **false or redundant analysis**.
   - Maintains **consistent outputs** for identical input audio files.
7. **Error & Deviation Detection**:
   - Detects any **deviation or variation** from the standard raga or thala.
   - Identifies mistakes in the performance and provides corrective feedback.

## Guidelines for Analysis

- The system will **strictly analyze only core and fundamental ragas and thalas** that are widely recognized.
- If variations exist in the music, they will be noted and flagged.
- The model does **not fabricate results**; only accurate and verifiable insights will be provided.

## Usage Instructions

1. Upload an **audio file** (preferably in **WAV/MP3 format**).
2. The system will process the audio and extract the attributes.
3. If there are mistakes or deviations, they will be highlighted along with corrective suggestions.
4. The output will be **consistent**, ensuring the same results for the same input audio.

## Future Scope

- Improving **ornament detection** accuracy.
- Supporting more **regional classical music styles**.
- Enhancing **tempo precision** with advanced rhythm analysis.

## Contributors

- **Chaitanya**
- **Yajju Hemanth**

## License

This project is licensed under the **MIT License**.
