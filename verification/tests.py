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
        "input": [[("nome", "Alice"), ("idade", 25)]],
        "answer": (["nome", "idade"], ["Alice", 25], [("nome", "Alice"), ("idade", 25)]),
    }
    ]
}
