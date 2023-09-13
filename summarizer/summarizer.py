from transformers import pipeline
from config import PathConfig
from pathlib import Path


class Summarizer:
	def __init__(self):
		self.__out_path = None
		Path(PathConfig.summarization_folder).mkdir(exist_ok=True)
		self._out_dir=Path(PathConfig.summarization_folder)
		self.__model=pipeline("summarization", model="facebook/bart-large-cnn")

	def chunk_and_summarize(self,text, chunk_size=500):
		chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
		summaries = [self.__model(chunk, max_length=130, min_length=30, do_sample=False) for chunk in chunks]
		return " ".join([summary[0]['summary_text'] for summary in summaries])
	def summarization(self,input_path:Path)->Path:
		self.__out_path=self._out_dir.joinpath(input_path.name)
		with open(str(input_path),"r+") as f:
			article=f.read()
		summary=self.chunk_and_summarize(article)

		with open(str(self.__out_path),"w+") as f:
			f.write(summary)
		return self.__out_path



