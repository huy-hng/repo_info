import os

from get_repos import RepoFinder

if __name__ == '__main__':
	repository = RepoFinder('huy-hng', os.environ['GITHUB_TOKEN'])
	# repository = RepoFinder('huy-hng')
	
	matches = repository.find_repo('spot')
	for match in matches:
		print(match['name'], match['html_url'])
	# repos = repository.get_repo_names()
	# for repo in repos:
	# 	print(repo)

	