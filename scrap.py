import os
import tiktoken

# Choose encoding used by the OpenAI model you're interested in
# e.g. "cl100k_base" for GPT-4, GPT-3.5-turbo
encoding = tiktoken.get_encoding("cl100k_base")

# Set the root directory of your repo
REPO_PATH = "C:\\Users\\mmmay\\Downloads\\token"

# File extensions you want to include
VALID_EXTENSIONS = {".py", ".js", ".ts", ".html", ".css", ".md", ".txt", ".json", ".yml", ".yaml", ".cpp", ".c", ".java", ".rs", ".go", ".php"}  # Add or remove as needed

def is_valid_file(filename):
    return os.path.splitext(filename)[1] in VALID_EXTENSIONS

def read_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"⚠️ Skipping file {filepath}: {e}")
        return ""

def count_tokens_in_repo(repo_path):
    total_tokens = 0
    for root, _, files in os.walk(repo_path):
        for file in files:
            if is_valid_file(file):
                filepath = os.path.join(root, file)
                content = read_file(filepath)
                tokens = encoding.encode(content)
                total_tokens += len(tokens)
    return total_tokens

if __name__ == "__main__":
    total = count_tokens_in_repo(REPO_PATH)
    print(f"🔢 Total tokens in repository: {total}")
