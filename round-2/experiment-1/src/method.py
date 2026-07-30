import json
import numpy as np

with open('full_data_out.json', 'r') as f:
    data = json.load(f)

dataset_list = data['datasets']
out_datasets = []

for ds in dataset_list:
    ds_name = ds.get('dataset', 'synthetic_time_series')
    examples = ds['examples']
    new_examples = []
    
    for item in examples:
        series = np.array(json.loads(item['input']) if isinstance(item['input'], str) else item['input'])
        
        # We evaluate on the last step or rolling over all steps
        # To match exp_gen_sol_out schema, each example needs input, output, and predict_<method_name>
        # Let's take history = series[:-1], actual = series[-1]
        history = series[:-1]
        actual = series[-1]
        
        f_naive = history[-1]
        
        def get_ma(k, hist):
            if len(hist) < k:
                return np.mean(hist)
            return np.mean(hist[-k:])
            
        f_ma1 = get_ma(1, history)
        f_ma3 = get_ma(3, history)
        f_ma5 = get_ma(5, history)
        f_ma10 = get_ma(10, history)
        
        def get_ses(alpha, hist):
            s = hist[0]
            for val in hist[1:]:
                s = alpha * val + (1 - alpha) * s
            return s
            
        f_ses02 = get_ses(0.2, history)
        f_ses05 = get_ses(0.5, history)
        f_ses08 = get_ses(0.8, history)
        
        ex_out = {
            "input": item['input'],
            "output": str(actual),
            "metadata_id": item.get('metadata_id', 0),
            "predict_naive": str(f_naive),
            "predict_ma_1": str(f_ma1),
            "predict_ma_3": str(f_ma3),
            "predict_ma_5": str(f_ma5),
            "predict_ma_10": str(f_ma10),
            "predict_ses_0.2": str(f_ses02),
            "predict_ses_0.5": str(f_ses05),
            "predict_ses_0.8": str(f_ses08)
        }
        new_examples.append(ex_out)
        
    out_datasets.append({
        "dataset": ds_name,
        "examples": new_examples
    })

output = {
    "status": "success",
    "datasets": out_datasets,
    "summary": "Evaluated moving averages and SES against naive baseline with per-example predictions."
}

def save_all(filename):
    with open(filename, 'w') as f:
        json.dump(output, f, indent=2)

save_all('method_out.json')
save_all('full_method_out.json')

mini_output = {
    "status": "success",
    "datasets": [{
        "dataset": out_datasets[0]["dataset"],
        "examples": out_datasets[0]["examples"][:3]
    }],
    "summary": output["summary"]
}

with open('mini_method_out.json', 'w') as f:
    json.dump(mini_output, f, indent=2)

with open('preview_method_out.json', 'w') as f:
    json.dump(mini_output, f, indent=2)

print("Method executed successfully. All output files generated.")
