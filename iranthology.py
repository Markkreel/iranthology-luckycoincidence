import ir_datasets
from ir_datasets.formats import JsonlDocs, TrecXmlQueries, TrecQrels
from typing import NamedTuple, Dict
from ir_datasets.datasets.base import Dataset


class IrAntologyData(NamedTuple):
    doc_id: str
    title: str
    abstract: str
    
    def default_text(self):
        return self.title

ir_datasets.registry.register('iranthology-lucky-coincidence', Dataset(
    JsonlDocs(ir_datasets.util.PackageDataFile(path='datasets_in_progress/ir-anthology-07-11-2021-ss23.jsonl'), doc_cls=IrAntologyData, lang='en'),
    TrecXmlQueries(ir_datasets.util.PackageDataFile(path='datasets_in_progress/topics.xml'))
))
