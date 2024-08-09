# function to summarize_chapters function
import replicate
def summarize_chapters(query):
    output = replicate.run(
        "mistralai/mixtral-8x7b-instruct-v0.1",
        input={
            "debug": False,
            "top_k": 50,
            "top_p": 1,
            "prompt": query,
            "temperature": 0.7,
            "system_prompt": "summarize the text given",
            "max_new_tokens": 1024,
            "min_new_tokens": -1
        }
    )
    
    return output