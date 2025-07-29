import os
import requests

ENV_PR_NUMBER = 'PR_NUMBER'
ENV_REPO = 'REPO'
ENV_FILES_CHANGED = 'FILES_CHANGED'


def get_pr_files():
    repo = os.getenv(ENV_REPO, '')
    if repo == '':
        exit(1)
    pr_number = os.getenv(ENV_PR_NUMBER, '')
    if pr_number == '':
        exit(1)
    max_per_page = 100
    page_number = 1
    files_in_pr = []
    file_name_field = 'filename'
    status_field = 'status'

    while True:
        api_url = f'https://api.github.com/repos/{repo}/pulls/{pr_number}/files?per_page={max_per_page}&page={page_number}'
        r = requests.get(api_url)
        files = r.json()
        if len(files) == 0:
            break
        for file in files:
            print(f"file in pr: {file[file_name_field]}")
            files_in_pr.append(file[file_name_field])
        page_number += 1

    files_str = ''
    if len(files_in_pr) > 0:
        files_str = ','.join(files_in_pr)
    print(files_str)


if __name__ == '__main__':
    get_pr_files()
