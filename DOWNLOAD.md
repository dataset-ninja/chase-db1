Dataset **CHASE DB1** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/P/y/r2/2nCV9YLepboiEJA8gO5BDCXGXCPQ9yqAw8i77xg1DtcI6SVXNwgo6dvBTqfQuP6eIAczps6ftCNtTqqOBBiIlkRfGUTr5IYk5OuX9JCgJBXLI6qX7ceAWk3PeyYJ.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='CHASE DB1', dst_path='~/dtools/datasets/CHASE DB1.tar')
```
The data in original format can be 🔗[downloaded here](https://staffnet.kingston.ac.uk/~ku15565/CHASE_DB1/assets/CHASEDB1.zip)