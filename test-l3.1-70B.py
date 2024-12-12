import openai
import argparse
import json
import re

parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, default=80,
                    help="display a square of a given number")

args = parser.parse_args()
print(f'using port: {args.port}')

#input_file = "./30_questions.json"
#output_file = "./generated_results.json"

# Set OpenAI's API key and API base to use vLLM's API server.
#openai_api_key = "EMPTY"

openai_api_key = "cmsc-35360"
openai_api_base = f"http://195.88.24.64:{args.port}/v1"
print(openai_api_key)
print(openai_api_base)
print("meta-llama/Meta-Llama-3.1-70B-Instruct")
print("")


client = openai.OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)
# instruction_template = """\
# You have the following question and options. Choose the most appropriate option as the final answer. Output only the number of the selected option without any additional explanation.\nQuestion:\n{question}\nOptions:\n{options}\n\nPlease output only the number of the option you think is correct.\n"""

# with open(input_file, 'r', encoding='utf-8') as fin, open(output_file, 'w', encoding='utf-8') as fout:
#     for line in fin:
#         line = line.strip()
#         if not line:
#             continue

#         data = json.loads(line)
#         question = data["question"]
#         options = data["options"]

#         # Format options
#         options_str = "\n".join(f"{i + 1}. {opt}" for i, opt in enumerate(options))

#         # Build the prompt
#         prompt = instruction_template.format(question=question, options=options_str)
#         messages = [{"role": "user", "content": prompt}]

#         # Communicate with the LLM
#         try:
#             chat_response = client.chat.completions.create(
#                 model='meta-llama/Meta-Llama-3.1-70B-Instruct',
#                 messages=messages,
#                 temperature=0.0,
#                 max_tokens=100
#             )
#             response = chat_response.choices[0].message.content.strip()
#             print("Raw response:", response)

#             # Extract the chosen option number
#             match = re.search(r'\b(\d+)\b', response)
#             final_answer = match.group(1) if match else "Invalid Response"

#         except Exception as e:
#             print(f"Error processing question ID {data['id']}: {e}")
#             final_answer = "Error"

#         # Create output data
#         output_data = {
#             "id": data["id"],
#             "answer": final_answer
#         }
#         print(output_data)

#         # Write output data to file
#         fout.write(json.dumps(output_data, ensure_ascii=False) + "\n")

chat_response = client.chat.completions.create(
    model='meta-llama/Meta-Llama-3.1-70B-Instruct',    
    messages=[
        {"role": "user", "content": "你知道为什么海南航空又叫‘半日航’吗？提示：原因和全日航有关"},
    ],
    temperature=0.0,
    max_tokens=2056,
)
response = chat_response.choices[0].message.content
#print("Chat response:", chat_response)
print(response)
with open("output.txt", "w", encoding="utf-8") as file:
    file.write(response)