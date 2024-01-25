def transcribe(audio_file, not_english=False):
    import assemblyai as aai
    import os

    if not os.path.exists(audio_file):
        print('Audio file does not exist!')
        return False
    
    
    if not_english: # TRANSLATION 
        with open(audio_file, 'rb') as f:
            print('Starting translating into English...', end='') 
            
            print('Done!')

    
    else: #TRANSCRIPING
        print('Transcribing...', end='')
        aai.settings.api_key = "32417edeb61b4eeabc108e202db37f14"
        transcriber = aai.Transcriber()
        transcript = transcriber.transcribe(audio_file)
        # transcript = transcriber.transcribe("./my-local-audio-file.wav")
        print('Done!')
    
    name, extension = os.path.splitext(audio_file) 
    transcript_filename = f'transcript-{name}.txt'
    
    
    with open(transcript_filename, 'w') as f: 
        f.write(transcript.text)
        return transcript_filename
    