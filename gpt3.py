import os
import openai

openai.api_key = os.getenv('OPENAI_KEY')


def gpt3(prompt, engine='davinci', model=None, response_length=64,
         temperature=0.7, top_p=1, frequency_penalty=0, presence_penalty=0,
         start_text='', restart_text='', stop_seq=None):
    
    if model:
        response = openai.Completion.create(
            prompt=prompt + start_text,
            model=model,
            max_tokens=response_length,
            temperature=temperature,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            stop=stop_seq,
        )
    else:
        response = openai.Completion.create(
            prompt=prompt + start_text,
            engine=engine,
            max_tokens=response_length,
            temperature=temperature,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            stop=stop_seq,
        )
    answer = response.choices[0]['text']
    new_prompt = prompt + start_text + answer + restart_text
    return answer, new_prompt