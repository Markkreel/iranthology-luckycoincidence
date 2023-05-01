import unittest
import ir_datasets
from ir_datasets.formats import JsonlDocs, TrecXmlQueries, TrecQrels
from ir_datasets.util.download import MemoryCache
from ir_datasets.datasets.base import Dataset
from typing import NamedTuple, Dict

class TestIrAnthology(unittest.TestCase):

    def setUp(self):
        # Create a memory cache for the dataset downloads
        self.cache = MemoryCache()
        
        # Download and load the IR Anthology JSONL file
        dataset_url = "https://github.com/georgetownir/ir-datasets/releases/download/v0.3.1/ir-anthology-07-11-2021-ss23.jsonl.gz"
        download = ir_datasets.util.Download([ir_datasets.util.GzipDownload(ir_datasets.util.HttpDownload(dataset_url))])
        self.docs = JsonlDocs(download, lang='en')

        # Download and load the IR Anthology TREC queries
        queries_url = "https://github.com/georgetownir/ir-datasets/releases/download/v0.3.1/iranthology.xml.gz"
        download = ir_datasets.util.Download([ir_datasets.util.GzipDownload(ir_datasets.util.HttpDownload(queries_url))])
        self.queries = TrecXmlQueries(download, lang='en')
        
        # Download and load the IR Anthology TREC qrels
        qrels_url = "https://github.com/georgetownir/ir-datasets/releases/download/v0.3.1/ir-anthology.qrels.gz"
        download = ir_datasets.util.Download([ir_datasets.util.GzipDownload(ir_datasets.util.HttpDownload(qrels_url))])
        self.qrels = TrecQrels(download, {0: 'Not Relevant', 1: 'Relevant'})

        # Register the dataset with ir_datasets
        ir_datasets.registry.register('ir_anthology', Dataset(self.docs, self.queries, self.qrels))
        
    def test_dataset(self):
        # Iterate over the documents and make sure they have the expected fields
        for doc in self.docs:
            self.assertIn('id', doc)
            self.assertIn('title', doc)
            self.assertIn('abstract', doc)
            self.assertIn('letters', doc)
            
        # Iterate over the queries and make sure they have the expected fields
        for query in self.queries:
            self.assertIn('id', query)
            self.assertIn('text', query)
            
        # Iterate over the qrels and make sure they have the expected format
        for qid, doc, label in self.qrels:
            self.assertIsInstance(qid, str)
            self.assertIsInstance(doc, str)
            self.assertIsInstance(label, int)
            self.assertIn(label, [0, 1])
            
if __name__ == '__main__':
    unittest.main()
