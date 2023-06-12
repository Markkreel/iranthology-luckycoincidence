import ir_datasets
from ir_datasets.formats import JsonlDocs, TrecXmlQueries, TrecQrels
from typing import NamedTuple, Dict
from ir_datasets.datasets.base import Dataset


class IrAntologyData(NamedTuple):
    doc_id: str
    text: str
    
    def default_text(self):
        return self.text

ir_datasets.registry.register('iranthology-lucky-coincidence', Dataset(
    JsonlDocs(ir_datasets.util.PackageDataFile(path='datasets_in_progress/processed_dataset.jsonl'), doc_cls=IrAntologyData, lang='en'),
    TrecXmlQueries(ir_datasets.util.PackageDataFile(path='datasets_in_progress/topics.xml'), lang='en'),
    TrecQrels(ir_datasets.util.PackageDataFile(path='datasets_in_progress/qrels.txt'), {0:'Not Relevant', 1:'Relevant'})
))
