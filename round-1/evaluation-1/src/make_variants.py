import json

def main():
    with open("/ai-inventor/aii_data/runs/run_nsX47UW7n32-/3_invention_loop/iter_1/gen_art/gen_art_evaluation_1/eval_out.json") as f:
        data = json.load(f)

    # full
    with open("/ai-inventor/aii_data/runs/run_nsX47UW7n32-/3_invention_loop/iter_1/gen_art/gen_art_evaluation_1/full_eval_out.json", "w") as f:
        json.dump(data, f, indent=2)

    # mini (subset of metrics)
    mini_data = {
        "metrics": {
            "ma_mse": data["metrics"]["ma_mse"],
            "naive_mse": data["metrics"]["naive_mse"],
            "mse_improvement": data["metrics"]["mse_improvement"]
        }
    }
    with open("/ai-inventor/aii_data/runs/run_nsX47UW7n32-/3_invention_loop/iter_1/gen_art/gen_art_evaluation_1/mini_eval_out.json", "w") as f:
        json.dump(mini_data, f, indent=2)

    # preview
    preview_data = {
        "mse_improvement": data["metrics"]["mse_improvement"]
    }
    with open("/ai-inventor/aii_data/runs/run_nsX47UW7n32-/3_invention_loop/iter_1/gen_art/gen_art_evaluation_1/preview_eval_out.json", "w") as f:
        json.dump(preview_data, f, indent=2)

if __name__ == "__main__":
    main()
