# function to split the content of the book into chapter wise
import re

def split_text_by_headings(text):
    chapters = {}
    
    # Regular expression to match a number alone on a line, followed by text on the next line
    heading_pattern = re.compile(r'^(\d+)\s*\n(.*?)(?=\n\d+\s*|\Z)', re.MULTILINE | re.DOTALL)
    for i, match in enumerate(heading_pattern.finditer(text)):
        chapter_number = match.group(1).strip()
        chapter_text = match.group(2).strip()
        
        # Use the chapter number for filename
        chapter_name = f"Chapter_{chapter_number}"
        chapters[chapter_name] = chapter_text
    return chapters