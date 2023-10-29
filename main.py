from argparse import ArgumentParser, Namespace
from pytube import YouTube
import os

parser = ArgumentParser()

parser.add_argument('url', help='The url to the youtube video', type=str)
parser.add_argument('-t', '--type', help='Select the format', type=str, choices=['mp3', 'mp4'], default='mp3')

args: Namespace = parser.parse_args()

yt_video = YouTube(args.url)
print("--- Downloading ---")
print(f'Title: {yt_video.title}')
print(f'Format: {args.type}')


if args.type == 'mp3':
    out_path = yt_video.streams.get_audio_only().download()
    new_name = os.path.splitext(out_path)
    os.rename(out_path, new_name[0]+'.mp3')
else:
    out_path = yt_video.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution().download()

print("--- Successfully downloaded! ---")