import argparse
import json


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--file', default="endjinnfile.json")
args = parser.parse_args()


if __name__ == "__main__":
    with open(args.file) as f:
        sim_params = json.load(f)

