from src.utils.config import load_yaml

def test_config(): assert load_yaml('configs/train.yaml')['training']['resume'] is True
