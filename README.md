# Text Diffusion Models with SEDD

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

This repo is based on the [Score Entropy Discrete Diffusion](https://github.com/louaaron/Score-Entropy-Discrete-Diffusion) repository. It contains a PyTorch implementation for the paper [Discrete Diffusion Modeling by Estimating the Ratios of the Data Distribution
](https://arxiv.org/abs/2310.16834) by [Aaron Lou](https://aaronlou.com), [Chenlin Meng](https://cs.stanford.edu/~chenlin/) and [Stefano Ermon](https://cs.stanford.edu/~ermon/).

![cover](assets/language_diffusion_forward.gif)


It has been modified to perform character level diffusion for a few practical reasons.

1) Be able to run on H100 with CUDA 11.8
2) See how well a character level language diffusion model performs.


## Installation

Get the repo
```bash
git clone https://github.com/Chrisz236/Score-Entropy-Discrete-Diffusion.git
cd Score-Entropy-Discrete-Diffusion
```

Create virtual env with conda and install dependencies with pip

```bash
conda env create -f environment.yaml
conda activate oxen
pip install -r requirements.txt
```


## Working with Pretrained Models

### Download Models

You will need setup an free API key from `https://www.oxen.ai/`, export it to environment variable:
```bash
export OXEN_API_KEY="YOUR_API_KEY_HERE"
```

I uploaded the raw PyTorch `SEDD-large` model to Oxen.ai for convenience. To download you can simply run:

```bash
python scripts/pull_model.py
```

This repository contains both the model weights `checkpoint.pth` and the `config.yaml` file with other necessary parameters.


### Run Sampling

We can run sampling using a command 

```bash
python -m scripts.run_sample --model models/SEDD-large/ --steps 128
```

We can also sample conditionally using

```bash
python -m scripts.run_sample_cond.py --model_path MODEL_PATH --step STEPS --prefix PREFIX --suffix SUFFIX
```

## Training New Models

### Run Training

We provide training code, which can be run with the command

```bash
python -m scripts.run_train.py --repo oxen_username/repo_name
```

## Acknowledgements

This repository builds heavily off of [Score Entropy Discrete Diffusion](https://github.com/louaaron/Score-Entropy-Discrete-Diffusion), [score sde](https://github.com/yang-song/score_sde_pytorch), [plaid](https://github.com/igul222/plaid), and [DiT](https://github.com/facebookresearch/DiT).

It was stripped down for demo and learning purposes for [arXiv dives](https://www.oxen.ai/community) series by Oxen.ai.