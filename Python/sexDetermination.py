import numpy as np

class Individual:
    def __init__(self, chromosomes, hormone_levels, physical_characteristics, genetic_markers, self_identification):
        self.chromosomes = chromosomes
        self.hormone_levels = hormone_levels
        self.physical_characteristics = physical_characteristics
        self.genetic_markers = genetic_markers
        self.self_identification = self_identification

def determine_sex(individual):
    sex_mapping = {
        'chromosomal': {'XX': 'Female', 'XY': 'Male'},
        'hormonal': {'male': 'Male', 'female': 'Female'},
        'physical': {'typical male': 'Male', 'typical female': 'Female'},
        'genetic': {'SRY': 'Male', 'SOX9': 'Female'}
    }

    chromosomal_sex = sex_mapping['chromosomal'].get(individual.chromosomes, 'Atypical')
    hormonal_sex = sex_mapping['hormonal'].get(np.sign(individual.hormone_levels['testosterone'] - individual.hormone_levels['estrogen']) + 1, 'Atypical')
    physical_sex = sex_mapping['physical'].get(individual.physical_characteristics[0], 'Atypical')
    genetic_sex = sex_mapping['genetic'].get(individual.genetic_markers[0], 'Atypical')

    return {
        'Chromosomal Sex': chromosomal_sex,
        'Hormonal Sex': hormonal_sex,
        'Physical Sex': physical_sex,
        'Genetic Sex': genetic_sex,
        'Self-Identified Sex': individual.self_identification
    }

individual = Individual(
    chromosomes='XY',
    hormone_levels={'testosterone': 500, 'estrogen': 50},
    physical_characteristics=['typical male'],
    genetic_markers=['SRY'],
    self_identification='Male'
)

sex_determination = determine_sex(individual)
print(sex_determination)
