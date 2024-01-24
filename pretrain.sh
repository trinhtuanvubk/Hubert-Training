cd fairseq

data_path="/home/sangdt/research/voice/hubert/vivos/tsv_dir"
label_path="/home/sangdt/research/voice/hubert/vivos/lab_dir"
config_path="/home/sangdt/research/voice/hubert/fairseq/examples/hubert/config/pretrain"
config_name="hubert_base_vivos.yaml"
# python fairseq_cli/hydra_train.py --config-dir ${config_path} --config-name ${config_name} task.data=${data_path} task.label_dir= ${label_path} task.labels='["km"]' model.label_rate=100

python fairseq_cli/hydra_train.py --config-dir ${config_path} --config-name ${config_name} task.data=${data_path}