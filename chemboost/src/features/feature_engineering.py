import re
import csv
from math import sqrt
from typing import Dict
from pymatgen.core.composition import Composition
import smact
from matminer.featurizers.composition import ElementProperty



def valence_electron_count(compound: str) -> float:
    """Calculate the Valence Electron Count (VEC) for a given chemical compound."""
    def get_element_valence(element: str) -> int:
        try:
            return smact.Element(element).num_valence_modified
        except Exception:
            raise ValueError(f"Valence data not found for element: {element}")
    
    element_stoich = Composition(compound).get_el_amt_dict()
    total_valence = total_stoich = 0
    for element, stoich in element_stoich.items():
        valence = get_element_valence(element)
        total_valence += stoich * valence
        total_stoich += stoich
    return total_valence / total_stoich if total_stoich != 0 else 0.0

def load_element_data(filename: str) -> Dict[str, float]:
    """
    Load element data from a CSV file.
    """
    element_data = {}
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            element = row["element"]
            electronegativity = float(row["Electronegativity"])
            element_data[element] = electronegativity
    return element_data

def parse_formula(formula: str) -> Dict[str, float]:
    """
    Parse a chemical formula into its elements and their stoichiometries.
    """
    pattern = re.compile(r"([A-Z][a-z]*)(\d*\.?\d*)")
    elements = pattern.findall(formula)
    return {elem: float(count) if count else 1.0 for elem, count in elements}

def calculate_atomic_concentrations(formula: str) -> Dict[str, float]:
    """
    Calculate atomic concentrations of elements in a formula.
    """
    parsed_formula = parse_formula(formula)
    total_atoms = sum(parsed_formula.values())
    return {elem: count / total_atoms for elem, count in parsed_formula.items()}

def calculate_electronegativity_difference(formula: str, element_data: Dict[str, float]) -> float:
    """
    Calculate the electronegativity difference in a compound.
    """
    concentrations = calculate_atomic_concentrations(formula)
    avg_electronegativity = sum(
        concentrations[elem] * element_data.get(elem, 0) for elem in concentrations
    )
    diff_sum = sum(
        concentrations[elem] * (element_data.get(elem, 0) - avg_electronegativity) ** 2
        for elem in concentrations
    )
    return sqrt(diff_sum)


def create_feature_matrix(df):
    """Create the complete feature matrix."""
    # Define Magpie features and stats
    features = [
        'Number', 'MendeleevNumber', 'AtomicWeight', 'CovalentRadius', 'Electronegativity', 
    'NsValence', 'NpValence', 'NdValence', 'NfValence', 'NValence', 
    'NsUnfilled', 'NpUnfilled', 'NdUnfilled', 'NfUnfilled', 'NUnfilled', 
    'GSvolume_pa', 'GSbandgap', 'GSmagmom', 'SpaceGroupNumber'

    ]
    stats = ['minimum', 'maximum', 'mean', 'range', 'std_dev']
    
    # Initialize and apply featurizer
    featurizer = ElementProperty(data_source='magpie', features=features, stats=stats)
    return featurizer.featurize_dataframe(df, col_id='composition', ignore_errors=True)