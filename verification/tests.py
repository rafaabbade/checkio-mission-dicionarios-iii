"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [

    {
        "input": [[("nome", "Alice"), ("idade", "25")]],
        "answer": (["Alice", "25"]),
        
    },
    {
        "input": [[('cidade', 'São Paulo'), ('população', 12000000)]],
        "answer": (['São Paulo', 12000000]),
    },
    {
        "input": [[('cor', 'vermelho'), ('valor', 255)]],
        "answer": (['vermelho', 255])
    }
    ]
}
