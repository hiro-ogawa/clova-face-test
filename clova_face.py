import os
import json
import requests
import mimetypes
from pathlib import Path

from requests.models import Response

from dotenv import load_dotenv
load_dotenv(verbose=True)

class ClovaFace(object):
    endpoint = ""
    base_header = {}

    def __init__(self, api_key=None, project_name=None, service_name=None):
        if api_key is None:
            api_key = os.getenv("CLOVA_FACE_API_KEY")
        if project_name is None:
            project_name = os.getenv("CLOVA_FACE_PROJECT_NAME")
        if service_name is None:
            service_name = os.getenv("CLOVA_FACE_SERVICE_NAME")

        self.endpoint = f"https://{project_name}.apigw.jp2.saas.line.me/{service_name}/face/1_1_4/"
        self.base_header = {"x-line-apigw-key": api_key}

    def detection(self, file: Path) -> Response:
        image_binary = file.open("rb").read()
        mimetype = mimetypes.guess_type(file)[0]
        files = {"image": (file.name, image_binary, mimetype)}
        url = f"{self.endpoint}detection"
        headers = self.base_header.copy()
        r = requests.post(url, headers=headers, files=files)
        return r

    def alignment(self, file: Path):
        image_binary = file.open("rb").read()
        mimetype = mimetypes.guess_type(file)[0]
        files = {"image": (file.name, image_binary, mimetype)}
        url = f"{self.endpoint}alignment"
        headers = self.base_header.copy()
        r = requests.post(url, headers=headers, files=files)
        return r
    
    def recognition(self, file: Path):
        image_binary = file.open("rb").read()
        mimetype = mimetypes.guess_type(file)[0]
        files = {"image": (file.name, image_binary, mimetype)}
        url = f"{self.endpoint}recognition"
        headers = self.base_header.copy()
        r = requests.post(url, headers=headers, files=files)
        return r

    def compare(self, file1: Path, file2: Path):
        image1_binary = file1.open("rb").read()
        mimetype1 = mimetypes.guess_type(file1)[0]
        image2_binary = file2.open("rb").read()
        mimetype2 = mimetypes.guess_type(file2)[0]
        files = {
            "image1": (file1.name, image1_binary, mimetype1),
            "image2": (file2.name, image2_binary, mimetype2),
        }
        url = f"{self.endpoint}compare"
        headers = self.base_header.copy()
        r = requests.post(url, headers=headers, files=files)
        return r

if __name__ == "__main__":
    file = Path("sample_images/Lenna.jpg")
    file2 = Path("sample_images/Girl.jpg")
    face = ClovaFace()

    ret = face.detection(file)
    print(ret)
    print(json.dumps(ret.json(), indent=2))

    ret = face.alignment(file)
    print(ret)
    print(json.dumps(ret.json(), indent=2))

    ret = face.recognition(file)
    print(ret)
    print(json.dumps(ret.json(), indent=2))

    ret = face.compare(file, file2)
    print(ret)
    print(json.dumps(ret.json(), indent=2))
