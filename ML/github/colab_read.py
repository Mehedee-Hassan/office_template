    import json, requests, urllib, io

    user='my_github_username'
    pao='my_pao'

    github_session = requests.Session()
    github_session.auth = (user, pao)

    # providing raw url to download csv from github
    csv_url = 'https://raw.githubusercontent.com/user/repo/master/csv_name.csv'

    download = github_session.get(url_swing).content
    downloaded_csv = pandas.read_csv(io.StringIO(download.decode('utf-8')), error_bad_lines=False)
