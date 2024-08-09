import yt_dlp


def download_any_videos(urls):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': True,
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # Convert to mp4 if needed
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for url in urls:
            try:
                print(f"Downloading from: {url}")
                ydl.download([url])
                print("Download completed")
            except Exception as e:
                print(f"Failed to download from {url}: {e}")


# Example usage
any_urls = input("Enter the Multiple URL's followed with commas: ")
urls = [url.strip() for url in any_urls.split(',')]
download_any_videos(urls)
