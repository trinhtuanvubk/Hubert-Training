tsv_dir="/home/sangdt/research/voice/hubert/vivos/tsv_dir"
split="train"
nshard=8
# rank=1
feat_dir="/home/sangdt/research/voice/hubert/vivos/feat_dir"

for rank in $(seq 0 $((nshard-1)))
do
    python dump_mfcc_feature.py ${tsv_dir} ${split} ${nshard} ${rank} ${feat_dir}
done
