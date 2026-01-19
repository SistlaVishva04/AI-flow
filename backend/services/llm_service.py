import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def call_llm(config, query, context):
    model_name = config.get("model", "gemini-pro")

    system_prompt = config.get("systemPrompt", "")
    use_context = config.get("useContext", True)

    prompt = ""

    if system_prompt:
        prompt += f"System Instruction:\n{system_prompt}\n\n"

    if use_context and context and len(context) > 0:
        context_text = "\n".join([c["text"] for c in context])
        prompt += f"Context:\n{context_text}\n\n"
    else:
        return "No relevant information found in the provided document."

    prompt += f"User Question:\n{query}"

    model = genai.GenerativeModel(model_name)

    response = model.generate_content(prompt)

    return response.text
