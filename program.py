from gpt3 import gpt3


def finetuned_gpt3(model, prompt):
   answer, prompt = gpt3(prompt,
                        model=model,
                        temperature=0.7,
                        frequency_penalty=1,
                        presence_penalty=1,
                        start_text='',
                        restart_text='',
                        stop_seq=["\n"])

   return answer, prompt


def generic_gpt3(prompt):
    answer, prompt = gpt3(prompt,
                        temperature=0.7,
                        frequency_penalty=0.25,
                        presence_penalty=0.25,
                        start_text='',
                        restart_text='',
                        stop_seq=["\n"])

    return answer, prompt


def main():
    # Name of finetuned model you want to use
    model = "curie:ft-user-8vvgaglgwj7ddjz3wpbnelsv-2021-07-26-15-48-58"

    prompt = """Steve: Is everything a joke to you?
    Tony: Funny things.
    Steve:"""
    print(prompt)

    flag = True

    while flag:
        # Comment out one of these, depending on which you want to use
        answer, prompt = finetuned_gpt3(model, prompt)
        # answer, prompt = generic_gpt3(prompt)

        print(answer)

        inp = input()
        if inp == "Quit":
            flag = False
        else:
            prompt = answer + inp

if __name__ == '__main__':
    main()