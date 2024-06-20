# GPT_Assistants
Language model assistants for personal workflows
test
Here's a README for the provided code:

---

# GitHub Repository File Fetcher

Language model assistants for personal workflows

## Description

The script contains a function `fetch_github_files` that takes a GitHub repository URL and a directory path within that repository. It retrieves all files from the specified directory and returns a dictionary where the keys are file paths and the values are the file contents.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone the repository or download the script file.

2. Install the `requests` library if you haven't already:

    ```bash
    pip install requests
    ```

## Usage

1. Update the `repo_url` and `directory` variables with the desired GitHub repository and directory.

    ```python
    # GitHub repository URL
    repo_url = 'BlockScience/neural-quorum-governance'

    # Directory containing the CADCAD model files
    directory = 'nqg_model/'
    ```

2. Run the script:

    ```bash
    python script_name.py
    ```

3. The script will print a dictionary containing the file paths and their contents.

## Example

```python
import requests

def fetch_github_files(repo_url, directory):
    """
    Fetches files from a GitHub repository.

    Args:
        repo_url (str): The URL of the GitHub repository.
        directory (str): The directory containing the CADCAD model files.

    Returns:
        dict: A dictionary mapping file paths to their content.
    """
    base_url = 'https://api.github.com/repos/'
    files_content = {}

    url = f"{base_url}{repo_url}/contents/{directory}"
    headers = {'Accept': 'application/vnd.github.v3.raw'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Parse the response to get the file paths
        files = response.json()

        for file_info in files:
            file_path = file_info['path']
            file_content_url = file_info['download_url']

            # Fetch file content
            file_content_response = requests.get(file_content_url)

            if file_content_response.status_code == 200:
                files_content[file_path] = file_content_response.text
            else:
                print(f"Failed to fetch content of {file_path}: {file_content_response.status_code}")
    else:
        print(f"Failed to fetch directory listing from {url}: {response.status_code}")

    return files_content

# GitHub repository URL
repo_url = 'BlockScience/neural-quorum-governance'

# Directory containing the CADCAD model files
directory = 'nqg_model/'

# Fetch files from the GitHub repository
files_content = fetch_github_files(repo_url, directory)
print(files_content)
```

