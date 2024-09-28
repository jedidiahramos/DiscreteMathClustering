import json
import random
from AI import get_response 

def load_questions(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)
    
def categorize_questions(questions, category):
    c_q = [] # categorized questions
    for question in questions:
        c_q.append({"question": question, "category": category})
    return c_q

def main():
    
    categories = [
        "Sets, Proofs, and Induction",
        "Formal Logic",
        "Relations",
        "Functions"
    ]
    
    questions = load_questions('questions.json')
    
    sets_proofs_induction = categorize_questions(questions[categories[0]], categories[0])
    formal_logic = categorize_questions(questions[categories[1]], categories[1])
    relations = categorize_questions(questions[categories[2]], categories[2])
    functions = categorize_questions(questions[categories[3]], categories[3])
    
    # Combine all the questions into one list
    combined_questions = sets_proofs_induction + formal_logic + relations + functions
    
    # Randomize the order of the combined list
    random.shuffle(combined_questions)
    
    # Only take the first 10 questions
    test_questions = combined_questions[:10]
    
    # Score variable for chatgpt's performance
    score = 0
    
    # Keep track of the wrong questions
    wrong_questions = []
    
    for i, q in enumerate(test_questions):
        # Prints the Question and its Correct Category
        print(f"Question #{i + 1}:\n{q["question"]}\nCorrect Category: {q["category"]}")
        
        # Prints the AI's response to the question's category
        response = get_response(q["question"])
        print(f"AI: {response}\n")
        
        if (response == q["category"]):
            score += 1
        else:
            wrong_questions.append(i + 1)
    
    print(f"Score: {score}/{len(test_questions)}")
    print(f"Accuracy: {score/len(test_questions)*100}%")
    print(f"Wrong Questions: {wrong_questions}")

        
if __name__ == "__main__":
    main()