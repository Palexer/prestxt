# Prestxt

Prestxt is a minimal presentation tool, which creates PDF-slides from a text file.

Inspired by suckless-sent

## Usage

1. Install required packages

`pip install -r requirements.txt`

2. Run the file

`python main.py samples/text.txt samples/out.pdf`

3. Open the output in samples/out.pdf

## ToDo

- add unicode font: ensure available on all systems / write install script
- configuration (slide size, font, dark theme) via command line flags
