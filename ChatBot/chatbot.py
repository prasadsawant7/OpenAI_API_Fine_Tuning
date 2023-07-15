import dotenv
import re
import openai

openai.api_key = dotenv.get_key(".env", "OPENAI_API_KEY")


def remove_escape_sequence_from_beg_end(completion: str) -> str:
    pattern = r"^(\n|\t)+|(\n|\t)+$"
    modified_completion = re.sub(pattern, "", completion)
    return modified_completion


def get_completion(prompt: str) -> str:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Answer this as an Psychatrist: {prompt}",
        temperature=0.4,
        max_tokens=100,
    )
    completion = remove_escape_sequence_from_beg_end(response.choices[0].text)
    return completion
