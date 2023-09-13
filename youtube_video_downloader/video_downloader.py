from pathlib import Path
from config import PathConfig
from pytube import YouTube


class VideoDownloader:
	def __init__(self):
		Path(PathConfig.saved_video_folder).mkdir(exist_ok=True)
		self.__out_dir = Path(PathConfig.saved_video_folder)

	def youtube_video_downloader(self, url: str) -> Path:
		yt = YouTube(url)
		video = yt.streams.filter(abr='160kbps').last()
		return Path(video.download(self.__out_dir))
