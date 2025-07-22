from langchain.llms import HuggingFacePipeline
from langchain_groq import ChatGroq
from transformers import pipeline
import os
import dotenv 

dotenv.load_dotenv()
os.environ["GROQ_API_KEY"] = dotenv.get_key(dotenv.find_dotenv(), "GROQ_API_KEY")
code_pipe = pipeline("text-generation", model="codellama/CodeLlama-7b-Instruct-hf")
code_llm = HuggingFacePipeline(pipeline=code_pipe)

codeproblemstatement_llm = ChatGroq(
    model="deepseek-r1-distill-llama-70b",
    max_tokens=1024,
    temperature=0.7,
    max_retries=3,
    reasoning_format="hidden",

)

def generate_code(prompt: str) -> str:
    response = code_llm(prompt)
    # HuggingFacePipeline typically returns a string directly
    return response if isinstance(response, str) else str(response)

def generate_solution(problem_statement: str) -> str:
    response = codeproblemstatement_llm.invoke(problem_statement)
    return response.content

def code_checker(code: str) -> bool:
    # Placeholder for code checking logic
    # This could involve syntax checks, linting, or running tests
    return True  # Assume the code is valid for this example

def main():
    problem_statement = "explain the concept of recursion in Python with an example"
    solution = generate_solution(problem_statement)
    prompt =f"Write a code in Manim to visualize the the solution for the problem statement:{problem_statement}\n and solution:{solution}"
    code = generate_code(prompt)
    
    # Save the generated code to a new file
    with open("manim_visualization.py", "w") as file:
        file.write(code)
    
    print(f"Generated Manim code has been saved to 'manim_visualization.py'")

if __name__ == "__main__":
    main()



