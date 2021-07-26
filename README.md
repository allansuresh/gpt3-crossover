# Crossovers Using GPT-3

This is a project that uses a finetuned model of OpenAI's GPT-3 to generate user-defined crossover scripts between DC and Marvel.

The model was finetuned using film scripts from the MCU and DCEU, formatted in the form of JSONL {"prompt":"<prev_dialogue>\n<Speaker>:","completion":"dialogue"} pairs.  Owing to limited data, this finetuning was limited to main characters, so it will work best with those characters.  Skip [here](#run) to try it.

## Setup

Set up a Python virtual environment using the following command in the root directory:

Windows:

```shell
$ python -m venv venv
$ venv\Scripts\activate
```

Mac / Linux:

```shell
$ python3 -m venv venv
$ source venv/bin/activate
```

Now install the OpenAI package:

```bash
(venv) $ pip install openai
```

Set the OpenAI key as an environment variable using the following command (replace <...> with your key):

Windows:

```shell
(venv) $ set OPENAI_KEY=<your-openai-key-here>
```

Mac / Linux:

```shell
(venv) $ export OPENAI_KEY="<your-openai-key-here>"
```

## Run

The `gpt3.py` file contains the function that calls the API, and the `program.py` file, which calls it, is what we'll execute.  So just go:

```shell
python program.py
```

This returns a line of dialogue given the prompt in the file (which can be edited - stick to that format though, it works best), and skips to a new line asking for input.  Give the tag of a character (refer below) followed by `:`, press Enter, and the process repeats.  When you want to stop, just type `Quit`.

You can also use the vanilla GPT-3 model if you want, by commenting out the line in the `main()` function that calls `finetuned_gpt3()` and uncommenting the line that calls `generic_gpt3()`.

### Characters

This is a list of characters the model was finetuned on and will thus work best with, along with the tag you should use in generation for them:

| Character Name   | Tag            |
| ---------------- | -------------- |
| Tony Stark       | Tony           |
| Steve Rogers     | Steve          |
| Thor             | Thor           |
| Loki             | Loki           |
| Scott Lang       | Scott          |
| Peter Parker     | Peter          |
| Natasha Romanoff | Black Widow    |
| Bruce Banner     | Bruce Banner   |
| Nick Fury        | Fury           |
| Clint Barton     | Hawkeye        |
| Wanda Maximoff   | Wanda          |
| Vision           | Vision         |
| Carol Danvers    | Captain Marvel |
| Thanos           | Thanos         |
| Peter Quill      | Star-Lord      |
| Stephen Strange  | Doctor Strange |
| Arthur Curry     | Aquaman        |
| Bruce Wayne      | Batman         |
| Clark Kent       | Superman       |
| Wonder Woman     | Wonder Woman   |

## Finetune

If you want to try finetuning using your own data, format it in a JSONL file according to [these](https://beta.openai.com/docs/guides/fine-tuning) requirements.  After that, upload your file by editing the `filename` variable in the `finetune.py` file to the name of your file, and running the Python script as follows:

```shell
python finetune.py u
```

After that, you can list the files you've uploaded to get the file ID of your data file.  Run `finetune.py` again as:

```shell
python finetune.py l
```

Now, edit the `file_id` variable in `finetune.py` with the file ID you just got.  And now, to create the fine-tuning job, run `finetune.py` for the last time, as:

```shell
python finetune.py f
```

Other functionalities using this program including deleting an uploaded file (pass `d` as argument after editing the file ID in the program), and listing all finetuning jobs (pass `fl` as argument).