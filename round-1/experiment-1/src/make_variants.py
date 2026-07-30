import json
import shutil

with open('/ai-inventor/aii_data/runs/run_nsX47UW7n32-/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/method_out.json', 'r') as f:
    data = json.load(f)

with open('/ai-inventor/aii_data/runs/run_nsX47UW7n32-/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/full_method_out.json', 'w') as f:
    json.dump(data, f, indent=2)

with open('/ai-inventor/aii_data/runs/run_nsX47UW7n32-/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/mini_method_out.json', 'w') as f:
    json.dump(data, f)

with open('/ai-inventor/aii_data/runs/run_nsX47UW7n32-/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/preview_method_out.json', 'w') as f:
    json.dump(data, f)
