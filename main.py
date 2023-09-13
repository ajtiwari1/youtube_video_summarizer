from youtube_video_downloader import VideoDownloader
from speech_to_text import SpeechToText
from summarizer import Summarizer
from pathlib import Path
import warnings
import streamlit as st
import time


warnings.filterwarnings("ignore")







# if __name__ == "__main__":
# 	video_downloader = VideoDownloader()
# 	speech_to_txt = SpeechToText()
# 	downloaded_path = video_downloader.youtube_video_downloader(url="https://www.youtube.com/watch?v=h5id4erwD4s")
# 	transcript_path = speech_to_txt.transcription(Path(downloaded_path))
# 	summary = Summarizer()
# 	summary_path = summary.summarization(transcript_path)
# 	print(summary_path)
if __name__ == "__main__":
	st.title("YouTube Video Summarizer 🎥")
	st.markdown('<style>h1{color: orange; text-align: center;}</style>', unsafe_allow_html=True)
	st.subheader('Built with the Wishper, Streamlit and ❤️')
	st.markdown('<style>h3{color: pink;  text-align: center;}</style>', unsafe_allow_html=True)
	with st.expander("About the App"):
		st.write("This app allows you to summarize while watching a YouTube video.")
		st.write(
			"Enter a YouTube URL in the input box below and click 'Submit' to start.")

	youtube_url = st.text_input("Enter YouTube URL")
	if st.button("Submit") and youtube_url:
		start_time = time.time()
		video_downloader = VideoDownloader()
		speech_to_txt = SpeechToText()
		summary = Summarizer()

		downloaded_path = video_downloader.youtube_video_downloader(url=youtube_url)
		transcript_path = speech_to_txt.transcription(Path(downloaded_path))
		summary_path = summary.summarization(transcript_path)
		end_time = time.time()  # End the timer
		elapsed_time = end_time - start_time

		col1, col2 = st.columns([1, 1])

		# Column 1: Video view
		with col1:
			st.video(youtube_url)

		# Column 2: Summary View
		with col2:
			st.header("Transcription of YouTube Video")
			with open(str(transcript_path),"r+") as f:
				transcript_out=f.read()
			with open(str(summary_path),"r+") as f:
				summary_out=f.read()

			st.write(transcript_out)
			st.header("Summarization of YouTube Video")
			st.success(summary_out)
			st.write(f"Time taken: {elapsed_time:.2f} seconds")






