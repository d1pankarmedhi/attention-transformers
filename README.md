<div align="center">
<h1>Attention Transformers</h1>

![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![pytorch](https://img.shields.io/badge/PyTorch-EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)

</div>

Language model train/inference scripts written in Pytorch using a self-attention mechanism for text generation.

This project currently showcases the ability of transformer architecture to generate characters for text generation. To do so, we are using news headlines data for training. 

The final model should be able to generate random news headlines.


### 🏗️ Training Data

```yaml
# data.txt
Natalee Holloway's suspected killer, Joran van der Sloot, admits to crime, says mother
Could Venezuela’s diaspora hold the key to its opposition primary race?
Joran van der Sloot expected to plead guilty to federal charges at Wednesday hearing
Natalee Holloway's mother tells her daughter's killer in court he has caused 'indescribable pain and harm' to her family
WeWork's inevitable retreat is here
Poland introduces border controls with EU neighbor
FBI details how van der Sloot's confession in Natalee Holloway's death came together
He is Ecuador’s youngest president-elect. What lies ahead for Daniel Noboa?
```

## 🏃‍♂️ Getting started

Setup the environment
```bash
# Clone the repository and cd into it.
git clone https://github.com/d1pankarmedhi/attention-transformers.git
cd attention-transformers

# Create and activate a virtual environment 
python -m venv .venv
source .venv/bin/activate # linux
.venv\Scripts\activate # windows

# Install the dependencies
pip install -r requirements.txt
```

### 🚂 Training

View the `params.py` file and make changes as required. Set the **epochs** and **batch_size**.

Make sure the `data.txt` file is present in the root dir. 

```bash
# run the train.py file to start traing
python train.py
```

The **model** should be saved inside `models/model.pt`. Now you can use it for inference.

### 🧗‍♂️ Inference

```bash
# run the `main.py` script for text generation.
python main.py
```

