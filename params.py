import torch 

class Params:
    batch_size = 16 
    block_size = 32 
    epochs = 1000
    eval_interval = 200
    learning_rate = 1e-3
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    eval_iters = 200
    n_embd = 64
    n_head = 4
    n_layer = 4
    dropout = 0.0
    split_size = 0.9

