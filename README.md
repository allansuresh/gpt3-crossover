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

The `gpt3.py` file contains the function that calls the API, and the program.py file, which calls it, is what we'll execute.  So just go:

```shell
python program.py
```