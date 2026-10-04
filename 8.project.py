#This is 8th project.
#Simple Quiz Game.
questions = {
    "1": {
        "question": "What is the output of: print(3 + 2 * 2)?",
        "options": {"a": "10", "b": "7", "c": "12", "d": "8"},
        "answer": "b"
    },
    "2": {
        "question": "What is the output of: print(10 % 3)?",
        "options": {"a": "3", "b": "1", "c": "0", "d": "10"},
        "answer": "b"
    },
    "3": {
        "question": "What is the output of: print(len('Python'))?",
        "options": {"a": "5", "b": "6", "c": "7", "d": "Error"},
        "answer": "b"
    },
    "4": {
        "question": "What is the output of: print('5' + '5')?",
        "options": {"a": "10", "b": "55", "c": "Error", "d": "5 5"},
        "answer": "b"
    },
    "5": {
        "question": "What is the output of: print(bool(0))?",
        "options": {"a": "True", "b": "False", "c": "0", "d": "Error"},
        "answer": "b"
    },
    "6": {
        "question": "What is the output of: x = [1,2,3]; print(x[-1])?",
        "options": {"a": "1", "b": "3", "c": "Error", "d": "[3]"},
        "answer": "b"
    },
    "7": {
        "question": "How many times will this loop run? for i in range(5): print(i)",
        "options": {"a": "4", "b": "5", "c": "6", "d": "Infinite"},
        "answer": "b"
    },
    "8": {
        "question": "What is the output of: print(type(5.0))?",
        "options": {"a": "<class 'int'>", "b": "<class 'float'>", "c": "<class 'str'>", "d": "Error"},
        "answer": "b"
    },
    "9": {
        "question": "What is the output of: x = 5; x += 3; print(x)?",
        "options": {"a": "5", "b": "3", "c": "8", "d": "53"},
        "answer": "c"
    },
    "10": {
        "question": "What is the output of: print('Hello'[1])?",
        "options": {"a": "H", "b": "e", "c": "l", "d": "Error"},
        "answer": "b"
    }
}

score = 0

print(" Welcome to the Quiz Game!\n")

for key, q in questions.items():
    print(q["question"])
    for opt_key, opt_value in q["options"].items():
        print(f"{opt_key}. {opt_value}")
    
    user_answer = input("Your answer: ").lower()
    
    if user_answer == q["answer"]:
        print(" Correct!\n")
        score += 1
    else:
        print(f" Wrong! Correct answer: {q['answer']}\n")

print(f" Quiz Over! Your final score: {score}/{len(questions)}")