# Lucky Coincidence

This is "Lucky Coincidence"'s GitHub repository!

# Build the image

docker build -t registry.webis.de/code-research/tira/tira-user-ir-lab-sose-2023-lucky-coincidence/ir-datasets:0.0.1 .

# Run a local jupyter notebook

docker run --rm -ti -w /workspace -v ${PWD}:/workspace registry.webis.de/code-research/tira/tira-user-ir-lab-sose-2023-lucky-coincidence/ir-datasets:0.0.1

# Test the import locally

```
tira-run \
    --output-directory ${PWD}/iranthology-dataset-tira \
    --image registry.webis.de/code-research/tira/tira-user-ir-lab-sose-2023-lucky-coincidence/ir-datasets:0.0.1 \
    --allow-network true \
    --command '/irds_cli.sh --ir_datasets_id iranthology-lucky-coincidence --output_dataset_path $outputDir'
```

# Test retrieval locally

```
tira-run \
    --input-directory ${PWD}/iranthology-dataset-tira \
    --image webis/tira-ir-starter-pyterrier:0.0.2-base \
    --command '/workspace/run-pyterrier-notebook.py --input $inputDataset --output $outputDir --notebook /workspace/full-rank-pipeline.ipynb'
```

# Render created run locally:

```
tira-run \
    --input-directory ${PWD}/tira-output \
    --image registry.webis.de/code-research/tira/tira-user-ir-lab-sose-2023-lucky-coincidence/ir-datasets:0.0.1 \
    --allow-network true \
    --command 'diffir --dataset iranthology-lucky-coincidence --web $outputDir/run.txt > $outputDir/run.html'
```

# Tira command we use:

```
tira-run \
    --output-directory ${PWD}/iranthology-dataset-tira \
    --image lucky-coincidence-qrels \
    --allow-network true \
    --command '/irds_cli.sh --ir_datasets_id iranthology-lucky-coincidence --output_dataset_path $outputDir'
```
