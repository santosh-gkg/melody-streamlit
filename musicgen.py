from gradio_client import Client

client = Client("https://facebook-musicgen.hf.space/")
result = client.predict(
				"Howdy!",	# str  in 'Describe your music' Textbox component
				"https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav",	# str (filepath or URL to file) in 'File' Audio component
				fn_index=0
)
print(result)