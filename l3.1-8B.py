import requests
import json
import os
from datetime import datetime
import json
import re

# Define the server URL and endpoint
url = "http://127.0.0.1:1234/v1/completions"

# Define the prompt to identify 20 random human genes and their connections to diseases
input_file = "./30_questions.json"
output_file = "./l8b_generated_results.json"


instruction_template = """\
You have the following question and options. Choose the most appropriate option as the final answer. Output only the number of the selected option without any additional explanation.\nQuestion:\n{question}\nOptions:\n{options}\n\nPlease output only the number of the option you think is correct.\n"""

with open(input_file, 'r', encoding='utf-8') as fin, open(output_file, 'w', encoding='utf-8') as fout:
    for line in fin:
        line = line.strip()
        if not line:
            continue


        data = json.loads(line)
        question = data["question"]
        options = data["options"]

        # Format options
        options_str = "\n".join(f"{i + 1}. {opt}" for i, opt in enumerate(options))
        prompt = instruction_template.format(question=question, options=options_str)
        # Build the prompt
        payload = {
            "prompt": prompt,
            "max_tokens": 100,
            "temperature": 0.0
        }

        # Send a POST request to the LM Studio API        
        # Communicate with the LLM
        try:
            response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(payload))
            result = response.json()
            print("Raw response:", result)

            # Extract the chosen option number
            match = re.search(r'\b(\d+)\b', result['choices'][0]['text'])
            final_answer = match.group(1) if match else "Invalid Response"

        except Exception as e:
            print(f"Error processing question ID {data['id']}: {e}")
            final_answer = "Error"

        # Create output data
        output_data = {
            "id": data["id"],
            "answer": final_answer
        }
        print(output_data)

        # Write output data to file
        fout.write(json.dumps(output_data, ensure_ascii=False) + "\n")

# prompt = """
# 你知道为什么海南航空又叫‘半日航’吗？提示：原因和全日航有关
# """

# # Set up the payload for the API request
# payload = {
#     "prompt": prompt,
#     "max_tokens": 300,  # Adjust this depending on how long a response you want
#     "temperature": 0  # You can adjust the creativity of the model's responses
# }

# # Send a POST request to the LM Studio API
# response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(payload))

# # Check if the response was successful
# if response.status_code == 200:
#     # Print the model's output
#     result = "response.json()"
#     with open("8b_output.txt", "w", encoding="utf-8") as file:
#         file.write(result['choices'][0]['text'])
#     # Print the response
#     print("Response from model:")
#     print(result['choices'][0]['text'])
    
#     print(f"Response saved")
# else:
#     print(f"Error: {response.status_code}")
#     print(response.text)
