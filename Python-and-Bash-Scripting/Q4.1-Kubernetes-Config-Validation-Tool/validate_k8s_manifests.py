import os
import sys
import argparse
import yaml
import json
from pathlib import Path

def validate_manifest(doc, file_path, doc_index):
    errors = []
    if not isinstance(doc, dict):
        errors.append("Document is not a valid YAML mapping.")
        return errors

    if 'apiVersion' not in doc:
        errors.append("Missing 'apiVersion'")
    if 'kind' not in doc:
        errors.append("Missing 'kind'")
    if 'metadata' not in doc or not isinstance(doc['metadata'], dict):
        errors.append("Missing or invalid 'metadata'")
    elif 'name' not in doc['metadata']:
        errors.append("Missing 'metadata.name'")
    
    return errors

def process_yaml_file(file_path):
    issues = []
    try:
        with open(file_path, 'r') as f:
            docs = list(yaml.safe_load_all(f))
            for i, doc in enumerate(docs):
                errors = validate_manifest(doc, file_path, i)
                if errors:
                    issues.append({
                        "file": str(file_path),
                        "document_index": i,
                        "errors": errors
                    })
    except Exception as e:
        issues.append({
            "file": str(file_path),
            "document_index": None,
            "errors": [f"Failed to parse YAML: {str(e)}"]
        })
    return issues

def main():
    parser = argparse.ArgumentParser(description="Validate Kubernetes YAML manifests.")
    parser.add_argument("directory", help="Path to directory containing YAML files")
    args = parser.parse_args()

    base_path = Path(args.directory)
    if not base_path.is_dir():
        print(json.dumps({"error": f"'{args.directory}' is not a valid directory"}), file=sys.stderr)
        sys.exit(1)

    all_issues = []

    for file in base_path.rglob("*.yaml"):
        all_issues.extend(process_yaml_file(file))
    for file in base_path.rglob("*.yml"):
        all_issues.extend(process_yaml_file(file))

    print(json.dumps({"issues": all_issues}, indent=2))

if __name__ == "__main__":
    main()
