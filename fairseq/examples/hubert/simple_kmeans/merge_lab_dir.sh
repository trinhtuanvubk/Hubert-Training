feat_dir="/home/sangdt/research/voice/hubert/vivos/feat_dir"
split="train"
nshard=8
km_path="/home/sangdt/research/voice/hubert/vivos/km_dir/train_km.pkl"
lab_dir="/home/sangdt/research/voice/hubert/vivos/lab_dir"


for rank in $(seq 0 $((nshard - 1))); do
  cat $lab_dir/${split}_${rank}_${nshard}.km
done > $lab_dir/${split}.km