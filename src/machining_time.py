from bs4 import BeautifulSoup
import re
import os

def extract_cutting_time(file_path):
    """Extract cutting time from HTML file and return total SECONDS."""
    #TODO make the search iterate thru embedded links in HTML
    
    if not os.path.exists(file_path):
        return 0

    with open(file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    for script in soup(["script", "style"]):
        script.decompose()
    text_content = soup.get_text()

    # patterns for different formats
    patterns = [
        r"Program cutting time:?\s*(\d+)\s*'?\s*(\d+)\s*''",  # 36' 44''
        r"cutting time:?\s*(\d+)\s*min\s*(\d+)\s*sec",        # 36 min 44 sec
        r"cutting time:?\s*(\d+)\s*:\s*(\d+)",                # 36:44
        r"cutting time:?\s*(\d+)\s*minutes?\s*(\d+)\s*seconds?", # 36 minutes 44 seconds
    ]

    for pattern in patterns:
        match = re.search(pattern, text_content, re.IGNORECASE)
        if match:
            minutes = int(match.group(1))
            seconds = int(match.group(2))
            return minutes * 60 + seconds

    return 0  # default if no match found
    #TODO return a valueerror for no match?

