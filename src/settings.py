from typing import Dict, List, Optional, Union

from dataset_tools.templates import AnnotationType, CVTask, Industry, License

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "CHASE DB1"
PROJECT_NAME_FULL: str = "CHASE DB1"

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.Custom(url="")
INDUSTRIES: List[Industry] = Industry.Medical()
CV_TASKS: List[CVTask] = CVTask.InstanceSegmentation()
ANNOTATION_TYPES: List[AnnotationType] = AnnotationType.InstanceSegmentation()

RELEASE_YEAR: int = 2016
HOMEPAGE_URL: str = "https://blogs.kingston.ac.uk/retinal/chasedb1/"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 884685
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/chase-db1"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[
    Union[str, dict]
] = "https://staffnet.kingston.ac.uk/~ku15565/CHASE_DB1/assets/CHASEDB1.zip"
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = None
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[str] = None
CITATION_URL: Optional[str] = None
ORGANIZATION_NAME: Optional[Union[str, List[str]]] = "Kingston University London"
ORGANIZATION_URL: Optional[Union[str, List[str]]] = "https://www.kingston.ac.uk/"
TAGS: List[str] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    settings = {
        "project_name": PROJECT_NAME,
        "license": LICENSE,
        "industries": INDUSTRIES,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["project_name_full"] = PROJECT_NAME_FULL or PROJECT_NAME
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["citation_url"] = CITATION_URL
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["tags"] = TAGS if TAGS is not None else []

    return settings
