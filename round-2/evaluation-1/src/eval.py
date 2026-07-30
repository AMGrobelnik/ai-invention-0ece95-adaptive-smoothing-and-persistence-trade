import json
import os
import numpy as np
from scipy import stats

def main():
    print("Starting evaluation script with correct schema...")
    
    dep_path = "/ai-inventor/aii_data/runs/run_nsX47UW7n32-/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/full_method_out.json"
    if not os.path.exists(dep_path):
        dep_path = "/ai-inventor/aii_data/runs/run_nsX47UW7n32-/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/mini_method_out.json"
    
    print(f"Loading data from {dep_path}")
    with open(dep_path, 'r') as f:
        data = json.load(f)
        
    all_examples = []
    for ds in data.get("datasets", []):
        all_examples.extend(ds.get("examples", []))
        
    print(f"Loaded {len(all_examples)} examples.")
    
    actuals = []
    ma_preds = []
    naive_preds = []
    
    formatted_examples = []
    for ex in all_examples:
        act = float(ex["output"])
        ma_p = float(ex["predict_moving_average"])
        naive_p = float(ex["predict_naive"])
        
        actuals.append(act)
        ma_preds.append(ma_p)
        naive_preds.append(naive_p)
        
        ma_err = (act - ma_p) ** 2
        naive_err = (act - naive_p) ** 2
        
        formatted_ex = {
            "input": str(ex.get("input", "")),
            "output": str(ex.get("output", "")),
            "metadata_run": ex.get("metadata_run", 0),
            "metadata_step": ex.get("metadata_step", 0),
            "predict_moving_average": str(ex.get("predict_moving_average", "")),
            "predict_naive": str(ex.get("predict_naive", "")),
            "eval_ma_squared_error": float(ma_err),
            "eval_naive_squared_error": float(naive_err)
        }
        formatted_examples.append(formatted_ex)
        
    actuals = np.array(actuals)
    ma_preds = np.array(ma_preds)
    naive_preds = np.array(naive_preds)
    
    ma_errors = (actuals - ma_preds) ** 2
    naive_errors = (actuals - naive_preds) ** 2
    
    ma_mse = float(np.mean(ma_errors))
    naive_mse = float(np.mean(naive_errors))
    ma_rmse = float(np.sqrt(ma_mse))
    naive_rmse = float(np.sqrt(naive_mse))
    ma_mae = float(np.mean(np.abs(actuals - ma_preds)))
    naive_mae = float(np.mean(np.abs(actuals - naive_preds)))
    
    t_stat, p_value = stats.ttest_rel(naive_errors, ma_errors)
    try:
        wilcoxon_stat, wilcoxon_p = stats.wilcoxon(naive_errors - ma_errors)
    except Exception:
        wilcoxon_stat, wilcoxon_p = 0.0, 1.0
        
    metrics_agg = {
        "moving_average_mse": ma_mse,
        "moving_average_rmse": ma_rmse,
        "moving_average_mae": ma_mae,
        "naive_persistence_mse": naive_mse,
        "naive_persistence_rmse": naive_rmse,
        "naive_persistence_mae": naive_mae,
        "mse_reduction": naive_mse - ma_mse,
        "percentage_improvement": float((naive_mse - ma_mse) / naive_mse * 100),
        "paired_t_stat": float(t_stat),
        "paired_t_p_value": float(p_value),
        "wilcoxon_stat": float(wilcoxon_stat),
        "wilcoxon_p_value": float(wilcoxon_p)
    }
    
    evaluation_output = {
        "metrics_agg": metrics_agg,
        "datasets": [
            {
                "dataset": "synthetic_noisy_time_series",
                "examples": formatted_examples
            }
        ]
    }
    
    out_path = "/ai-inventor/aii_data/runs/run_nsX47UW7n32-/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1/eval_out.json"
    print(f"Saving evaluation output to {out_path}")
    with open(out_path, 'w') as f:
        json.dump(evaluation_output, f, indent=2)
        
    print("Evaluation completed successfully.")

if __name__ == "__main__":
    main()
