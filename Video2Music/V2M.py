import moviepy.editor as mp
def video_to_music(input,output):
    clip = mp.AudioFileClip(input)
    clip.write_audiofile(output)
