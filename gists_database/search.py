from .models import Gist
import datetime

def search_gists(db_connection, **kwargs):
    if not kwargs:
        query = 'SELECT * FROM gists'
    elif 'github_id' in kwargs:
        query = 'SELECT * FROM gists WHERE github_id = :github_id'
    elif 'created_at' in kwargs:
        query = 'SELECT * FROM gists WHERE datetime(created_at) == datetime(:created_at)'

    cursor = db_connection.execute(query, kwargs)
    results = []
    for i in cursor:
        results.append(Gist(i))
    return results
