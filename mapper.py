import yaml
from utils import trajectory_analysis

# Open the configuration file
with open("configs/config.yaml",'r') as file:
    config = yaml.safe_load(file)

def main(config):
    trajectory_analysis.run(config)

if __name__ == "__main__":
    main()