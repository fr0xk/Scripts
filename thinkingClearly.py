# Define the decision tree using a list of tuples
decision_tree = [
    ("What is the problem?: ",
     [("Is the problem urgent?",
       [("Take action immediately.", lambda: True),
        ("Delegate the task to someone else.", lambda: True)]),
      ("Is the problem recurring?",
       [("Have you addressed the root cause of the problem?",
         [("Take action to fix the problem.", lambda: True),
          ("Investigate the root cause of the problem.", lambda: True)])]),
      ("Do you have enough information to make a decision?",
       [("Make a decision based on the available information.", lambda: True),
        ("Gather more information before making a decision.", lambda: True)])]),
    ("Have you considered the consequences?",
     [("What are the potential positive consequences?",
       [("Proceed with the decision.", lambda: True),
        ("Re-evaluate the decision.", lambda: True)]),
      ("What are the potential negative consequences?",
       [("Re-evaluate the decision.", lambda: True),
        ("Proceed with caution.", lambda: True)])]),
    ("What is the opportunity cost?",
     [("Are there alternative choices to consider?",
       [("Evaluate the alternatives.", lambda: True),
        ("Proceed with the decision.", lambda: True)])]),
    ("What is the worst-case scenario?",
     [("What can go wrong?",
       [("Consider the risks and mitigate them.", lambda: True),
        ("Re-evaluate the decision.", lambda: True)])])]

# Define a function to traverse the decision tree
def traverse_decision_tree(tree):
    question, answers = tree[0], tree[1]
    print(question)
    for i, answer in enumerate(answers):
        print(f"{i+1}. {answer[0]}")
    choice = input("Enter your choice: ")
    if choice.isdigit() and int(choice) in range(1, len(answers)+1):
        answer = answers[int(choice)-1]
        if answer[1]():
            print(answer[0])
        else:
            traverse_decision_tree(answer[1])
    else:
        print("Invalid choice. Please try again.")
        traverse_decision_tree(tree)

# Ask the user for the problem
problem = input("What is the problem? ")

# Traverse the decision tree for the given problem
if "urgent" in problem.lower():
    traverse_decision_tree(decision_tree[0])
elif "consequences" in problem.lower():
    traverse_decision_tree(decision_tree[1])
elif "opportunity cost" in problem.lower():
    traverse_decision_tree(decision_tree[2])
elif "worst-case scenario" in problem.lower():
    traverse_decision_tree(decision_tree[3])
else:
    print("Sorry, we don't have a decision tree for that problem.")
