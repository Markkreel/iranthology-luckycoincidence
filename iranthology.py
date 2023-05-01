import ir_datasets
from ir_datasets.formats import JsonlDocs, TrecXmlQueries, TrecQrels
from typing import NamedTuple, Dict
from ir_datasets.util.download import RequestsDownload
from ir_datasets.datasets.base import Dataset
import os
import json

current_dir = os.getcwd()

dataset_path = os.path.join(current_dir, "ir-anthology-07-11-2021-ss23.jsonl")

#with open(dataset_path, "r") as json_file:
#    dataset = json.load(json_file)


class IrAntologyData(NamedTuple):
    id: str
    title: str
    abstract: str
    
    def default_text(self):
        return self.title

ir_datasets.registry.register('pangrams', Dataset(
    JsonlDocs(ir_datasets.util.Download([RequestsDownload(dataset_path + 'ir-anthology-07-11-2021-ss23.jsonl')]), lang='en'),
    TrecXmlQueries(ir_datasets.util.Download([RequestsDownload(dataset_path + 'iranthology.xml')])),
    TrecQrels(ir_datasets.util.Download([RequestsDownload(dataset_path + 'pangram-qrels.txt')]), {0: 'Not Relevant', 1: 'Relevant'})
))