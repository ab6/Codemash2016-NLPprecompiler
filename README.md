#Introduction to NLP using NLTK and Python
Codemash 2016

Amber McKenzie

##Pre-requisite installation

###Windows:

####Install git:
- Download: https://git-scm.com/download/win
- Run the installer, use Git from the Windows Command Prompt
- Open a command prompt, navigate to a working directory
- Run: git clone https://github.com/ab6/Codemash2016-NLPprecompiler.git

####Install Python3:
- Download: https://www.python.org/ftp/python/3.5.1/python-3.5.1.exe
- Run the installer, use the custom installation to set the environment variables and ensure pip is included

###Mac:
- Python Mac Install Documentation: https://docs.python.org/3/using/mac.html

###Install Python Libraries:
- NLTK: Open a console, run: pip install nltk
- NUMPY: Open a console, run: pip install numpy
  - IF NUMPY INSTALL FAILS (Windows Only): 
    - Go to http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy
    - Download numpy+mkl32 (numpy-1.10.2+mkl-cp35-none-win32.whl)
    - Open a console, navigate to the download directory 
    - Run: pip install numpy-1.10.2+mkl-cp35-none-win32.whl
- MATPLOTLIB: Open a console, run: pip install matplotlib

###NLTK requirements:
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
  - words
- Click the Models tab
- Download the following:
  - averaged_perceptron_tagger 
  - maxent_ne_chunker
  - punkt
  

