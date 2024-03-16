import os


class FileHandler:
    @staticmethod
    def save_results(repo):
        if len(repo):
            folder_path = "Results"
            if not os.path.exists(folder_path):
                os.makedirs("Results")
            with open(f"{folder_path}/Repositories.txt", "w") as file:
                for item in repo:
                    file.write(f"{item}\n")
            return repo
        else:
            print('Empty repository')
            exit()
    
    @staticmethod
    def save_search_results(find_text, result):
        with open(f"Results/{find_text}.txt", "a") as file:
            file.write(f"{result}\n")
