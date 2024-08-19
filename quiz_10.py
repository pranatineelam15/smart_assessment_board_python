import random
states_and_capitals = {
    "Andhra Pradesh": "Amaravati",
    "Arunachal Pradesh": "Itanagar",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Chhattisgarh": "Raipur",
    "Goa": "Panaji",
    "Gujarat": "Gandhinagar",
    "Haryana": "Chandigarh",
    "Himachal Pradesh": "Shimla",
    "Jharkhand": "Ranchi",
    "Karnataka": "Bengaluru",
    "Kerala": "Thiruvananthapuram",
    "Madhya Pradesh": "Bhopal",
    "Maharashtra": "Mumbai",
    "Manipur": "Imphal",
    "Meghalaya": "Shillong",
    "Mizoram": "Aizawl",
    "Nagaland": "Kohima",
    "Odisha": "Bhubaneswar",
    "Punjab": "Chandigarh",
    "Rajasthan": "Jaipur",
    "Sikkim": "Gangtok",
    "Tamil Nadu": "Chennai",
    "Telangana": "Hyderabad",
    "Tripura": "Agartala",
    "Uttar Pradesh": "Lucknow",
    "Uttarakhand": "Dehradun",
    "West Bengal": "Kolkata"
}
def conduct_quiz():
    states = list(states_and_capitals.keys())
    random.shuffle(states)
    quiz_states = states[:10]
    score = 0
    print("Welcome to the States and Capitals Quiz!")
    print(f"There are 10 questions in this quiz. Let's begin!\n")
    for state in quiz_states:
        answer = input(f"What is the capital of {state}? ").strip()
        if answer.lower() == states_and_capitals[state].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The capital of {state} is {states_and_capitals[state]}.\n")
    print("\nQuiz over!")
    print(f"Your final score is: {score}/10")
    print("Thank you for participating!")
if __name__ == "__main__":
    conduct_quiz()