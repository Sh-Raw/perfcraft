import yaml

def load_test_config(file_path="configs/test.yaml"):
    """
    Load test configuration from a YAML file.

    :param file_path: path to the YAML config file
    :return: dictionary with config values
    """
    try:
        with open(file_path, 'r') as f:
            config = yaml.safe_load(f)
            return config
    except FileNotFoundError:
        print(f"❌ Config file not found: {file_path}")
        return {}
    except yaml.YAMLError as e:
        print(f"❌ YAML parse error: {e}")
        return {}

