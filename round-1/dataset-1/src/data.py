import json
import os

def process_datasets():
    input_path = "/ai-inventor/aii_data/runs/run_nsX47UW7n32-/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/temp/datasets/data_out.json"
    with open(input_path, "r") as f:
        raw_data = json.load(f)
        
    examples = []
    for item in raw_data:
        examples.append({
            "input": json.dumps(item["series"]),
            "output": json.dumps(item["base"]),
            "metadata_id": item["id"],
            "metadata_length": item["length"],
            "metadata_noise_level": item["noise_level"],
            "metadata_trend_type": item["trend_type"]
        })
        
    output_data = {
        "datasets": [
            {
                "dataset": "synthetic_time_series",
                "examples": examples
            }
        ]
    }
    
    out_path = "/ai-inventor/aii_data/runs/run_nsX47UW7n32-/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/full_data_out.json"
    with open(out_path, "w") as f:
        json.dump(output_data, f, indent=2)
    print(f"Saved {len(examples)} examples to {out_path}")

if __name__ == '__main__':
    process_datasets()
