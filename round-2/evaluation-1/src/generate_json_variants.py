import json
import os

def main():
    with open("eval_out.json", "r") as f:
        data = json.load(f)
        
    with open("full_eval_out.json", "w") as f:
        json.dump(data, f, indent=2)
        
    mini_data = {
        "metrics_agg": data.get("metrics_agg"),
        "datasets": [
            {
                "dataset": "synthetic_noisy_time_series",
                "examples": data["datasets"][0]["examples"][:5]
            }
        ]
    }
    with open("mini_eval_out.json", "w") as f:
        json.dump(mini_data, f, indent=2)
        
    preview_data = {
        "metrics_agg": data.get("metrics_agg"),
        "datasets": [
            {
                "dataset": "synthetic_noisy_time_series",
                "examples": data["datasets"][0]["examples"][:2]
            }
        ]
    }
    with open("preview_eval_out.json", "w") as f:
        json.dump(preview_data, f, indent=2)
        
    print("Successfully generated full, mini, and preview JSON files with correct schema.")

if __name__ == "__main__":
    main()
