import requests

from plotly.graph_objs import  Bar
from plotly import offline

# API呼び出しを作成してそのレスポンスを格納する
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'ステータスコード: {r.status_code}')

# APIレスポンスを変数に格納する
response_dict = r.json()
print(f"全リポジトリ数: {response_dict['total_count']}")

# リポジトリに関する情報を調べる
repo_dicts = response_dict['items']
repo_links, stars, labels = [], [], []
# print(f'情報が返されたリポジトリの数: {len(repo_dicts)}')

# 1つ目のリポジトリを調査する
# repo_dict = repo_dicts[0]
# repo_dict = repo_dicts[0]
# print(f"\nキーの数: {len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
# print(key)
# print("\n各リポジトリの情報の抜粋:")
for repo_dict in repo_dicts:
# print(f"名前: {repo_dict['name']}")
# print(f"所有者: {repo_dict['owner']['login']}")
# print(f"スターの数: {repo_dict['stargazers_count']}")
# print(f"リポジトリURL: {repo_dict['html_url']}")
# print(f"作成日時: {repo_dict['created_at']}")
# print(f"最終更新日時: {repo_dict['updated_at']}")
# print(f"説明文: {repo_dict['description']}\n")
    repo_name = (repo_dict['name'])
    repo_url = (repo_dict['html_url'])
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    repo_url = (repo_dict['html_url'])

    stars.append(repo_dict['stargazers_count'])
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)

# 可視化を実行する
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'GitHubで最も多くのスターがついているPythonプロジェクト',
    'xaxis': {
        'title': 'リポジトリ',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'スターの数',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')

# 結果を処理する
# print(response_dict.keys())