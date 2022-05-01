import os
import yaml
from azure.storage.blob import ContainerClient


# reading the configuration file
def load_config():
    dir_root = os.path.dirname(os.path.realpath(__file__))
    print("the dir ", dir_root)
    with open(dir_root + "/config.yaml", "r") as yamlfile:
        return yaml.load(yamlfile, Loader=yaml.FullLoader)


# getting the files from the mentioned directory
def get_files(dir):
    with os.scandir(dir) as entries:
        for entry in entries:
            if entry.is_file() and not entry.name.startswith('.'):
                yield entry


# uploading the relevant frames and the txt files
def upload(files, connection_string, container_name):
    container_client = ContainerClient.from_connection_string(connection_string, container_name)
    print("uploading files in progres...")

    for file in files:
        blob_client = container_client.get_blob_client(file.name)
        with open(file.path, "rb") as data:
            blob_client.upload_blob(data)
            print(f'{file.name} uploaded to blob storage')
            os.remove(file)
            print(f'{file.name} removed from folder')


def main():
    config = load_config()
    dir_root = os.path.dirname(os.path.realpath(__file__))
    full_path = dir_root+"/frames"
    files_to_upload = get_files(full_path)

    upload(files_to_upload, config["azure_storage_connection_string"], config["frame_container_name"])
