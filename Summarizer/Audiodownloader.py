def youtube_audio_downloader (link):
    from pytube import YouTube
    import re
    import os

    if 'youtube.com' not in link:
        print('Invalid YouTube Link!')
        return False
    
    yt = YouTube(link)
    audio = yt.streams.filter(only_audio = True).first()
    
    print('Downloading the audio stream....', end='')
    output_file = audio.download()
    
    
    if os.path.exists(output_file):
        print('Done!')
    else:
        print('Error downloading the file!')
        return False
    
    basename = os.path.basename(output_file)
    name, extension = os.path.splitext(basename)
    
    audio_file = f'{name}.mp3'
    audio_file = re.sub('\s+', '-', audio_file)
    
    os.rename(basename, audio_file)
    
    return audio_file