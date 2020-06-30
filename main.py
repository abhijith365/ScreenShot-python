from pytube import YouTube

link = input("Enter the link: ")

yt = YouTube(link)

# Title of the video
print("Title: ", yt.title)

# Number of views of video
print("Number of views: ", yt.views)

# Length of the video
print("Length of video: ", yt.length)

# Description of video
# print("Description: ", yt.description)
#
#  Rating
# print("Rating: ", yt.rating)
#
#  print the all available streams
# print("Available streams: ", yt.streams)
#
#  audio steams
#  print("Available audio streams: ", yt.streams.filter(only_audio=True))
#
#  video available streams
#  print("Available video streams: ", yt.streams.filter(only_video=True))
#
#  progressive stream (low quality)
# print(yt.streams.filter(progressive=True))
#
#  Dash stream (high)
ys = yt.streams.get_highest_resolution()

# ys.download('location')

# Staring downloading
print("downloading...")

ys.download()

print("Download completed!!")
