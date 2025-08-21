from langchain_ollama import ChatOllama

# Initialize the AI model
llm = ChatOllama(model="gemma3:270m")

# Get user information
print("=== AI Assistant Setup ===")
user_name = input("What's your name? ")
topic = input("What do you want to learn about? ")
experience = input("Are you a beginner, intermediate, or advanced learner? ")

# Clean up the inputs using string methods
user_name = user_name.strip().title()
topic = topic.strip().lower()
experience = experience.strip().lower()

# Create a personalized prompt using f-strings
prompt = f"""Hello! I'm helping {user_name} learn about {topic}.
{user_name} is a {experience} level learner.
Please explain {topic} in a way that's perfect for a {experience} learner.
Use simple language and include practical examples.
Keep your response under 200 words."""

print(f"Sending your question to AI...")
print(f"Topic: {topic}")
print(f"Your level: {experience}")

# Send to AI and get response
response = llm.invoke(prompt)
ai_output = response.content

# Process the AI response
response_length = len(ai_output)
word_count = len(ai_output.split())