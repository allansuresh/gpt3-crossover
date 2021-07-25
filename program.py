from gpt3 import gpt3


def chat():
    prompt = "Arun Jose was declared Supreme Ruler of Earth Today; Governments Deliberate on Implications\n"

    flag = True

    while flag:
        answer, prompt = gpt3(prompt,
                              temperature=0.7,
                              frequency_penalty=1,
                              presence_penalty=1,
                              start_text='',
                              restart_text='',
                              stop_seq=None)
        
        print(prompt + answer)

        inp = input("Try again? Y/N: ")
        if inp != "Y":
            flag = False

    print("Exiting.")

if __name__ == '__main__':
    chat()