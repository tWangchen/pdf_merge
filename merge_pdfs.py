from pypdf import PdfWriter


# List the pdfs to merge
INPUT_PDF_LIST = ["1.pdf", "2.pdf"]

# Merged output pdf filename
OUTPUT_PDF = "merged.pdf"

merger = PdfWriter()


def main(input_pdf_list, output_pdf) -> None:
    for pdf in input_pdf_list:
        merger.append(pdf)
    merger.write(f"{OUTPUT_PDF}")
    merger.close()


if __name__ == "__main__":
    main(input_pdf_list=INPUT_PDF_LIST, output_pdf=OUTPUT_PDF)
