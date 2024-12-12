# Lab 3: Evaluation of Llama Models and Qwen2.5-14B-Instruct

## Overview
This repository contains the code and results for evaluating the performance of three Llama models (Llama 3.1 8B, 70B, and 405B) and Qwen2.5-14B-Instruct on a custom set of challenging questions. The questions include multiple-choice, T/F, and a short-answer problem, designed to test the reasoning, linguistic, and contextual understanding capabilities of the models.

## File Descriptions
- **30_questions.json**: Contains 29 multiple-choice and T/F questions used for evaluation.
- **key.txt**: The answer key for the 29 questions, used to score the models and human responses.
- **compare.ipynb**: Jupyter Notebook used to score and compare the performance of the models and human responses. Includes accuracy calculations and detailed analysis.
- **l3.1-8B.py**: Python script for running evaluations on the Llama 3.1 8B model locally.
- **test-l3.1-70B.py**: Never modified it (provided by the professor).
- **test-l3.1-70B.py**: Python script for running evaluations on the Llama 3.1 70B model (provided by the professor).
- **test-l3.1-405B.py**: Python script for running evaluations on the Llama 3.1 405B model (provided by the professor).
- **qwq.py**: Python script for running evaluations on the Qwen2.5-14B-Instruct model locally using LM Studio.
- **l8b_generated_results.json**: Output file containing the generated responses for the multiple-choice questions by the Llama 3.1 8B model.
- **70B_generated_results.json**: Output file containing the generated responses for the multiple-choice questions by the Llama 3.1 70B model.
- **405B_generated_results.json**: Output file containing the generated responses for the multiple-choice questions by the Llama 3.1 405B model.
- **qwq_generated_results.json**: Output file containing the generated responses for the multiple-choice questions by the Qwen2.5-14B-Instruct model.
- **8b_output.txt**: Output for the short-answer question by the Llama 3.1 8B model.
- **70B_output.txt**: Output for the short-answer question by the Llama 3.1 70B model.
- **405B_output.txt**: Output for the short-answer question by the Llama 3.1 405B model.
- **qwen_output.txt**: Output for the short-answer question by the Qwen2.5-14B-Instruct model.
