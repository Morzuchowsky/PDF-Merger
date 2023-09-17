import PyPDF4
import re
import subprocess
import os


# Automatically installs the necessary packages from the requirements.txt file.
def install_requirements():
    subprocess.call(["pip", "install", "-r", "requirements.txt"])


# Merge PDF files from the given source directory into a single file.
def merge_pdf_files(source_directory, output_path):
    pdf_file_paths = [
        os.path.join(source_directory, file_name)
        for file_name in os.listdir(source_directory)
        if os.path.isfile(os.path.join(source_directory, file_name))
        and file_name.endswith(".pdf")
    ]

    if not pdf_file_paths:
        print("No PDF files found in the directory.")
        return False

    writer = PyPDF4.PdfFileWriter()
    for pdf_file_path in pdf_file_paths:
        reader = PyPDF4.PdfFileReader(pdf_file_path)
        for page_num in range(reader.numPages):
            writer.addPage(reader.getPage(page_num))

    with open(output_path, "wb") as file:
        writer.write(file)

    return True


# Ensure the file name ends with a .pdf extension.
def add_pdf_extension(file_name):
    if not file_name.endswith(".pdf"):
        return file_name + ".pdf"
    return file_name


# Get the default filename for the merged PDF file.
def get_default_output_filename():
    return "merged_output.pdf"


# Prompt the user for the destination directory and validate its existence.
def get_destination_directory():
    while True:
        destination_directory = input(
            "Enter the path to the directory where you want to save the file (or 'quit' to exit): "
        )
        if destination_directory.lower() == "quit":
            return None
        if os.path.isdir(destination_directory):
            return destination_directory
        else:
            print("Provided path is not a valid directory. Please try again.")


# Prompt the user for the source directory and validate its existence.
def prompt_for_source_directory():
    while True:
        source_directory = input(
            "Enter the path to the directory with PDF files (or 'quit' to exit): "
        )
        if source_directory.lower() == "quit":
            return None
        if os.path.isdir(source_directory):
            return source_directory
        else:
            print("Provided path is not a valid directory. Please try again.")


# Prompt the user for the output filename and ensure its validity.
def get_output_filename():
    while True:
        file_name = input(
            "Enter the name of the output file (Leave empty for default or 'quit' to exit): "
        )
        if file_name.lower() == "quit":
            return None
        if not file_name:
            return get_default_output_filename()
        if is_valid_filename(file_name):
            return add_pdf_extension(file_name)
        print("Invalid filename provided. Please try again.")


# Determine the full path where the merged PDF should be saved, ensuring the filename is unique.
def get_full_output_path(output_filename):
    directory = get_destination_directory()
    if not directory:
        return None

    unique_filename = generate_unique_filename(directory, output_filename)
    return os.path.join(directory, unique_filename)


# Check if the provided filename is valid.
def is_valid_filename(filename):
    if os.name == "nt":
        return not bool(re.search(r'[<>:"/\\|?*]', filename)) and len(filename) <= 255
    else:
        return "/" not in filename and len(filename) <= 255


# Generate a unique filename if a file with the same name already exists in the directory.
def generate_unique_filename(directory, filename):
    base_name, ext = os.path.splitext(filename)
    counter = 1

    while os.path.exists(os.path.join(directory, filename)):
        filename = f"{base_name}{counter}{ext}"
        counter += 1

    return filename


# Orchestrates the PDF merging process based on user input.
def main():
    while True:
        source_directory = prompt_for_source_directory()
        if not source_directory:
            return

        output_filename = get_output_filename()
        if not output_filename:
            return

        output_path = get_full_output_path(output_filename)
        if not output_path:
            return

        result = merge_pdf_files(source_directory, output_path)
        if result:
            print("PDF files have been successfully merged.")


if __name__ == "__main__":
    main()
