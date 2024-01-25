def video_to_audio(video_name):
    from moviepy.editor import VideoFileClip
    video = VideoFileClip(video_name)
    video.audio.write_audiofile("audio.mp3")
