import json
from glob import glob


def main():
    try:
        for file_name in glob("**/*.json", recursive=True):
            with open(file_name, "r", encoding="utf-8") as infile:
                file = json.load(infile)

            with open(file_name, "w", encoding="utf-8") as outfile:
                json.dump(file, outfile, indent=2, sort_keys=False, ensure_ascii=True)
                # outfile.write("\n")
                print(f"Pretty print {file_name}")
    except Exception as e:
        print(f"Failed to pretty print {file_name}")
        raise SystemExit(e)


if __name__ == "__main__":
    main()
