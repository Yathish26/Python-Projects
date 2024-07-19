import fitz  # PyMuPDF


def pdf_to_text(pdf_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    text = ""

    # Iterate through each page
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text += page.get_text()

    # Close the PDF file
    pdf_document.close()

    return text


def main():
    pdf_path = "English Notes 1.pdf"  # Replace with your PDF file path
    text = pdf_to_text(pdf_path)

    # Output text to a file with UTF-8 encoding
    with open("output.txt", "w", encoding="utf-8") as text_file:
        text_file.write(text)

    print("Text extraction complete. Check 'output.txt' for the results.")


if __name__ == "__main__":
    main()
