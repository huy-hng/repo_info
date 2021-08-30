import requests
from fuzzyfinder import fuzzyfinder
from dotenv import load_dotenv

from data_types import Repos, Repo

load_dotenv()

class RepoFinder:
	def __init__(self, username: str, credentials=None):
		self.username = username
		self.credentials = credentials
		self.repos: list[Repo]
		self.update_repos()

	def update_repos(self) -> None:
		url =	f'https://api.github.com/search/repositories?q=user:{self.username}'
		headers = {'Authorization': f'token {self.credentials}'} if self.credentials else {}
		response = requests.get(url, headers=headers)
		data : Repos = response.json()

		if response.status_code != 200:
			raise Exception(data['message'])

		self.repos = data['items']

	def get_repo_names(self):
		return [repo['name'] for repo in self.repos]

	def find_repo(self, name: str) -> list[Repo]:
		# names = self.get_repo_names()
		matches = []
		for repo in self.repos:
			match = list(fuzzyfinder(name, [repo['name']]))
			if len(match) > 0:
				matches.append(repo)
		
		return matches
