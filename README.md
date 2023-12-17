<div align="center">
<h1>Attention Transformers</h1>

![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![pytorch](https://img.shields.io/badge/PyTorch-EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)

</div>

Language model train/inference scripts written in Pytorch using a self-attention mechanism for text generation.

## Text Generation with Decoder Model

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

### 🗒️ Sample output

**Training Parameters**:
```yaml
# Trained on a T4 GPU
epochs = 5000
batch_size = 32
n_embd or d_model = 256
parameters = 6.403185 M 

# loss
val_loss = 1.6990
```

**Generate Text**:
```text
Restrictions of volkay may be set to end his finds
Philippine prices earn to Gaza Student and talks with the world
Ball for braces in car car shopping as govt
Formula One to Americans Town Water Tadmil New Paper
India's ready former PM Sunhila 208 2023 ads Arid Lespeed on Humanity
Argentina votes Tesla Eras stripped on half a ban piece
```

Even though the output doesn't make any sense, the fact that the model was able to generate such text which looks similar to news headlines with just 5000 iterations and 6M parameters is extraordinary. 

With some hyperparameter tuning, the accuracy is sure to rise and the model will be able to generate some great results.

<!-- 
### 🌐 Model architecture
![model](https://github.com/d1pankarmedhi/attention-transformers/assets/136924835/eae08797-1888-42c9-93d4-99f95028657c) -->

## 🤝 Acknowledgments

I would like to express my gratitude to the following individuals and projects for inspiration.
- Andrej Karpathy's [nanoGPT](https://github.com/karpathy/nanoGPT)
