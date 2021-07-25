# Setup

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

# Run

The `gpt3.py` file contains the function that calls the API, and the `program.py` file, which calls it, is what we'll execute.  So just go:

```shell
python program.py
```

# Finetune

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