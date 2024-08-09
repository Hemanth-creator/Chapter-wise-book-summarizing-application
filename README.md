# Chapter wise book summarizing application

## Overview
This repository provides a suite of tools for extracting, processing, and summarizing text from PDF documents. The primary features include:

Extracting text from PDF files
Splitting the extracted text into chapters based on headings
Saving chapters as individual text files
Summarizing each chapter using a text summarization model
Creating a Word document from the summaries

## Usage
### 1. Extract Text from PDF
To extract text from a PDF, use the extract_text_from_pdf(pdf_path) function. The function takes a path to the PDF file and returns the extracted text.

### 2. Split Text by Headings
The split_text_by_headings(text) function processes the extracted text and splits it into chapters based on numeric headings. Each chapter is saved as a separate text file.

### 3. Save Text to File
The save_text_to_file(text, output_path) function saves the entire extracted text to a specified file path.

### 4. Save Chapters to Files
The save_chapters_to_files(chapters, output_dir) function saves each chapter to a separate text file within a specified directory.

### 5. Summarize Chapters
To summarize chapters, use the summarize_chapters_in_folder(folder_path, summaries_folder_path) function. This function reads chapter files from a folder, generates summaries, and saves them to another folder.


### 6. Create Word Document from Summaries
The create_word_document_from_summaries(summaries_folder_path, output_docx_path) function creates a Word document from the summaries. Each summary is added as a paragraph, and chapter titles are used as headings.
