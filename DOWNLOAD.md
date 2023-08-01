Dataset **CHASE DB1** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/P/y/r2/2nCV9YLepboiEJA8gO5BDCXGXCPQ9yqAw8i77xg1DtcI6SVXNwgo6dvBTqfQuP6eIAczps6ftCNtTqqOBBiIlkRfGUTr5IYk5OuX9JCgJBXLI6qX7ceAWk3PeyYJ.tar)

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
