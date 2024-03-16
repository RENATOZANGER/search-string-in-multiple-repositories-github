import warnings
from github_api.github_repository_search import GitHubRepositorySearch
from github_api.github_code_search import GitHubCodeSearch
from github_api.file_handler import FileHandler

warnings.filterwarnings("ignore")


def main():
    token = "token_github"
    headers = {"Authorization": f"Bearer {token}"}
    
    repo_has_string = "sns"
    owner = "aws-samples"
    query = f'{owner}/{repo_has_string}'
    
    repo_search = GitHubRepositorySearch()
    repositories = repo_search.search_repositories(query, owner, headers)
    
    code_search = GitHubCodeSearch()
    find_text = "boto3"
    
    for index, repo in enumerate(repositories, start=1):
        code_urls = code_search.search_code(repo, find_text, headers)
        for code_url in code_urls:
            print(f"Text found in the file: {code_url}")
            FileHandler.save_search_results(find_text, code_url)
        print(f"{index} of {len(repositories)} repositories were validated")


if __name__ == "__main__":
    main()
