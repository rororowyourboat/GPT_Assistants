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

def main():
    # GitHub repository URL
    repo_url = 'BlockScience/neural-quorum-governance'

    # Directory containing the CADCAD model files
    directory = 'cadCAD/'

    # Fetch files from the GitHub repository
    files_content = fetch_github_files(repo_url, directory)
    print(files_content)

if __name__ == "__main__":
    main()
