from pypdf import PdfWriter


# List the pdfs to merge
INPUT_PDF_LIST = ["1.pdf", "2.pdf"]

merger = PdfWriter()


def main(input_pdf_list) -> None:
    for pdf in input_pdf_list:
        merger.append(pdf)
    merger.write("merged.pdf")
    merger.close()


if __name__ == "__main__":
    main(input_pdf_list=INPUT_PDF_LIST)
