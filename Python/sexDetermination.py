import numpy as np

class Individual:
    def __init__(self, karyotype, endocrine_profile, phenotypic_traits, genetic_loci, gender_identity):
        self.karyotype = karyotype
        self.endocrine_profile = endocrine_profile
        self.phenotypic_traits = phenotypic_traits
        self.genetic_loci = genetic_loci
        self.gender_identity = gender_identity

    def validate(self):
        if not isinstance(self.karyotype, str):
            raise ValueError("Karyotype should be a string.")
        if not isinstance(self.endocrine_profile, dict):
            raise ValueError("Endocrine profile should be a dictionary.")
        if not isinstance(self.phenotypic_traits, list):
            raise ValueError("Phenotypic traits should be a list.")
        if not isinstance(self.genetic_loci, list):
            raise ValueError("Genetic loci should be a list.")
        if not isinstance(self.gender_identity, str):
            raise ValueError("Gender identity should be a string.")

def determine_sex(individual):
    sex_mapping = {
        'chromosomal': {'XX': 'Female', 'XY': 'Male'},
        'hormonal': lambda profile: 'Male' if profile['testosterone'] > profile['estrogen'] else 'Female',
        'phenotypic': {'typical male': 'Male', 'typical female': 'Female'},
        'genetic': {'SRY': 'Male', 'SOX9': 'Female'}
    }

    try:
        individual.validate()
        
        chromosomal_sex = sex_mapping['chromosomal'].get(individual.karyotype, 'Atypical')
        hormonal_sex = sex_mapping'hormonal'
        phenotypic_sex = sex_mapping['phenotypic'].get(individual.phenotypic_traits[0], 'Atypical')
        genetic_sex = sex_mapping['genetic'].get(individual.genetic_loci[0], 'Atypical')

        return {
            'Chromosomal Sex': chromosomal_sex,
            'Hormonal Sex': hormonal_sex,
            'Phenotypic Sex': phenotypic_sex,
            'Genetic Sex': genetic_sex,
            'Self-Identified Sex': individual.gender_identity
        }
    except Exception as e:
        return str(e)

individual = Individual(
    karyotype='XY',
    endocrine_profile={'testosterone': 500, 'estrogen': 50},
    phenotypic_traits=['typical male'],
    genetic_loci=['SRY'],
    gender_identity='Male'
)

sex_determination = determine_sex(individual)
print(sex_determination)
