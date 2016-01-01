Introduction to NLP using NLTK and Python
Codemash 2016
Amber McKenzie

Pre-requisite installation

Windows:

Install git:
- Download: https://git-scm.com/download/win
- Run the installer, use Git from the Windows Command Prompt
- Open a command prompt, navigate to a working directory
- Run: git clone https://github.com/ab6/Codemash2016-NLPprecompiler.git

Install Python3:
- Download: https://www.python.org/ftp/python/3.5.1/python-3.5.1.exe
- Run the installer, use the custom installation to set the environment variables and ensure pip is included
- Open a command prompt, run: pip install nltk


NLTK requirements:
- Run: python
- Execute the following in the python prompt
  - import nltk
  - nltk.download()
- When the NLTK Downloader opens, click the Corpora tab
- Download the following: 
  - brown
  - gutenberg
  - state_union
  - stopwords

