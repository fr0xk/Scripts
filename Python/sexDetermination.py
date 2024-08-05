import sys
from functools import partial

class InputValidator:
    @staticmethod
    def validate_non_empty(prompt, value):
        if not value.strip():
            raise ValueError(f"{prompt} cannot be empty.")
        return value

    @staticmethod
    def validate_numeric(prompt, value):
        try:
            return float(value)
        except ValueError:
            raise ValueError(f"{prompt} must be a valid number.")

class UserInput:
    def __init__(self):
        self.karyotype = self.get_input("Enter karyotype (e.g., 'XX', 'XY', 'XO', 'XXY', 'XXX', 'XYY', 'XXXY')", InputValidator.validate_non_empty)
        self.testosterone = self.get_input("Enter testosterone level (ng/dL, typical range: 300-1000 for males, 15-70 for females)", InputValidator.validate_numeric)
        self.estrogen = self.get_input("Enter estrogen level (pg/mL, typical range: 15-60 for males, 15-350 for females)", InputValidator.validate_numeric)
        self.phenotypic_traits = self.get_input("Enter phenotypic traits (e.g., 'typical male', 'typical female', 'ambiguous', 'clitoromegaly', 'micropenis')", InputValidator.validate_non_empty)
        self.genetic_loci = self.get_input("Enter genetic loci (e.g., 'SRY', 'SOX9', '5-ARD', 'AIS', 'CAH')", InputValidator.validate_non_empty)
        self.gender_identity = self.get_input("Enter self-identified gender", InputValidator.validate_non_empty)

    @staticmethod
    def get_input(prompt, validator):
        value = input(f"{prompt}: ")
        return validator(prompt, value)

class SexDetermination:
    sex_mapping = {
        'chromosomal': {
            'XX': 'Female', 'XY': 'Male', 'XO': 'Turner Syndrome', 'XXY': 'Klinefelter Syndrome',
            'XXX': 'Triple X Syndrome', 'XYY': 'XYY Syndrome', 'XXXY': 'XXXY Syndrome'
        },
        'phenotypic': {
            'typical male': 'Male', 'typical female': 'Female', 'ambiguous': 'Ambiguous',
            'clitoromegaly': 'Clitoromegaly', 'micropenis': 'Micropenis'
        },
        'genetic': {
            'SRY': 'Male', 'SOX9': 'Female', '5-ARD': '5-Alpha Reductase Deficiency',
            'AIS': 'Androgen Insensitivity Syndrome', 'CAH': 'Congenital Adrenal Hyperplasia'
        }
    }

    @staticmethod
    def determine_chromosomal_sex(karyotype):
        return SexDetermination.sex_mapping['chromosomal'].get(karyotype, 'Atypical')

    @staticmethod
    def determine_hormonal_sex(endocrine_profile):
        return 'Male' if endocrine_profile['testosterone'] > endocrine_profile['estrogen'] else 'Female'

    @staticmethod
    def determine_phenotypic_sex(phenotypic_trait):
        return SexDetermination.sex_mapping['phenotypic'].get(phenotypic_trait, 'Atypical')

    @staticmethod
    def determine_genetic_sex(genetic_locus):
        return SexDetermination.sex_mapping['genetic'].get(genetic_locus, 'Atypical')

    @staticmethod
    def find_discrepancies(sex_attributes):
        compare = partial(SexDetermination.compare_attributes, sex_attributes)
        discrepancies = filter(None, map(compare, [
            ("Chromosomal vs Hormonal", "Chromosomal Sex", "Hormonal Sex"),
            ("Chromosomal vs Phenotypic", "Chromosomal Sex", "Phenotypic Sex"),
            ("Chromosomal vs Genetic", "Chromosomal Sex", "Genetic Sex"),
            ("Hormonal vs Phenotypic", "Hormonal Sex", "Phenotypic Sex"),
            ("Hormonal vs Genetic", "Hormonal Sex", "Genetic Sex"),
            ("Phenotypic vs Genetic", "Phenotypic Sex", "Genetic Sex")
        ]))
        return list(discrepancies)

    @staticmethod
    def compare_attributes(sex_attributes, comparison):
        label, attr1, attr2 = comparison
        return label if sex_attributes[attr1] != sex_attributes[attr2] else None

def display_results(sex_attributes):
    print("\n=== Sex Determination Report ===")
    for key, value in sex_attributes.items():
        print(f"{key}: {value}")
    print("================================")

def main():
    user_input = UserInput()

    chromosomal_sex = SexDetermination.determine_chromosomal_sex(user_input.karyotype)
    hormonal_sex = SexDetermination.determine_hormonal_sex({'testosterone': user_input.testosterone, 'estrogen': user_input.estrogen})
    phenotypic_sex = SexDetermination.determine_phenotypic_sex(user_input.phenotypic_traits)
    genetic_sex = SexDetermination.determine_genetic_sex(user_input.genetic_loci)

    sex_attributes = {
        'Chromosomal Sex': chromosomal_sex,
        'Hormonal Sex': hormonal_sex,
        'Phenotypic Sex': phenotypic_sex,
        'Genetic Sex': genetic_sex,
        'Self-Identified Sex': user_input.gender_identity,
        'Discrepancies': SexDetermination.find_discrepancies({
            'Chromosomal Sex': chromosomal_sex,
            'Hormonal Sex': hormonal_sex,
            'Phenotypic Sex': phenotypic_sex,
            'Genetic Sex': genetic_sex
        }) or "None"
    }

    display_results(sex_attributes)

if __name__ == '__main__':
    try:
        main()
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        
