# Search multiple repositories under a single owner that has a specific text

In this Python script, it is possible to search several repositories that have a certain word in the owner's github, if found, search if each repository has a certain string.

The result will save a file with all the repositories found and another file with all the strings found in each repository

As an example, I am searching for all repositories that contain the word `sns` in the owner `aws-samples`, if the repositories are found, it will be searched for which repositories have the text `boto3`.

### Required parameters:

- `Token`: GitHub access token. You can generate an access token by following the steps outlined [here](https://docs.github.com/en/enterprise-server@3.9/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).
- `repo_has_string`: Search repositories that have a certain string.
- `Owner`: Name of the owner of the repository.
- `find_text`: Search if there is a text in the owner's repository.

### How to use:
1. Replace the parameter values in the `main.py` script with your own.
2. Run the script.