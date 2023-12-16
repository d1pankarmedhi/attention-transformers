from model import LanguageModel
from params import Params
from utils import *
import torch 
import os 

device = Params.device
epochs = Params.epochs
block_size = Params.block_size
eval_interval = Params.eval_interval
learning_rate = Params.learning_rate
batch_size = Params.batch_size
eval_iters = Params.eval_iters
split_size = Params.split_size

torch.manual_seed(1337)

# get data
text,chars = get_data("data.txt")
vocab_size = len(chars)

# str int mapper
mapper = StrIntMapper(chars)


# data loading
def get_batch(split:str = "train"):
    data = torch.tensor(mapper.encode(text), dtype=torch.long)
    n = int(split_size*len(data)) 
    train_data = data[:n]
    val_data = data[n:]

    # generate a small batch of data of inputs x and targets y
    data = train_data if split == 'train' else val_data
    ix = torch.randint(len(data) - block_size, (batch_size,))
    x = torch.stack([data[i:i+block_size] for i in ix])
    y = torch.stack([data[i+1:i+block_size+1] for i in ix])
    x, y = x.to(device), y.to(device)
    return x, y


@torch.no_grad()
def estimate_loss(model):
    out = {}
    model.eval()
    for split in ['train', 'val']:
        losses = torch.zeros(eval_iters)
        for k in range(eval_iters):
            X, Y = get_batch(split)
            logits, loss = model(X, Y)
            losses[k] = loss.item()
        out[split] = losses.mean()
    model.train()
    return out

def train():

    

    model = LanguageModel(vocab_size)
    model = model.to(device)
    # number of parameters
    print(f"Model Parameters: {sum(param.numel() for param in model.parameters())/1e6} M")
    # optimizer
    optimizer = torch.optim.AdamW(model.parameters(), lr=learning_rate)

    for epoch in range(epochs):
        if epoch % eval_interval == 0 or epoch == epochs - 1:
            losses = estimate_loss(model)
            print(f"step {epoch}: train loss {losses['train']:.4f}, val loss {losses['val']:.4f}")

        # sample a batch of data
        xb, yb = get_batch('train')

        # evaluate the loss
        logits, loss = model(xb, yb)
        optimizer.zero_grad(set_to_none=True)
        loss.backward()
        optimizer.step()

    # save the model
    os.makedirs("models", exist_ok=True)
    torch.save(model, "models/model.pt")



if __name__ == "__main__":
    train()