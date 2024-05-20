import os
import yt_dlp as youtube_dl

# Ensure 'downloaded songs' directory exists
download_folder = "Downloaded Songs"
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

def download_audio(url, quality='best'):
    ydl_opts = {
        'format': f'bestaudio/{quality}',
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'progress_hooks': [progress_hook]
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        print(f"Downloaded audio: {url}")

def download_playlist(playlist_url, quality='best'):
    ydl_opts = {
        'format': f'bestaudio/{quality}',
        'outtmpl': os.path.join(download_folder, '%(playlist_title)s', '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'progress_hooks': [progress_hook]
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])
        print(f"Downloaded playlist: {playlist_url}")

def progress_hook(d):
    if d['status'] == 'downloading':
        print(f"Downloading: {d['filename']} - {d['_percent_str']} complete")
    elif d['status'] == 'finished':
        print(f"Finished downloading: {d['filename']}")

def main():
    print("")
    print("====================================================================================================================")
    print("""
███╗░░░███╗██████╗░██████╗░  ██████╗░░█████╗░░██╗░░░░░░░██╗███╗░░██╗██╗░░░░░░█████╗░░█████╗░██████╗░███████╗██████╗░
████╗░████║██╔══██╗╚════██╗  ██╔══██╗██╔══██╗░██║░░██╗░░██║████╗░██║██║░░░░░██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██╔████╔██║██████╔╝░█████╔╝  ██║░░██║██║░░██║░╚██╗████╗██╔╝██╔██╗██║██║░░░░░██║░░██║███████║██║░░██║█████╗░░██████╔╝
██║╚██╔╝██║██╔═══╝░░╚═══██╗  ██║░░██║██║░░██║░░████╔═████║░██║╚████║██║░░░░░██║░░██║██╔══██║██║░░██║██╔══╝░░██╔══██╗
██║░╚═╝░██║██║░░░░░██████╔╝  ██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░██║░╚███║███████╗╚█████╔╝██║░░██║██████╔╝███████╗██║░░██║
╚═╝░░░░░╚═╝╚═╝░░░░░╚═════╝░  ╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░╚══╝╚══════╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝

███████╗░█████╗░██████╗░  ██████╗░░░░░░██╗██╗░██████╗
██╔════╝██╔══██╗██╔══██╗  ██╔══██╗░░░░░██║╚█║██╔════╝
█████╗░░██║░░██║██████╔╝  ██║░░██║░░░░░██║░╚╝╚█████╗░
██╔══╝░░██║░░██║██╔══██╗  ██║░░██║██╗░░██║░░░░╚═══██╗
██║░░░░░╚█████╔╝██║░░██║  ██████╔╝╚█████╔╝░░░██████╔╝
╚═╝░░░░░░╚════╝░╚═╝░░╚═╝  ╚═════╝░░╚════╝░░░░╚═════╝░
""")
    print("====================================================================================================================")
    print("https://github.com/merttcetn \n")

    song_links_file = 'links.txt'
    
    # Check if the file exists and is not empty
    if not os.path.isfile(song_links_file) or os.path.getsize(song_links_file) == 0:
        print(f"The file '{song_links_file}' is empty or does not exist.")
        return
    
    with open(song_links_file, 'r') as file:
        links = file.readlines()

    if not links:
        print(f"No links found in '{song_links_file}'.")
        return

    while True:
        # Prompt user to select audio quality
        print("Enter preferred audio quality")
        quality = input("(e.g., best, 128k, 192k): ")

        # Check if quality is valid
        if quality.lower() in ['best', 'worst', '128k', '192k', '256k', '320k']:
            break
        else:
            print("Invalid audio quality. Please enter a valid quality.")

    for link in links:
        link = link.strip()
        if link:
            if 'youtube.com/playlist' in link:
                download_playlist(link, quality)
            elif 'youtube.com' in link or 'youtu.be' in link or 'soundcloud.com' in link:
                download_audio(link, quality)
            else:
                print(f"Unsupported link: {link}")
        else:
            print("Skipping empty line in the file.")

if __name__ == "__main__":
    main()
