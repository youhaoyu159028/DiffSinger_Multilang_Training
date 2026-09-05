def check_languages(requested, supported):
    missing=sorted(set(requested)-set(supported))
    return {'ok': not missing, 'missing_languages': missing, 'supported_languages': sorted(set(supported))}

def check_phonemes(phonemes, vocabulary):
    missing=sorted(set(phonemes)-set(vocabulary))
    return {'ok': not missing, 'missing_phonemes': missing}
