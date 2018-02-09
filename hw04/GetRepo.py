import requests
import json


def get_repo_info(user_name='ywang567'):
    output = []
    user_url = 'https://api.github.com/users/{}/repos'.format(user_name)
    res = requests.get(user_url)
    repos = json.loads(res.text)
    output.append('User: {}'.format(user_name))

    if not validate_user_response(repos):
        return 'unable to fetch repos from user'

    try:
        for repo in repos:
            repo_name = repo['name']
            repo_url = 'https://api.github.com/repos/{}/{}/commits'.format(user_name, repo_name)
            repo_info = requests.get(repo_url)
            repo_info_json = json.loads(repo_info.text)
            output.append('Repo: {} Number of commits: {}'.format(repo_name, len(repo_info_json)))
    except TypeError:
        return 'unable to fetch commits from repo'

    return output


def validate_user_response(repos):
    try:
        repos[0]['name']
    except TypeError:
        return False
    return True


if __name__ == '__main__':
    for entry in get_repo_info():
        print(entry)
