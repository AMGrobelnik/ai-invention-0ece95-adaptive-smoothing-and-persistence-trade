import json
from jsonschema import validate

def validate_output():
    with open("/ai-inventor/aii_data/runs/run_nsX47UW7n32-/3_invention_loop/iter_1/gen_art/gen_art_evaluation_1/schema.json") as f:
        schema = json.load(f)
    with open("/ai-inventor/aii_data/runs/run_nsX47UW7n32-/3_invention_loop/iter_1/gen_art/gen_art_evaluation_1/eval_out.json") as f:
        data = json.load(f)
    validate(instance=data, schema=schema)
    print("Validation successful!")

if __name__ == "__main__":
    validate_output()
