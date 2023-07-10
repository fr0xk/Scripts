#include <iostream>

class DecisionTree {
public:
    bool isScaredOfDeath() {
        return getBooleanInput("Are people afraid of death? (1 = Yes, 0 = No): ");
    }

    bool hasPurpose() {
        return getBooleanInput("Do people believe their lives have a purpose? (1 = Yes, 0 = No): ");
    }

    bool isAnimalWithConsciencePurposeful() {
        return getBooleanInput("Are animals with a conscience living just to eat, sleep, and reproduce? (1 = Yes, 0 = No): ");
    }

    bool providesSenseOfPurpose() {
        return getBooleanInput("Does religion provide a sense of purpose? (1 = Yes, 0 = No): ");
    }

    bool isMoralValueDriven() {
        return getBooleanInput("Do all religious stories make people feel scared of eternal and hypothetical punishment in the absence of practicing moral values? (1 = Yes, 0 = No): ");
    }

    void start() {
        bool scaredOfDeath = isScaredOfDeath();
        bool hasPurposeBelief = hasPurpose();
        bool animalPurposeful = isAnimalWithConsciencePurposeful();
        bool religionPurpose = providesSenseOfPurpose();
        bool moralValueDriven = isMoralValueDriven();

        if (scaredOfDeath) {
            if (hasPurposeBelief && animalPurposeful) {
                if (religionPurpose) {
                    printMessage("Religion provides a sense of purpose.");
                } else {
                    printMessage("All religious stories make people feel scared of eternal and hypothetical punishment in the absence of practicing moral values.");
                }
            } else {
                printMessage("All religious stories make people feel scared of eternal and hypothetical punishment in the absence of practicing moral values.");
            }
        } else {
            if (hasPurposeBelief) {
                if (religionPurpose) {
                    printMessage("Religion provides a sense of purpose.");
                } else {
                    printMessage("All religious stories make people feel scared of eternal and hypothetical punishment in the absence of practicing moral values.");
                }
            } else {
                if (religionPurpose) {
                    printMessage("Religion provides a sense of purpose.");
                } else if (moralValueDriven) {
                    printMessage("People are driven by fear of eternal and hypothetical punishment in the absence of practicing moral values.");
                } else {
                    printMessage("Some other case...");
                }
            }
        }
    }

private:
    bool getBooleanInput(const std::string& prompt) {
        bool response;
        std::cout << prompt;
        std::cin >> response;
        return response;
    }

    void printMessage(const std::string& message) {
        std::cout << message << std::endl;
    }
};

int main() {
    DecisionTree decisionTree;
    decisionTree.start();
    return 0;
}
