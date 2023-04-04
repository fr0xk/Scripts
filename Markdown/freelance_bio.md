# Description

This program defines personal `'Sudarshan Kakoty'`, with a class containing a `describe` hat returns a string description of the sudarshan's identity, skills, and portfolio.

## Usage

To use this program, first define a `Freelancer` object with a name, profession, skills, and portfolio. Then call the `describe` method to generate a description of the freelancer's work.

```python
class Freelancer:
    
    def __init__(self, name, profession, skills, portfolio):
        self.name = name
        self.profession = profession
        self.skills = skills
        self.portfolio = portfolio
        
    def describe(self):
        """
        Return my identity 
        """
        bio = f"Hello, I'm {self.name}, a {self.profession} skilled in {', '.join(self.skills)}.\n"
        bio += "With a passion for delivering quality work to clients, I have completed several projects across various industries.\n"
        bio += "My portfolio showcases my proficiency in the following areas:\n"
        
        for item in self.portfolio:
            bio += f"- {item}\n"
        
        bio += "As a freelancer, I pride myself on my ability to deliver while maintaining open communication with clients.\n"
        bio += "I am always looking for new and exciting opportunities to challenge myself and expand my skillset.\n"
        
        return bio


# Example usage
sudarshan = Freelancer(
    name="Sudarshan Kakoty",
    profession="Programmer, Teacher",
    skills=["Comouter Programming", "Physics", "Mathematical Analysis", "System Administration"],
    portfolio=["Developed few automation processes in finance industry"]
)

print(sudarshan.describe())

