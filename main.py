import warnings
from github_api import GitHubAPI
warnings.filterwarnings("ignore")


def main():
    token = "Token_github"
    api = GitHubAPI(token)
    
    repo_has_string = "sns"
    owner = "owner_repository"
    find_text = "boto3"
    query = f'{owner}/{repo_has_string}'
    
    repositories = api.search_repositories(query, owner)
    number_of_repositories = len(repositories)
    
    for index, repo in enumerate(repositories, start=1):
        api.search_code(repo, find_text)
        print(f"Validated {index} out of {number_of_repositories} repositories")


if __name__ == "__main__":
    main()
