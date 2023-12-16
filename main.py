import torch 
from params import Params
from utils import *

device = Params.device

# load model
model = torch.load("models/model.pt", map_location=device)

# text data
text, chars = get_data("data.txt")
mapper = StrIntMapper(chars)


# inference 
context = torch.tensor([mapper.encode("India demands")], dtype=torch.long)
print(mapper.decode(model.generate(context, max_new_tokens=2000)[0].tolist()))