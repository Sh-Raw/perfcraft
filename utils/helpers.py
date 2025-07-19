import yaml
import logging

logging.basicConfig(level=logging.INFO)

def load_test_config(file_path="configs/test.yaml"):
    """
    Load test configuration from a YAML file.
    :param file_path: path to the YAML config file
    :return: dictionary with config values
    """
    try:
        with open(file_path, 'r') as f:
            config = yaml.safe_load(f)
            if not config:
                logging.warning("⚠️ Loaded config is empty. Check the file content.")
            return config
    except FileNotFoundError:
        logging.error(f"❌ Config file not found: {file_path}")
        return {}
    except yaml.YAMLError as e:
        logging.error(f"❌ YAML parse error: {e}")
        return {}
