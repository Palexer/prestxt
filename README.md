# Prestxt

Prestxt is a minimal presentation tool, which creates PDF-slides from a text file.

Inspired by suckless-sent

## Usage

1. Install required packages

`pip install -r requirements.txt`

_Note: The script requires Python 3.10 to run._

2. Run the file

`python main.py samples/text.txt samples/out.pdf`

3. Open the output in samples/out.pdf

---

**Options:**

Enter a font (serif, fixed-width, symbolic) as the third command line argument to change the document wide
font family to something different than the default sans-serif. If the third argument is not given or invalid, the script will fall back to sans-serif.

## ToDo

- add unicode font: ensure available on all systems / write install script
- configuration (slide size, dark theme) via command line flags
