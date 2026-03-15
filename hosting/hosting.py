from huggingface_hub import HfApi, create_repo
from huggingface_hub.utils import RepositoryNotFoundError, HfHubHTTPError
import os

api = HfApi(token=os.getenv("HF_TOKEN"))
repo_id = "FREEDOMA1/PIMA-Diabetes-Prediction"
repo_type = "space"

try:
    api.repo_info(repo_id=repo_id, repo_type=repo_type)
    print(f"Space '{repo_id}' already exists. Using it.")
except RepositoryNotFoundError:
    print(f"Space '{repo_id}' not found. Creating new space...")
    create_repo(repo_id=repo_id, repo_type=repo_type, private=False)
    print(f"Space '{repo_id}' created.")

api.upload_folder(
    folder_path="deployment",  # Corrected path
    repo_id=repo_id,    # enter the Hugging Face username here
    repo_type=repo_type,
    path_in_repo="",                          # optional: subfolder path inside the repo
    create_pr=True                            # Add this to explicitly create a Pull Request
)
