feat_dir="/home/sangdt/research/voice/hubert/vivos/feat_dir"
split="train"
nshard=8
km_path="/home/sangdt/research/voice/hubert/vivos/km"
n_cluster=100

python learn_kmeans.py ${feat_dir} ${split} ${nshard}  ${km_path} ${n_cluster} --percent 1