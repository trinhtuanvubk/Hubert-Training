feat_dir="/home/sangdt/research/voice/hubert/vivos/feat_dir"
split="valid"
nshard=8
km_path="/home/sangdt/research/voice/hubert/vivos/km_dir/train_km.pkl"
lab_dir="/home/sangdt/research/voice/hubert/vivos/lab_dir"

for rank in $(seq 0 $((nshard-1)))
do
    python dump_km_label.py ${feat_dir} ${split} ${km_path} ${nshard} ${rank} ${lab_dir}
done
