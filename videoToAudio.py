from audio_extract import extract_audio

Downloads = "C:/Users/abell/Downloads"

PAIRS = [\
            [f"{Downloads}/testVid.mp4", "odecha.mp3"],\
            [f"{Downloads}/RPReplay_Final1713113401.mp4","Adonai_Zecharanu_Yivarech.mp3"],\
            [f"{Downloads}/RPReplay_Final1713113595.mp4","Betzeit_Yisroel.mp3"],\
        ]
def main():
    for pair in PAIRS:
        try:
            extract_audio(input_path=f"{pair[0]}", output_path=f"./data/{pair[1]}")
        except Exception as e:
            print(e)
            print(f"Error processing {pair[0]}")

main()