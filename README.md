# Find Text in Repository

In this Python script, it is possible to search several repositories that have a certain word in the owner's github, if found, search if each repository has a certain string.
The results will be saved in a txt file.

### Required parameters:

- `Token`: GitHub access token. You can generate an access token by following the steps outlined [here](https://docs.github.com/en/enterprise-server@3.9/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).
- `repo_has_string`: Search repositories that have a certain string.
- `Owner`: Name of the owner of the repository.
- `find_text`: Search if there is a text in the owner's repository.

### How to use:
1. Replace the parameter values in the `main.py` script with your own.
2. Run the script.