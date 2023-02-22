
from langchain.llms import OpenAI

name = "Andrei"
age = 31
print("My name is {} and I am {} years old.".format(name, age))

llm = OpenAI(temperature=0.9)

text = "What would be a good company name a company that makes colorful socks?"
print(llm(text))

