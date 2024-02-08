import os
import torch

score_threshold = 0.3
search_k = 5
llm_model = "gpt-4-1106-preview" # gpt-3.5-turbo / gpt-4-1106-preview
user_img = "https://freesvg.org/img/abstract-user-flat-4.png"
bot_img = "https://github.com/ash-hun/WelSSISKo/raw/main/assets/logo02.png"

device = (
    "cuda"
    if torch.cuda.is_available()
    else "mps"
    if torch.backends.mps.is_available()
    else "cpu"
)

EMBEDDING_MODEL_PATH = './model/ko_sroberta_multitask_seed_777_lr_1e-5'
CHROMA_DB_PATH = "./chroma"