

class StrIntMapper:
    def __init__(self, chars):
        self.stoi = { ch:i for i,ch in enumerate(chars) }
        self.itos = { i:ch for i,ch in enumerate(chars) }
        

    def encode(self, string) -> list:
        return [self.stoi[char] for char in string]
    
    def decode(self, array) -> str:
        return "".join([self.itos[i] for i in array])
    

def get_data(file_path: str):
    with open('data.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    chars = sorted(list(set(text)))

    return text , chars

