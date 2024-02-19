import json
from difflib import get_close_matches

def load_knowledge_base(file_path: str) -> dict:
    with open(file_path , 'r') as file:
        data:dict = json.load(file)
    return data
#loaded our knowledge base


def save_knowledge_base(file_path :str , data:dict):
    with open(file_path , 'w') as file:
        json.dump(data , file,  indent=2)
#saved  our knowledge base


def find_best_match(user_question: str , question :list[str]) -> str | None :
    matches: list = get_close_matches(user_question  , question , n=1, cutoff = 0.9)
    return matches[0] if matches else None
#finding best matches base on out knowledge base


def get_answer_for_question(question: str , base : dict) -> str | None:
    for q in base["question"] :
        if q["question"] == question :
            return q["answer"]
#we get our answer here

def chat():
    knowledge_base: dict = load_knowledge_base('base.json')
    
    while True:
        user_input : str = input("user: ")
        
        if user_input.lower() == 'quit':
            break
        
        best_match: str| None = find_best_match(user_input , [q["question"] for q in knowledge_base["question"]])
        if best_match:
            answer: str = get_answer_for_question(best_match , knowledge_base)
            print(f'Bot : {answer}')
        else:
            print('Bot : Can you teach me??')
            new_answer:str = input('Type the answer :')
            
            if new_answer.lower()!= 'skip':
                knowledge_base["question"].append({"question": user_input , "answer": new_answer})
                save_knowledge_base('base.json' , knowledge_base)
                print('Bot : Learned something new')
#our main function that run the chatbout

if __name__ == '__main__':
    chat()


