# ds587-Gender-Bias-in-GPT

## Overview

Report link:[]()

This repository contains the code and datasets used in the DS587 final project, which explores gender bias in Generative Pre-trained Transformers (GPT) models. The project aims to understand how different versions of GPT models, including GPT-3.5, GPT-4, and Google Bard, handle gender-related prompts and whether they exhibit any bias.

## Repository Structure

codes/: Essential codes for the project
- evaluation.py: Script for comparing model outputs with expected answers to assess accuracy. 
- gpt.py: Python script for interfacing with GPT models and generating responses to prompts. 
- visualization.ipynb: Jupyter Notebook for visualizing the results and accuracy of different models. 

results/: Results for the project
- model_accuracy_results.csv: Compiled results of model accuracy across different categories. 
- `model type`-results.csv: Misclassification counts of each model.

dataset/: Directory containing various datasets used for evaluating the models. 

## Key Findings

The project evaluates models on their responses to both pro-stereotyped and anti-stereotyped prompts.
A detailed analysis of model accuracy across different categories is presented, highlighting how each model performs in terms of gender bias.

## How to Use

Clone the repository.
Install `requirements.txt`
Run `evaluation.py` to evaluate the models on the datasets.
Use `visualization.ipynb` to generate visualizations of the results.


## Acknowledgments

This project was conducted as part of the DS587 course of Boston University.
Thanks to Prof. Allison McDonald and teaching fellow Bhushan Suwal.