Dataset **CHASE DB1** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzExOTVfQ0hBU0UgREIxL2NoYXNlLWRiMS1EYXRhc2V0TmluamEudGFyIiwgInNpZyI6ICJmWVNYeHFxQncvWE5aMFVtQW9KVTVCdG5VZklpQnB0S0NqTUY1TUNDUDBFPSJ9)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='CHASE DB1', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be downloaded here:

- [CHASEDB1.zip](https://researchdata.kingston.ac.uk/96/1/CHASEDB1.zip)
- [readme.txt](https://researchdata.kingston.ac.uk/96/2/readme.txt)
