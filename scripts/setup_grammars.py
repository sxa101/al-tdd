import os
import subprocess
from tree_sitter import Language

# Languages to set up
LANGUAGES = {
    "python": "https://github.com/tree-sitter/tree-sitter-python",
    "javascript": "https://github.com/tree-sitter/tree-sitter-javascript",
    "rust": "https://github.com/tree-sitter/tree-sitter-rust",
}

GRAMMAR_DIR = "grammars"
BUILD_LIB_PATH = os.path.join("build", "languages.so")

def setup_grammars():
    """
    Clones grammar repositories and builds a shared library for all of them.
    """
    if not os.path.exists(GRAMMAR_DIR):
        os.makedirs(GRAMMAR_DIR)

    if not os.path.exists("build"):
        os.makedirs("build")

    grammar_repos = []
    for lang, url in LANGUAGES.items():
        repo_path = os.path.join(GRAMMAR_DIR, f"tree-sitter-{lang}")
        if not os.path.exists(repo_path):
            print(f"Cloning {lang} grammar from {url}...")
            try:
                subprocess.run(["git", "clone", url, repo_path], check=True)
                grammar_repos.append(repo_path)
            except (subprocess.CalledProcessError, FileNotFoundError) as e:
                print(f"Error cloning {lang} grammar. Make sure git is installed and in your PATH.")
                print(e)
                return
        else:
            print(f"Grammar for {lang} already exists at {repo_path}.")
            grammar_repos.append(repo_path)


    print("Building shared library for grammars...")
    if not hasattr(Language, 'build_library'):
        print("Error: The installed version of the 'tree-sitter' library appears to be missing the 'build_library' method.")
        print("Please try upgrading the library: pip install --upgrade tree-sitter")
        return

    try:
        Language.build_library(
            # Create a .so on Linux/macOS or .dll on Windows
            BUILD_LIB_PATH,
            # Include one directory for each grammar
            grammar_repos
        )
        print(f"Successfully built library at {BUILD_LIB_PATH}")
    except Exception as e:
        print(f"Error building grammars library: {e}")
        print("\nThis can happen if you don't have a C/C++ compiler installed and in your PATH.")
        print("For Windows, you may need to install the 'Build Tools for Visual Studio'.")
        print("For macOS, you may need to install the Xcode Command Line Tools.")
        print("For Linux, you may need to install the 'build-essential' package (or equivalent).")

if __name__ == "__main__":
    setup_grammars()
