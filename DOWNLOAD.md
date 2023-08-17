Dataset **CHASE DB1** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/k/S/xR/5iPP70dC1pYsy6aEtvWdgsos6H3qLjarsHh6XqozdlbXQfLrr7wywWwWU1yJUBWwehf8ZxdR81o2qfIbOJUHEQtsm0ie6AjrxkQSXllkBNHp5ZJ2j97x5qJF9go6.tar)

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
