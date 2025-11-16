import ollama

# Initialize the Ollama client
client = ollama.Client()

# Define the model and the input prompt
model = "llama3.1"  # Replace with your model name
prompt = "Give me some interesting functions of Pyspark that truly makes " \
"the work easier while handling data. Give the output in points along with their use"

# Send the query to the model
response = client.generate(model=model, prompt=prompt,stream =True)

# Print the response from the model
print("Response from Ollama:")
print(response.response)