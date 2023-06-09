Suspension Data
=================================

Introduction
------------

The Suspension Project aims to organize government-provided data on student leave reasons and present it in a visual format on a website using Vue3. The data processing for this project is done in Python. Additionally, OpenAI's fine-tune is used to train a GPT model for predicting data traits changes.

Objective
---------

The objective of the Suspension Project is to create a user-friendly website that displays student leave reasons data in an easily understandable and visually appealing manner. By organizing the government-provided data, we aim to provide valuable insights into student leave patterns and reasons. The integration of OpenAI's fine-tuned GPT model allows us to make predictions about future data traits changes based on historical patterns.

Usage
-----

Please make sure you have these tools installed:

- `poetry`
- `pyenv`

To get the Suspension Project, follow this steps:

- Clone the repository:

```bash
git clone git@github.com:Xanonymous-GitHub/suspension-data.git
```

- Install specific python environment:

```bash
pyenv install 3.10
```

- Change to that version of python locally:

```bash
pyenv local 3.10
```

- Switch to the python environment:

```bash
poetry env use "$(pyenv which python3)"
```

- Install dependencies:

```bash
poetry install
```

- Start the development shell:

```bash
poetry shell
```

- Since we are using a virtual environment, set the `PYTHONPATH` at the **project root folder** to run successfullly:

```bash
export PYTHONPATH="${PYTHONPATH}:`pwd`"
```

- Execute the main script:

```bash
python3 main.py
```

Check Typing
-----

- `pytype $(git ls-files '*.py')`

License
-------

The Suspension Project is licensed under the MIT License. Please review the license file for more information.

Contact
-------

If you have any questions, suggestions, or feedback regarding the Suspension Project, please contact the project maintainer or open an issue in the repository.
