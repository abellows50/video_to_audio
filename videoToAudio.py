from audio_extract import extract_audio

Downloads = "C:/Users/abell/Downloads"

PAIRS = [\
            ["C:/Users/abell/Downloads/Shalosh_Regalim_Maariv.mp4","./Shalosh_Regalim_Maariv.mp3"],\
        ]
def main():
    for pair in PAIRS:
        try:
            extract_audio(input_path=f"{pair[0]}", output_path=f"./data/{pair[1]}")
        except Exception as e:
            print(e)
            print(f"Error processing {pair[0]}")

main()