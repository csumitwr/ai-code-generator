# Chunk 1
import ollama


# Chunk 2
MODEL_NAME = "qwen2.5:7b"


# Chunk 3
def build_prompt(user_prompt, language):
    prompt = f"""
You are an expert software engineer and coding teacher.

Generate clean and beginner-friendly {language} code.

User Request:
{user_prompt}

IMPORTANT RULES:
1. Generate ONLY the code only. No comments, no explanation inside the code.
2. After the code, write:

EXPLANATION:
3. Keep explanations beginner friendly.
4. Explain in very short chunks.
5. Maximum 2-3 lines per chunk.
6. Keep the code simple and readable.
"""

    return prompt.strip()


# Chunk 4
def generate_code(user_prompt, language):
    try:
        final_prompt = build_prompt(user_prompt, language)

        response = ollama.chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": final_prompt
                }
            ]
        )

        output = response["message"]["content"]

        return output

    except Exception as error:
        return f"Error: {str(error)}"