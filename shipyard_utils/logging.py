import os

try:
    import files
except BaseException:
    from . import files


def determine_base_artifact_folder(vendor):
    artifact_folder_default = f'{os.environ.get("USER")}-artifacts'
    base_artifact_folder = files.clean_folder_name(
        f'{os.environ.get("SHIPYARD_ARTIFACTS_DIRECTORY",artifact_folder_default)}/{vendor}-blueprints/')
    return base_artifact_folder


def create_artifacts_folders(vendor):
    base_artifact_folder = determine_base_artifact_folder(vendor)
    subfolders = ['artifacts', 'response', 'logs', 'variables']
    for subfolder in subfolders:
        files.create_folder_if_dne(files.clean_folder_name(f'{base_artifact_folder}/{subfolder}')