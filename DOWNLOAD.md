Dataset **CHASE DB1** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogInMzOi8vc3VwZXJ2aXNlbHktZGF0YXNldHMvMTE5NV9DSEFTRSBEQjEvY2hhc2UtZGIxLURhdGFzZXROaW5qYS50YXIiLCAic2lnIjogIkN3MlZzY09nZGEvTVhoVFNKZWpIVWI3VGhxbXAzdnlyTmo3MkZJdDhEVGc9In0=?response-content-disposition=attachment%3B%20filename%3D%22chase-db1-DatasetNinja.tar%22)

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
