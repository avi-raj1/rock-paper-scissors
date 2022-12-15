from scripts.turn import Turn
from common.utils import scoring_profile


if __name__ == '__main__':
    # test cases for Turn class
    a, b = Turn('Rock', 'Rock').execute()
    assert(a == scoring_profile['draw'] and b  == scoring_profile['draw'])
    a, b = Turn('Paper', 'Paper').execute()
    assert(a == scoring_profile['draw'] and b == scoring_profile['draw'])
    a, b = Turn('Scissors', 'Scissors').execute()
    assert(a == scoring_profile['draw'] and b == scoring_profile['draw'])
    a, b = Turn('Rock', 'Paper').execute()
    assert(a == scoring_profile['lose'] and b == scoring_profile['win'])
    a, b = Turn('Paper', 'Scissors').execute()
    assert(a == scoring_profile['lose'] and b == scoring_profile['win'])
    a, b = Turn('Scissors', 'Rock').execute()
    assert(a == scoring_profile['lose'] and b == scoring_profile['win'])
    a, b = Turn('Paper', 'Rock').execute()
    assert(a == scoring_profile['win'] and b == scoring_profile['lose'])
    a, b = Turn('Rock', 'Scissors').execute()
    assert(a == scoring_profile['win'] and b == scoring_profile['lose'])
    a, b = Turn('Scissors', 'Paper').execute()
    assert(a == scoring_profile['win'] and b == scoring_profile['lose'])
