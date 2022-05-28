from fpdf import FPDF
import sys


class PDF(FPDF):
    def __init__(self, orientation="P", unit="mm", format="A4", font="Arial", font_cache_dir=False) -> None:
        super().__init__(orientation, unit, format)
        self.font = font

    def add_title(self, text: str, centered=False):
        height = 17.9 if centered else 1.5
        self.set_font(self.font, "B", 42)
        self.cell(w=0.5, h=height, align="L", txt=text, ln=1)

    def add_text(self, text: str):
        self.set_font(self.font, "", 28)
        self.cell(w=1, h=2, align='L', ln=1)
        for line in iter(text.splitlines()):
            self.cell(w=1, h=1.9, align='L', txt=line, ln=1)

    def add_image(self, path: str):
        self.image(name=path, h=19)


def main():
    # make sure input and output file are provided
    if len(sys.argv) < 3:
        print("Please enter a valid path for the input and the output file.")
        sys.exit(1)

    # set font family
    font = ""
    if len(sys.argv) == 4:
        match sys.argv[3].lower():
            case "serif":
                font = "Times"
            case "fixed-width":
                font = "Courier"
            case "symbolic":
                font = "Symbol"
            case _:
                font = "Arial"

    # create PDF object
    pdf = PDF(
        orientation="L",
        unit="cm",
        format="A4",
        font=font,
        font_cache_dir=False
    )

    # read file
    content = ""
    with open(sys.argv[1]) as file:
        content = file.read()

    # divide file into pages
    pages = content.split("\n---\n")
    pdf.add_page()  # add first page

    # loop over pages
    for page in pages:
        # images
        if page[0] == "@":
            pdf.add_image(page[1:].strip())
            continue
        # full-page headings
        elif page[0] == "#":
            pdf.add_title(page[1:].strip(), True)
            continue

        # normal headings and text
        pdf.add_page()
        line = page.split("\n")
        pdf.add_title(line[0])
        pdf.add_text("\n".join(line[1:]).strip())

    # save file
    pdf.output(sys.argv[2], "F")


if __name__ == "__main__":
    main()
