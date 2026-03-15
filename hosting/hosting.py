from huggingface_hub import HfApi
import os

api = HfApi(token=os.getenv("HF_TOKEN"))
api.upload_folder(
    folder_path="deployment",  # Corrected path
    repo_id="FREEDOMA1/PIMA-Diabetes-Prediction",    # enter the Hugging Face username here
    repo_type="space",
    path_in_repo="",                          # optional: subfolder path inside the repo
    create_pr=True                            # Add this to explicitly create a Pull Request
)
