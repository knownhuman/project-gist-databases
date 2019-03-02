import requests

def import_gists_to_database(db, username, commit=True):
    r = requests.get('https://api.github.com/users/{}/gists'.format(username))
    r.raise_for_status()

    query="""
    INSERT INTO gists(
        github_id, html_url, git_pull_url, git_push_url, commits_url, forks_url,
        public, created_at, updated_at, comments, comments_url)
        VALUES
        (:github_id, :html_url, :git_pull_url, :git_push_url, :commits_url,
        :forks_url, :public, :created_at, :updated_at, :comments, :comments_url)
    """

    for i in r.json():
        params = {
        'github_id': i['id'],
        'html_url': i['html_url'],
        'git_pull_url': i['git_pull_url'],
        'git_push_url': i['git_push_url'],
        'commits_url': i['commits_url'],
        'forks_url': i['forks_url'],
        'public': i['public'],
        'created_at': i['created_at'],
        'updated_at': i['updated_at'],
        'comments': i['comments'],
        'comments_url': i['comments_url']
        }

        db.execute(query, params)

    if commit:
        db.commit()
    return
