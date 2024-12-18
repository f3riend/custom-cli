from yt_dlp import YoutubeDL
import click
import os

resolutions = {
    'l': '144p',
    's': '360p',
    'm': '720p'
}

@click.command()
@click.option(
    '--res', 
    prompt='Enter video resolution (l/s/m)', 
    default='s', 
    type=click.Choice(['l', 's', 'm'], case_sensitive=False), 
    help="Choose video resolution: l (low), s (standard), m (medium)"
)
@click.option(
    '--format', 
    prompt='Choose format (mp3/mp4)', 
    default='mp4', 
    type=click.Choice(['mp3', 'mp4'], case_sensitive=False), 
    help="Select file format: mp3 or mp4 (default: mp4)"
)
def download(res, format):
    try:
        resolution = resolutions[res.lower()]
        fileType = format.lower()

        link = click.prompt('Enter video link')

        playlist = click.prompt('Enter playlist link (optional)', default='', show_default=False)

        if not link.startswith("https://www.youtube.com/watch?v=") and not playlist.startswith("https://www.youtube.com/playlist?"):
            print("Invalid link. Please enter a valid YouTube video or playlist link.")
            return

        otp = {
            'outtmpl': os.path.join(os.path.expanduser('~'), 'Downloads', '%(title)s.%(ext)s'),
            'noplaylist': True if not playlist else False,
        }

        if fileType == 'mp3':
            otp['format'] = 'bestaudio/best'
            otp['postprocessors'] = [{
                'key': 'FFmpegAudioConvertor',
                'preferedformat': 'mp3',
            }]
        elif fileType == 'mp4':
            match res.lower():
                case 'l':
                    otp['format'] = 'bestvideo[height=144]+bestaudio/best[height=144]'
                case 's':
                    otp['format'] = 'bestvideo[height=360]+bestaudio/best[height=360]'
                case 'm':
                    otp['format'] = 'bestvideo[height=720]+bestaudio/best[height=720]'
                case _:
                    print("Invalid resolution. Please choose l, s, or m.")
                    return
        else:
            print("Invalid file type. Please choose mp3 or mp4.")
            return

        video_link = playlist if playlist else link

        with YoutubeDL(otp) as ydl:
            ydl.download([video_link])

    except Exception as e:
        print(f'Something went wrong: {e}')

@click.command()
def snap_text():
    print("Snap Text")

@click.group()
def cli():
    pass

cli.add_command(download)
cli.add_command(snap_text)

if __name__ == "__main__":
    cli()
