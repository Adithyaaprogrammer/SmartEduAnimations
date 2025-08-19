from langchain_groq import ChatGroq
import os
import dotenv 
os.environ["GROQ_API_KEY"] = dotenv.get_key(".env", "GROQ_API_KEY") 
code_llm = ChatGroq(
    model="moonshotai/kimi-k2-instruct",
    max_tokens=3000,
    temperature=0.5,
)

codeproblemstatement_llm = ChatGroq(
    model="qwen/qwen3-32b",
    max_tokens=3000,
    temperature=0.5,
    max_retries=3,
    # reasoning_format="hidden",

)

def generate_code(prompt: str) -> str:
    response = code_llm.invoke(prompt)
    # HuggingFacePipeline typically returns a string directly
    return response.content

def generate_solution(problem_statement: str) -> str:
    response = codeproblemstatement_llm.invoke(problem_statement)
    return response.content

def code_checker(code: str) -> bool:
    # Placeholder for code checking logic
    # This could involve syntax checks, linting, or running tests
    return True  # Assume the code is valid for this example

def main():
    standard_prompt = "Please explain the above concept in a clear and detailed manner and Make the explanation beginner-friendly while ensuring technical depth. Include an example that illustrates the concept effectively."
    input = "explain the cauchy riemann equation proof"
    problem_statement = input + standard_prompt
    solution = generate_solution(problem_statement)
    print(f"Generated solution: {solution}")
    prompt =f"""Generate only complete Manim code in Python that visually presents and solves the following problem. Do **not** include any explanation—only the full, runnable Manim code. Your animation should:
1. Clearly state the problem at the top of the screen.
2. Step through each part of the solution using manim codable/generatable diagrams, graphs, geometric shapes, or annotations.
3. Use transforms, highlights, and manim generatable label animations to guide the viewer’s attention.
4. Conclude with a final summary frame that displays the answer visually.
 
Problem Statement:
{problem_statement}

Solution Outline:
{solution}
"""
    code = generate_code(prompt)

    # Save the generated code to a new file
    with open("manim_visualization.py", "w", encoding="utf-8") as file:
        file.write(code)

    print(f"Generated Manim code has been saved to 'manim_visualization.py'")

if __name__ == "__main__":
    main()
