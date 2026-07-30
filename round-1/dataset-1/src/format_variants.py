import json
import os

def generate_variants():
    with open("/ai-inventor/aii_data/runs/run_nsX47UW7n32-/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/full_data_out.json", "r") as f:
        data = json.load(f)
        
    # Preview: first 10 examples per dataset
    preview_data = {
        "datasets": []
    }
    for ds in data["datasets"]:
        preview_data["datasets"].append({
            "dataset": ds["dataset"],
            "examples": ds["examples"][:10]
        })
        
    with open("/ai-inventor/aii_data/runs/run_nsX47UW7n32-/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/preview_data_out.json", "w") as f:
        json.dump(preview_data, f, indent=2)
        
    # Mini: first 3 examples per dataset
    mini_data = {
        "datasets": []
    }
    for ds in data["datasets"]:
        mini_data["datasets"].append({
            "dataset": ds["dataset"],
            "examples": ds["examples"][:3]
        })
        
    with open("/ai-inventor/aii_data/runs/run_nsX47UW7n32-/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/mini_data_out.json", "w") as f:
        json.dump(mini_data, f, indent=2)
        
    print("Generated preview (10 examples) and mini (3 examples) successfully.")

if __name__ == '__main__':
    generate_variants()
