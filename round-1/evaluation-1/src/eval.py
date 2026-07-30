import numpy as np
import json
from scipy import stats

def main():
    np.random.seed(42)
    n_runs = 50
    series_length = 30

    ma_sq_errors = []
    naive_sq_errors = []
    ma_abs_errors = []
    naive_abs_errors = []

    examples = []

    for run in range(n_runs):
        t = np.arange(series_length)
        trend = 0.1 * t
        noise = np.random.normal(0, 1.0, size=series_length)
        series = trend + noise

        for i in range(3, series_length):
            ma_pred = np.mean(series[i-3:i])
            ma_sq_err = float((series[i] - ma_pred) ** 2)
            ma_abs_err = float(abs(series[i] - ma_pred))

            naive_pred = series[i-1]
            naive_sq_err = float((series[i] - naive_pred) ** 2)
            naive_abs_err = float(abs(series[i] - naive_pred))

            ma_sq_errors.append(ma_sq_err)
            ma_abs_errors.append(ma_abs_err)
            naive_sq_errors.append(naive_sq_err)
            naive_abs_errors.append(naive_abs_err)

            ex = {
                "input": f"run_{run}_step_{i}",
                "output": str(series[i]),
                "metadata_run": run,
                "metadata_step": i,
                "predict_ma": float(ma_pred),
                "predict_naive": float(naive_pred),
                "eval_ma_mse": ma_sq_err,
                "eval_naive_mse": naive_sq_err
            }
            examples.append(ex)

    ma_mse = float(np.mean(ma_sq_errors))
    ma_rmse = float(np.sqrt(ma_mse))
    ma_mae = float(np.mean(ma_abs_errors))

    naive_mse = float(np.mean(naive_sq_errors))
    naive_rmse = float(np.sqrt(naive_mse))
    naive_mae = float(np.mean(naive_abs_errors))

    t_stat, t_pval = stats.ttest_rel(ma_sq_errors, naive_sq_errors)
    wilcoxon_stat, wilcoxon_pval = stats.wilcoxon(ma_sq_errors, naive_sq_errors)

    metrics_agg = {
        "ma_mse": ma_mse,
        "ma_rmse": ma_rmse,
        "ma_mae": ma_mae,
        "naive_mse": naive_mse,
        "naive_rmse": naive_rmse,
        "naive_mae": naive_mae,
        "mse_improvement": float(naive_mse - ma_mse),
        "mae_improvement": float(naive_mae - ma_mae),
        "paired_t_statistic": float(t_stat),
        "paired_t_pvalue": float(t_pval),
        "wilcoxon_statistic": float(wilcoxon_stat),
        "wilcoxon_pvalue": float(wilcoxon_pval)
    }

    full_data = {
        "metrics_agg": metrics_agg,
        "datasets": [
            {
                "dataset": "synthetic_time_series",
                "examples": examples
            }
        ]
    }

    out_path = "/ai-inventor/aii_data/runs/run_nsX47UW7n32-/3_invention_loop/iter_1/gen_art/gen_art_evaluation_1/eval_out.json"
    with open(out_path, "w") as f:
        json.dump(full_data, f, indent=2)

    with open("/ai-inventor/aii_data/runs/run_nsX47UW7n32-/3_invention_loop/iter_1/gen_art/gen_art_evaluation_1/full_eval_out.json", "w") as f:
        json.dump(full_data, f, indent=2)

    mini_data = {
        "metrics_agg": metrics_agg,
        "datasets": [
            {
                "dataset": "synthetic_time_series",
                "examples": examples[:10]
            }
        ]
    }
    with open("/ai-inventor/aii_data/runs/run_nsX47UW7n32-/3_invention_loop/iter_1/gen_art/gen_art_evaluation_1/mini_eval_out.json", "w") as f:
        json.dump(mini_data, f, indent=2)

    preview_data = {
        "metrics_agg": {
            "mse_improvement": float(naive_mse - ma_mse)
        },
        "datasets": [
            {
                "dataset": "synthetic_time_series",
                "examples": examples[:2]
            }
        ]
    }
    with open("/ai-inventor/aii_data/runs/run_nsX47UW7n32-/3_invention_loop/iter_1/gen_art/gen_art_evaluation_1/preview_eval_out.json", "w") as f:
        json.dump(preview_data, f, indent=2)

    print("Successfully generated all eval variants with metrics_agg and datasets!")

if __name__ == "__main__":
    main()
