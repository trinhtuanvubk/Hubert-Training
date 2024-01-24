# HUBERT Training

### Data preparation for Hubert
Clone Fairseq (if needed)

```bash
git clone https://github.com/pytorch/fairseq
cd fairseq
pip install --editable ./
```
To prepare data
```bash
cd fairseq/fairseq/examples/hubert/simple_kmeans
```
- 1.Prepare 2 tsv files for train and valid data with format:
```
<root-dir>
<audio-path-1>
<audio-path-2>
...
```

- 2.Run for MFCC feature (for `split="strain"` and  `split=valid`)
```bash
bash mfcc_fea.sh
```

- 3.Train kmeans cluster 1 time
```bash
bash kmeans_cluster.sh
```

- 4.Run trained kmeans to get labels (for `split="strain"` and  `split=valid`)
```bash
bash kmeans_label.sh
```

- 5.Merge to 1 file (for `split="strain"` and  `split=valid`)
```bash
bash merge_lab_dir.sh
```

Follow the steps in `./simple_kmeans` above to create:
- `{train,valid}.tsv` waveform list files
- `{train,valid}.km` frame-aligned pseudo label files.
- `dict.km.txt` a dummy dictionary

The `label_rate` is the same as the feature frame rate used for clustering,
which is 100Hz for MFCC features and 50Hz for HuBERT features by default.

