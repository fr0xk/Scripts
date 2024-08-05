import numpy as np

class Individual:
    def __init__(self, karyotype, endocrine_profile, phenotypic_traits, genetic_loci, gender_identity):
        self.karyotype = karyotype
        self.endocrine_profile = endocrine_profile
        self.phenotypic_traits = phenotypic_traits
        self.genetic_loci = genetic_loci
        self.gender_identity = gender_identity

    def validate(self):
        assert isinstance(self.karyotype, str), "Karyotype should be a string."
        assert isinstance(self.endocrine_profile, dict), "Endocrine profile should be a dictionary."
        assert isinstance(self.phenotypic_traits, list), "Phenotypic traits should be a list."
        assert isinstance(self.genetic_loci, list), "Genetic loci should be a list."
        assert isinstance(self.gender_identity, str), "Gender identity should be a string."

def determine_sex(individual):
    sex_mapping = {
        'chromosomal': {
            'XX': 'Female', 'XY': 'Male', 'XO': 'Turner Syndrome', 'XXY': 'Klinefelter Syndrome',
            'XXX': 'Triple X Syndrome', 'XYY': 'XYY Syndrome', 'XXXY': 'XXXY Syndrome'
        },
        'hormonal': lambda profile: 'Male' if profile['testosterone'] > profile['estrogen'] else 'Female',
        'phenotypic': {
            'typical male': 'Male', 'typical female': 'Female', 'ambiguous': 'Ambiguous',
            'clitoromegaly': 'Clitoromegaly', 'micropenis': 'Micropenis'
        },
        'genetic': {
            'SRY': 'Male', 'SOX9': 'Female', '5-ARD': '5-Alpha Reductase Deficiency',
            'AIS': 'Androgen Insensitivity Syndrome', 'CAH': 'Congenital Adrenal Hyperplasia'
        }
    }

    individual.validate()
    
    chromosomal_sex = sex_mapping['chromosomal'].get(individual.karyotype, 'Atypical')
    hormonal_sex = sex_mapping['hormonal'](individual.endocrine_profile)
    phenotypic_sex = sex_mapping['phenotypic'].get(individual.phenotypic_traits[0] if individual.phenotypic_traits else None, 'Atypical')
    genetic_sex = sex_mapping['genetic'].get(individual.genetic_loci[0] if individual.genetic_loci else None, 'Atypical')

    comparisons = [
        (chromosomal_sex, hormonal_sex, "Chromosomal vs Hormonal"),
        (chromosomal_sex, phenotypic_sex, "Chromosomal vs Phenotypic"),
        (chromosomal_sex, genetic_sex, "Chromosomal vs Genetic"),
        (hormonal_sex, phenotypic_sex, "Hormonal vs Phenotypic"),
        (hormonal_sex, genetic_sex, "Hormonal vs Genetic"),
        (phenotypic_sex, genetic_sex, "Phenotypic vs Genetic")
    ]
    
    discrepancies = list(filter(lambda x: x[0] != x[1], comparisons))
    discrepancy_labels = list(map(lambda x: x[2], discrepancies))

    return {
        'Chromosomal Sex': chromosomal_sex,
        'Hormonal Sex': hormonal_sex,
        'Phenotypic Sex': phenotypic_sex,
        'Genetic Sex': genetic_sex,
        'Self-Identified Sex': individual.gender_identity,
        'Discrepancies': discrepancy_labels or "None"
    }

def get_user_input():
    karyotype = input("Enter karyotype (e.g., 'XX', 'XY', 'XO', 'XXY', 'XXX', 'XYY', 'XXXY'): ")
    testosterone = float(input("Enter testosterone level (ng/dL, typical range: 300-1000 for males, 15-70 for females): "))
    estrogen = float(input("Enter estrogen level (pg/mL, typical range: 15-60 for males, 15-350 for females): "))
    phenotypic_traits = input("Enter phenotypic traits (e.g., 'typical male', 'typical female', 'ambiguous', 'clitoromegaly', 'micropenis'): ").split(',')
    genetic_loci = input("Enter genetic loci (e.g., 'SRY', 'SOX9', '5-ARD', 'AIS', 'CAH'): ").split(',')
    gender_identity = input("Enter self-identified gender: ")

    return Individual(
        karyotype=karyotype,
        endocrine_profile={'testosterone': testosterone, 'estrogen': estrogen},
        phenotypic_traits=phenotypic_traits,
        genetic_loci=genetic_loci,
        gender_identity=gender_identity
    )

individual = get_user_input()
sex_determination = determine_sex(individual)
print(sex_determination)
