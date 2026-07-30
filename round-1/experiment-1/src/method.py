import numpy as np
import json

def main():
    np.random.seed(42)
    n_runs = 50
    series_length = 30

    examples = []

    for run in range(n_runs):
        t = np.arange(series_length)
        trend = 0.1 * t
        noise = np.random.normal(0, 1.0, size=series_length)
        series = trend + noise

        for i in range(3, series_length):
            ma_pred = float(np.mean(series[i-3:i]))
            naive_pred = float(series[i-1])
            actual = float(series[i])

            examples.append({
                "input": f"Run {run}, step {i}, history: {list(series[i-3:i])}",
                "output": f"{actual}",
                "metadata_run": run,
                "metadata_step": i,
                "predict_moving_average": f"{ma_pred}",
                "predict_naive": f"{naive_pred}"
            })

    ma_errors = []
    naive_errors = []
    for ex in examples:
        actual = float(ex["output"])
        ma_pred = float(ex["predict_moving_average"])
        naive_pred = float(ex["predict_naive"])
        ma_errors.append((actual - ma_pred) ** 2)
        naive_errors.append((actual - naive_pred) ** 2)

    ma_mse = float(np.mean(ma_errors))
    naive_mse = float(np.mean(naive_errors))
    improvement = float(naive_mse - ma_mse)

    dataset_obj = {
        "datasets": [
            {
                "dataset": "synthetic_noisy_time_series",
                "examples": examples
            }
        ],
        "aggregate_metrics": {
            "ma_mse": ma_mse,
            "naive_mse": naive_mse,
            "improvement": improvement
        }
    }

    with open('/ai-inventor/aii_data/runs/run_nsX47UW7n32-/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/method_out.json', 'w') as f:
        json.dump(dataset_obj, f, indent=2)

    with open('/ai-inventor/aii_data/runs/run_nsX47UW7n32-/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/full_method_out.json', 'w') as f:
        json.dump(dataset_obj, f, indent=2)

    mini_dataset_obj = {
        "datasets": [
            {
                "dataset": "synthetic_noisy_time_series",
                "examples": examples[:10]
            }
        ],
        "aggregate_metrics": {
            "ma_mse": ma_mse,
            "naive_mse": naive_mse,
            "improvement": improvement
        }
    }

    with open('/ai-inventor/aii_data/runs/run_nsX47UW7n32-/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/mini_method_out.json', 'w') as f:
        json.dump(mini_dataset_obj, f, indent=2)

    with open('/ai-inventor/aii_data/runs/run_nsX47UW7n32-/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/preview_method_out.json', 'w') as f:
        json.dump(mini_dataset_obj, f, indent=2)

    print(f"Generated {len(examples)} examples.")
    print(f"MA MSE: {ma_mse:.4f}, Naive MSE: {naive_mse:.4f}")

if __name__ == '__main__':
    main()
