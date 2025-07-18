import yaml




def load_test_config(file_path):
	with open(file_path, 'r') as f:
		config =yaml.safe_load(f)
	return config

def main():
    config = load_test_config("test.yml")

    print("🚀 Test Configuration:")
    print("----------------------")
    print("Test Name:", config["test_name"])
    print("Host:", config["host"])
    print("Endpoint:", config["endpoint"])
    print("Method:", config["method"])
    print("Payload:", config["payload"])
    print("Users:", config["users"])
    print("Spawn Rate:", config["spawn_rate"])
    print("Duration:", config["duration"], "seconds")

if __name__ == "__main__":
    main()

	