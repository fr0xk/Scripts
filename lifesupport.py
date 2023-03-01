import time

# Define decision tree nodes

def ask_question(question, yes_node, no_node):

    response = input(question)

    if response.lower() == "y":

        return yes_node()

    elif response.lower() == "n":

        return no_node()

    else:

        print("Invalid input. Please try again.")

        return ask_question(question, yes_node, no_node)

def ask_health():

    return ask_question(

        "Have you taken care of your physical health today? (y/n) ",

        ask_online_work,

        ask_physical_activity

    )

def ask_physical_activity():

    return ask_question(

        "Have you engaged in physical activity today? (y/n) ",

        ask_online_work,

        lambda: print("Remember to engage in at least 30 minutes of moderate physical activity each day. This can help improve your physical and mental health.") or ask_online_work()

    )

def ask_online_work():

    return ask_question(

        "Have you spent time looking for online work opportunities today? (y/n) ",

        ask_learning,

        lambda: print("Remember to explore online work options. This can help supplement your income.") or ask_question(

            "Do you have a job or other work today? (y/n) ",

            ask_learning,

            ask_financial_health

        )

    )

def ask_learning():

    return ask_question(

        "Have you spent time learning something new today? (y/n) ",

        ask_financial_health,

        lambda: print("Remember to prioritize learning new skills. This can help increase your earning potential and improve your overall well-being.") or ask_learning_details()

    )

def ask_learning_details():

    skill = input("What skill do you want to work on today? (e.g. coding, graphic design, digital marketing) ")

    print(f"Remember to set aside time each week to work on {skill}.")

    return ask_financial_health()

def ask_financial_health():

    return ask_question(

        "Have you taken steps to improve your financial health today? (y/n) ",

        ask_social_support,

        lambda: print("Remember to prioritize your financial health. Consider talking to a financial advisor or setting up a budget to better manage your finances.") or ask_social_support()

    )

def ask_social_support():

    return ask_question(

        "Have you reached out to friends or family for social support today? (y/n) ",

        lambda: print("Great job! Social support can have a positive impact on your mental and physical health."),

        lambda: print("Remember to prioritize your social connections. Consider reaching out to friends or family members for support.") or ask_question(

            "Do you have any social activities planned for today? (y/n) ",

            lambda: print("Great! Enjoy your social activity."),

            lambda: print("Remember to schedule time for social activities. This can help improve your overall well-being.") or None

        )

    )

# Run decision tree

def main():

    ask_health()

if __name__ == "__main__":

    main()

