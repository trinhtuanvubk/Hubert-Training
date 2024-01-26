cd fairseq

data_path="/home/sangdt/research/voice/hubert/vivos/tsv_dir"
label_path="/home/sangdt/research/voice/hubert/vivos/lab_dir"
config_path="/home/sangdt/research/voice/hubert/fairseq/examples/hubert/config/finetune"
config_name="base_vivos.yaml"
checkpoint="/home/sangdt/research/voice/hubert/fairseq/Hubert_Checkpoint/checkpoints/checkpoint_best.pt"

python fairseq_cli/hydra_train.py \
--config-dir ${config_path} \
--config-name ${config_name} \