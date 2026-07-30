import json
import numpy as np
import os

np.random.seed(42)

def generate_synthetic_series():
    data = []
    noise_levels = [0.1, 0.5, 1.0, 2.0]
    lengths = [30, 40, 50]
    
    id_counter = 0
    for length in lengths:
        for noise in noise_levels:
            for trend_type in ['constant', 'linear', 'sine']:
                for i in range(10): # 10 samples per configuration
                    if trend_type == 'constant':
                        base = np.ones(length) * np.random.uniform(5, 15)
                    elif trend_type == 'linear':
                        slope = np.random.uniform(-0.2, 0.2)
                        base = np.linspace(10, 10 + slope * length, length)
                    elif trend_type == 'sine':
                        freq = np.random.uniform(0.05, 0.2)
                        base = 10 + 5 * np.sin(2 * np.pi * freq * np.arange(length))
                    
                    noise_vals = np.random.normal(0, noise, length)
                    series = base + noise_vals
                    
                    record = {
                        "id": id_counter,
                        "length": length,
                        "noise_level": noise,
                        "trend_type": trend_type,
                        "series": series.tolist(),
                        "base": base.tolist()
                    }
                    data.append(record)
                    id_counter += 1
                    
    os.makedirs("/ai-inventor/aii_data/runs/run_nsX47UW7n32-/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/temp/datasets", exist_ok=True)
    out_path = "/ai-inventor/aii_data/runs/run_nsX47UW7n32-/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/temp/datasets/data_out.json"
    with open(out_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {len(data)} time series into {out_path}")

if __name__ == '__main__':
    generate_synthetic_series()
