import requests
import plotly.express as px

#Make api call and check the response.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

#Process results.
response_dict = r.json()
repo_dicts = response_dict['items']

print(f"total repositories: {response_dict['total_count']}")
print(f"complete results: {not response_dict['incomplete_results']}")
print(f"repositories returned: {len(repo_dicts)}")
print("\nSelected information about each repository")
repo_links, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href = '{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)
    '''print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repositories: {repo_dict['html_url']}")
    print(f"description: {repo_dict['description']}")'''

#make visualization.
title = "Most-starred Python projects on github"
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, hover_name=hover_texts)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)

fig.show()


