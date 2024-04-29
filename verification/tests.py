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
        "input": [[('cidade', 'São Paulo'), ('população', 12_000_000)]],
        "answer": (['cidade', 'população'], ['São Paulo', 12000000], [('cidade', 'São Paulo'), ('população', 12000000)])
    },
    {
        "input": [[('cor', 'vermelho'), ('valor', 255)]],
        "answer": (['cor', 'valor'], ['vermelho', 255], [('cor', 'vermelho'), ('valor', 255)])
    }
    ]
}
