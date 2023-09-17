
# Simple PDF Merger

## Description

This project provides a simple tool to merge multiple PDF files from a given directory into a single output file. The user can specify the source directory containing the PDF files, the name of the output file, and the destination directory to save the merged file.

## Features

- Merge multiple PDFs into one file.
- Ability to specify source and destination directories.
- Provides feedback for invalid input or errors.
- Ensures unique naming for the output file to avoid overwriting.

## Installation

1. Clone this repository:

```bash
git clone https://github.com/Morzuchowsky/PDF-Merger.git
```

2. Navigate to the project directory:

```bash
cd Simple
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

To start the program, execute:

```bash
python main.py
```

Follow the on-screen prompts to merge your PDF files.

## Creating an Executable

If you wish to distribute your application as an executable, follow these steps:

1. Install `pyinstaller`:

```bash
pip install pyinstaller
```

2. Navigate to your script's directory and create the executable:

```bash
pyinstaller --onefile your_script_name.py
```

This will generate a single `.exe` file in the `dist` directory.

3. Share and execute the `.exe` file on any compatible machine. The user doesn't need to have Python installed.

## Dependencies

- PyPDF4
