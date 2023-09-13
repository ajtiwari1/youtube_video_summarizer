from pathlib import Path
from config import PathConfig
import whisper_timestamped as whisper
import json


class SpeechToText:
	def __init__(self):
		Path(PathConfig.transcription_folder).mkdir(exist_ok=True)
		self.__transcript_directory = Path(PathConfig.transcription_folder)
		self.model = whisper.load_model("tiny", device="cpu")

	def transcription(self, input_path: Path) -> Path:
		audio = whisper.load_audio(str(input_path))
		result = whisper.transcribe(self.model, audio, language="en")
		text_file = self.__transcript_directory.joinpath(Path(input_path.stem).with_suffix(".txt"))
		with open(str(text_file),"w+") as f:
			f.write(str(result["text"]))
		return text_file
