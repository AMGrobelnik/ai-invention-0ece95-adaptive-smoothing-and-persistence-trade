# gen_paper_text — test_idea

> Phase: `invention_loop` · round 2 · `gen_paper_text`
> Run: `run_nsX47UW7n32-` — Adaptive Smoothing and Persistence Trade-offs in Short-Horizon Noisy Time Series Forecasting
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_paper_text` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-07-30 10:45:42 UTC

````
<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for related-work positioning and how this field frames a genuinely novel contribution.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>
<previous_paper>
STARTING POINT: This is your paper draft from the previous iteration.

# Introduction\n\nTime series forecasting underpins decision-making in diverse application domains, including economic forecasting, stock market analysis, energy grid telemetry, and industrial equipment health monitoring [1]. In many practical settings, practitioners encounter short-horizon forecasting tasks where historical observations are scarce and corrupted by high-frequency observational noise [2]. Establishing robust baseline models is essential before deploying complex parametric or deep learning architectures [3]. Among foundational baseline models, the naive persistence forecaster—which assumes that the future value will equal the most recent observation—and the moving average forecaster—which computes the unweighted mean of past observations over a sliding window—serve as primary points of comparison [2].\n\nDespite their conceptual simplicity, the precise error trade-offs between naive persistence and moving average smoothing on short, noisy sequences remain a critical baseline benchmark. Naive forecasting is highly responsive to immediate changes but suffers from extreme variance amplification when observation noise is present. Conversely, smoothing methods like the 3-point moving average suppress high-frequency random fluctuations at the cost of potential lag. Understanding the quantitative margin of improvement under controlled Gaussian noise distributions provides foundational insight for statistical modeling.\n\nIn this paper, we conduct a rigorous comparative evaluation of a 3-point moving average forecasting model versus a naive last-value persistence baseline. Using a synthetic dataset generator spanning diverse sequence lengths, trend configurations, and noise levels [ARTIFACT:art_k4m-oBvAqLyv], we evaluate forecasting performance across 100 independent noisy time series paths [ARTIFACT:art_-9wvKstb0T26]. Our main contributions are summarized as follows:\n\n- We establish a rigorous experimental framework for evaluating short-horizon forecasting baselines under controlled additive Gaussian noise (sigma = 1.0) [ARTIFACT:art_k4m-oBvAqLyv].\n- We demonstrate empirically that a 3-point moving average model reduces Mean Squared Error (MSE) from 1.9847 (naive baseline) to 1.3558, achieving a robust performance improvement of 0.6290 [ARTIFACT:art_-9wvKstb0T26].\n- We perform exhaustive statistical significance testing via paired t-tests and Wilcoxon signed-rank tests, establishing that the error reductions achieved by moving average smoothing are highly statistically significant (p < 10^-40) [ARTIFACT:art_PAVwq5tc5rW6].\n\n[FIGURE:fig1]\n\n# Background and Related Work\n\nStatistical time series forecasting has a rich history grounded in classical autoregressive and moving average frameworks [1]. The foundations of linear time series models, popularized by Box et al. [1], emphasize the decomposition of series into trend, seasonal, and irregular components. When observation noise dominates short-horizon sequences, classical smoothing techniques remain indispensable.\n\nIn modern benchmarking literature, such as the M-Competitions [3], simple statistical baselines like naive persistence, simple moving averages, and exponential smoothing serve as foundational yardsticks against which advanced machine learning models are measured. While recent advances in transformer-based and neural time series forecasters have expanded capacity, understanding the fundamental variance-bias trade-offs of basic smoothing versus persistence under noise is vital [2]. Our work directly addresses this by providing exact parametric evaluations on short synthetic series.\n\n# Methodology\n\nTo rigorously evaluate forecasting models under controlled conditions, we formulate a synthetic time series generation and evaluation pipeline [ARTIFACT:art_k4m-oBvAqLyv].\n\n## Synthetic Data Generation\n\nWe generate synthetic time series paths defined by an underlying deterministic trend combined with additive zero-mean Gaussian noise. Formally, a time series y_t for t = 1, ..., T is modeled as:\n\ny_t = f(t) + epsilon_t\n\nwhere f(t) represents the underlying trend configuration (e.g., a linear upward trend f(t) = m * t + c) and epsilon_t ~ N(0, sigma^2) represents observation noise with standard deviation sigma = 1.0. Sequence lengths are set to T in {30, 40, 50}, and evaluation is conducted across 100 independent simulation runs [ARTIFACT:art_-9wvKstb0T26].\n\n## Forecasting Models\n\nWe evaluate two primary baseline forecasting strategies:\n\n1. **Naive Persistence Model**: Predicts that the next time step equals the current observed value:\n\nhat{y}_{t+1}^{naive} = y_t\n\n2. **3-Point Moving Average Model**: Predicts the next value as the unweighted mean of the preceding three observations:\n\nhat{y}_{t+1}^{ma} = (1 / 3) sum_{i=0}^{2} y_{t-i}\n\nEvaluation commences at time step t = 3 to ensure a complete 3-point sliding window history is available [ARTIFACT:art_-9wvKstb0T26].\n\n[FIGURE:fig2]\n\n# Experiments and Results\n\n## Experimental Setup\n\nWe implemented the evaluation pipeline in Python, executing 100 independent simulation runs over synthetic time series paths of length T = 30 with Gaussian noise sigma = 1.0 [ARTIFACT:art_-9wvKstb0T26]. For each time step from t = 3 onward, we recorded the squared errors for both the 3-point moving average and the naive persistence baseline [ARTIFACT:art_-9wvKstb0T26].\n\n## Quantitative Forecasting Performance\n\nTable 1 summarizes the core forecasting error metrics comparing the 3-point moving average against the naive persistence baseline across all evaluation runs [ARTIFACT:art_PAVwq5tc5rW6].\n\n| Forecasting Method | Mean Squared Error (MSE) | Root Mean Squared Error (RMSE) | Mean Absolute Error (MAE) |\n| :--- | :--- | :--- | :--- |\n| Naive Persistence Baseline | 1.9847 | 1.4088 | 1.1245 |\n| 3-Point Moving Average | **1.3558** | **1.1644** | **0.9312** |\n| **Error Reduction / Improvement** | **+0.6290** | **+0.2444** | **+0.1933** |\n\nAs reported in Table 1, the 3-point moving average achieves an MSE of **1.3558**, substantially outperforming the naive baseline MSE of **1.9847**, yielding an error reduction of **0.6290** (a 31.7% relative reduction in MSE) [ARTIFACT:art_-9wvKstb0T26]. Similar improvements are observed in RMSE (1.1644 vs 1.4088) and MAE (0.9312 vs 1.1245) [ARTIFACT:art_PAVwq5tc5rW6].\n\n[FIGURE:fig3]\n\n## Statistical Significance and Robustness\n\nTo verify that the observed performance gains are not artifacts of random sampling fluctuations, we conducted paired hypothesis tests. Both the paired t-test and the Wilcoxon signed-rank test yielded p-values well below 10^-40 (p < 10^-40) [ARTIFACT:art_PAVwq5tc5rW6]. This confirms that smoothing over a 3-point window provides a statistically highly significant advantage in suppressing observation noise over naive persistence [ARTIFACT:art_PAVwq5tc5rW6].\n\n# Discussion\n\nOur empirical findings confirm the central hypothesis: smoothing short, noisy time series with a 3-point moving average significantly outperforms naive last-value forecasting. When observation noise (sigma = 1.0) corrupts a sequence, naive persistence projects the noise directly into the one-step-ahead forecast, thereby amplifying variance. In contrast, the sliding window average dampens high-frequency noise variance by a factor proportional to the window size, leading to superior predictive accuracy [ARTIFACT:art_-9wvKstb0T26].\n\n## Limitations\n\nWhile our study provides rigorous statistical validation under controlled synthetic conditions, several limitations should be noted:\n\n1. **Fixed Window Size**: We evaluated a fixed window size of K = 3. While optimal for short sequences, varying noise levels or trend velocities may require adaptive or larger window sizes [ARTIFACT:art_k4m-oBvAqLyv].\n2. **Synthetic Data Assumption**: Our evaluation focused on linear trends with additive Gaussian noise. Real-world series often exhibit non-stationary behaviors, structural breaks, and non-Gaussian error distributions [1].\n\n# Conclusion\n\nIn this paper, we evaluated the performance trade-offs between a 3-point moving average forecasting model and a naive last-value persistence baseline on short, noisy synthetic time series. Our empirical results demonstrate that moving average smoothing reduces Mean Squared Error from 1.9847 to 1.3558 (p < 10^-40), proving the efficacy of local smoothing under Gaussian noise. Future work will investigate adaptive window selection and non-stationary time series domains.\n\n# References\n\n[1] G. E. Box, G. M. Jenkins, G. C. Reinsel, and G. M. Ljung, *Time series analysis: forecasting and control*. John Wiley \\& Sons, 2015.\n[2] R. J. Hyndman and G. Athanasopoulos, *Forecasting: principles and practice*. OTexts, 2018.\n[3] S. Makridakis, E. Spiliotis, and V. Assimakopoulos, "The M4 Competition: 100,000 time series and 61 forecasting methods," *International Journal of Forecasting*, vol. 36, no. 1, pp. 54--74, 2020.\n
</previous_paper>

<reviewer_feedback>
STEP 1 — REVIEW: A reviewer evaluated the previous paper draft above and produced this feedback.

- [MAJOR] (novelty) Comparing a 3-point moving average to a naive persistence baseline is a textbook exercise in elementary signal processing and time series analysis. The variance reduction property of moving averages is analytically derivable and well-documented in classical literature.
  Action: Refocus the paper around adaptive window sizing or dynamic noise regimes, moving beyond the trivial static K=3 comparison.
- [MAJOR] (scope) The evaluation is restricted to a single fixed window size (K=3) and a single noise level (sigma=1.0) in the primary results table, despite the synthetic data generator supporting broader parameter sweeps.
  Action: Include a comprehensive phase diagram or sensitivity analysis matrix showing performance across varying K in {1, 3, 5, 10} and sigma in {0.1, 0.5, 1.0, 2.0}.
- [MINOR] (evidence) The comparison lacks broader classical baselines such as Simple Exponential Smoothing (SES) with optimized smoothing parameter alpha, which is the standard baseline in M-competitions.
  Action: Add Simple Exponential Smoothing (SES) as an additional baseline alongside naive persistence and moving average.
</reviewer_feedback>

<pipeline_steps>
STEP 2 — STRATEGY: The pipeline's strategy generator (gen_strat) read the reviewer feedback
and designed a new research strategy to address the critiques.

STEP 3 — PLANNING: The planner (gen_plan) turned the strategy into concrete artifact plans —
specific experiments, datasets, or research tasks to execute.

STEP 4 — EXECUTION: The executor (gen_art) ran those plans and produced the new artifacts
shown in <new_artifacts_this_iteration> below.
</pipeline_steps>

<hypothesis>
STEP 5 — HYPOTHESIS UPDATE: The hypothesis was revised based on evidence from previous iterations.

kind: hypothesis
title: Adaptive Window Moving Average Forecasting
hypothesis: >-
  Adaptive moving average window sizes and Simple Exponential Smoothing (SES) outperform static 3-point moving averages and
  naive persistence across diverse noise regimes and non-stationary short synthetic time series.
motivation: >-
  Understanding the baseline performance trade-offs between smoothing methods and naive persistence models on short noisy
  sequences is fundamental for time series forecasting.
assumptions:
- >-
  The synthetic series exhibits a stationary or slowly varying underlying trend with additive Gaussian noise.
- >-
  The window size of 3 is optimal or competitive for capturing short-term local trends without excessive lag.
investigation_approach: >-
  Generate synthetic time series data, compute both 3-point moving average and naive last-value forecasts across multiple
  runs, and compare their mean squared errors.
success_criteria: >-
  The 3-point moving average achieves a lower average mean squared error than the naive last-value forecast across the synthetic
  series evaluation runs.
related_works:
- >-
  Standard time series forecasting benchmarks comparing simple moving averages to persistence models.
inspiration: Classical statistical forecasting baselines.
terms:
- term: Moving Average
  definition: >-
    A calculation used to analyze data points by creating a series of averages of different subsets of the full data set.
- term: Naive Forecast
  definition: >-
    A forecasting method that assumes the next period's value will be equal to the current period's observed value.
summary: >-
  Testing whether a 3-point moving average beats a naive last-value forecast on a short synthetic series.
_relation_rationale: >-
  Broadening from static K=3 to adaptive window sizing and SES across dynamic noise regimes.
_confidence_delta: increased
_key_changes:
- >-
  Extended scope from static K=3 to dynamic window sizes (K in {1, 3, 5, 10}) and noise regimes (sigma in {0.1, 0.5, 1.0,
  2.0}).
- Added Simple Exponential Smoothing (SES) as an additional classical baseline.
- Focused on adaptive/parameterized smoothing performance under varying noise.
relation_type: evolution
</hypothesis>

<all_artifacts>
FULL EVIDENCE BASE: All 5 research artifacts across all iterations.

--- Item 1 ---
id: art_k4m-oBvAqLyv
type: dataset
title: Synthetic Time Series Dataset Generator
summary: >-
  This artifact generates a comprehensive and robust synthetic time series dataset specifically designed for rigorously evaluating
  and comparing forecasting models such as moving average against naive last-value baselines. It produces 360 individual time
  series instances featuring diverse characteristics, including varying sequence lengths (30, 40, and 50 time steps), multiple
  additive Gaussian noise standard deviations (0.1, 0.5, 1.0, and 2.0), and distinct underlying trend configurations (constant
  stationary levels, linear trends, and sinusoidal wave oscillations). The generated data is meticulously formatted and structured
  into full, preview, and mini JSON variants adhering strictly to the required schema standards, ensuring seamless integration
  into downstream experiment pipelines and robust performance benchmarking.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_nsX47UW7n32-/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 2 ---
id: art_-9wvKstb0T26
type: experiment
title: Moving Average vs Naive Forecast Evaluation
summary: >-
  This experiment evaluates the forecasting performance of a 3-point moving average versus a naive persistence (last-value)
  baseline across 100 synthetic noisy time series. Results show that smoothing via moving average reduces mean squared error
  (MSE) from 1.9847 to 1.3558, demonstrating the benefit of smoothing under Gaussian noise. Time series forecasting is a critical
  component of many predictive modeling tasks across finance, economics, weather forecasting, and industrial monitoring. When
  data is corrupted by observation noise or short-term random fluctuations, naive baseline forecasters that simply project
  the most recent observation forward can suffer from high variance and poor predictive accuracy. In contrast, moving average
  models smooth out high-frequency noise by aggregating past observations over a fixed sliding window. To rigorously test
  this hypothesis, we generated 100 synthetic time series paths, each spanning 30 time steps, incorporating a deterministic
  linear upward trend combined with additive zero-mean Gaussian noise of standard deviation 1.0. For every time step starting
  from index 3, we computed both the 3-point moving average prediction and the naive persistence prediction, recording the
  squared errors for each method across all runs and evaluation points. Our empirical findings confirm that the 3-point moving
  average achieves a substantially lower mean squared error of 1.3558 compared to 1.9847 for the naive persistence baseline,
  yielding a robust error reduction and performance improvement of 0.6290. These results validate the efficacy of moving average
  smoothing in mitigating random noise in short-horizon time series forecasting scenarios.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_nsX47UW7n32-/3_invention_loop/iter_1/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 3 ---
id: art_PAVwq5tc5rW6
type: evaluation
title: Moving Average vs Naive Forecast Evaluation
summary: >-
  This evaluation artifact provides a rigorous, comprehensive statistical comparison and robustness analysis between a 3-point
  moving average forecasting method and a naive last-value baseline across multiple synthetic time series. Specifically, we
  evaluate model predictions over 100 independent synthetic series featuring linear trends and additive Gaussian noise, computing
  core error metrics including Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and Mean Absolute Error (MAE). To
  ensure statistical rigor and verify performance differences, we conduct paired hypothesis tests including the paired t-test
  and Wilcoxon signed-rank test, both of which confirm highly statistically significant error reductions (p < 1e-40). All
  pipeline evaluation outputs are thoroughly validated against strict JSON schemas and provided in full, mini, and preview
  formats to facilitate downstream synthesis in the paper writing phase.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_nsX47UW7n32-/3_invention_loop/iter_1/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json

--- Item 4 ---
id: art_V5FD1CB4IH2g
type: experiment
title: Adaptive Moving Average and SES Forecasting
summary: >-
  This research artifact rigorously evaluates adaptive moving average models across multiple window lengths (K in {1, 3, 5,
  10}) and Simple Exponential Smoothing (SES) models with various smoothing parameter values (alpha in {0.2, 0.5, 0.8}) against
  standard naive last-value persistence baselines. Utilizing a robust dataset of 360 synthetic time series instances featuring
  diverse characteristics—such as varying sequence lengths, multiple additive Gaussian noise standard deviations, and distinct
  trend configurations—we perform rolling and recursive 1-step ahead forecasting evaluations. We compute comprehensive performance
  metrics including Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and Mean Absolute Error (MAE) for each model.
  The experimental findings provide detailed quantitative insights into the trade-offs between smoothing window sizes, exponential
  smoothing memory parameters, and noise robustness in time series forecasting.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_nsX47UW7n32-/3_invention_loop/iter_2/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 5 ---
id: art_Mr8trU24FEjC
type: evaluation
title: Adaptive Moving Average Window Evaluation
summary: >-
  This evaluation artifact provides a comprehensive, rigorous statistical analysis and parameter sensitivity sweep comparing
  moving average smoothing models against naive persistence baselines across noisy synthetic time series. Specifically, we
  load and process 1,350 evaluation points across 100 independent simulation runs, computing primary error metrics including
  Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and Mean Absolute Error (MAE). Our results demonstrate that the
  moving average model achieves an MSE of 1.344 compared to 2.008 for the naive persistence baseline, yielding a substantial
  and statistically significant error reduction of 33.07%. To establish statistical robustness beyond point estimates, we
  perform rigorous hypothesis testing, including paired t-tests (yielding a t-statistic of 11.476 and a highly significant
  p-value of 3.71e-29) and Wilcoxon signed-rank tests (yielding a p-value of 7.17e-26), confirming that the performance gains
  of moving average smoothing over naive projection are highly statistically significant and consistent across realizations.
  Furthermore, we conduct a detailed parameter sensitivity analysis across varying sliding window sizes K (ranging from 1
  to 10), mapping out the complete phase space of predictive error and identifying optimal window configurations that balance
  noise mitigation against lag distortion in short-horizon forecasting scenarios.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_nsX47UW7n32-/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json
</all_artifacts>

<new_artifacts_this_iteration>
NEW THIS ITERATION: These 2 artifacts were created to address the reviewer
feedback. Their findings should be the primary basis for your revisions.

id: art_V5FD1CB4IH2g
summary: >-
  This research artifact rigorously evaluates adaptive moving average models across multiple window lengths (K in {1, 3, 5,
  10}) and Simple Exponential Smoothing (SES) models with various smoothing parameter values (alpha in {0.2, 0.5, 0.8}) against
  standard naive last-value persistence baselines. Utilizing a robust dataset of 360 synthetic time series instances featuring
  diverse characteristics—such as varying sequence lengths, multiple additive Gaussian noise standard deviations, and distinct
  trend configurations—we perform rolling and recursive 1-step ahead forecasting evaluations. We compute comprehensive performance
  metrics including Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and Mean Absolute Error (MAE) for each model.
  The experimental findings provide detailed quantitative insights into the trade-offs between smoothing window sizes, exponential
  smoothing memory parameters, and noise robustness in time series forecasting.
title: Adaptive Moving Average and SES Forecasting
type: experiment

id: art_Mr8trU24FEjC
summary: >-
  This evaluation artifact provides a comprehensive, rigorous statistical analysis and parameter sensitivity sweep comparing
  moving average smoothing models against naive persistence baselines across noisy synthetic time series. Specifically, we
  load and process 1,350 evaluation points across 100 independent simulation runs, computing primary error metrics including
  Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and Mean Absolute Error (MAE). Our results demonstrate that the
  moving average model achieves an MSE of 1.344 compared to 2.008 for the naive persistence baseline, yielding a substantial
  and statistically significant error reduction of 33.07%. To establish statistical robustness beyond point estimates, we
  perform rigorous hypothesis testing, including paired t-tests (yielding a t-statistic of 11.476 and a highly significant
  p-value of 3.71e-29) and Wilcoxon signed-rank tests (yielding a p-value of 7.17e-26), confirming that the performance gains
  of moving average smoothing over naive projection are highly statistically significant and consistent across realizations.
  Furthermore, we conduct a detailed parameter sensitivity analysis across varying sliding window sizes K (ranging from 1
  to 10), mapping out the complete phase space of predictive error and identifying optimal window configurations that balance
  noise mitigation against lag distortion in short-horizon forecasting scenarios.
title: Adaptive Moving Average Window Evaluation
type: evaluation
</new_artifacts_this_iteration>

<data_files>
Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</data_files>

<task>
Write a research paper draft with LaTeX-ready text, BibTeX citations, and figure placeholders.

YOUR TURN (gen_paper_text): Revise the paper.

You are a researcher improving your paper after receiving a conference review.
Take the feedback seriously and make substantive changes, not cosmetic ones.

1. ADDRESS REVIEWER FEEDBACK: For each critique in <reviewer_feedback>, either fix the
   issue in the paper or argue convincingly why it doesn't apply. Major critiques MUST
   be resolved -- they would cause rejection if left unaddressed.
2. USE THE NEW EVIDENCE: The artifacts in <new_artifacts_this_iteration> were created
   specifically to address the reviewer's concerns. Reference their findings to
   strengthen the sections that were flagged as weak.
3. REWRITE, DON'T PATCH: Don't just append new paragraphs. Restructure and rewrite
   the sections the reviewer identified as problematic.
4. MAINTAIN CONSISTENCY: Ensure the paper aligns with the updated hypothesis.
</task>

<figure_instructions>
FIGURE FORMAT: Use [FIGURE:fig_id] markers in paper_text to indicate where each figure goes.
Then provide the full figure specs in the separate `figures` structured output array.
Each figure in the array must have an `id` matching a marker in the text. Set the `aspect_ratio`
field per figure: 21:9 for architecture / pipeline / flow-chart diagrams (the hero figure should
be one of these — place its marker near the END of the Introduction so it floats to the top of
page 2), 16:9 for comparisons / multi-panel results, 4:3 for dense charts, 1:1 for heatmaps /
confusion matrices / scatter plots.

Example in paper_text:
  "...our method achieves state-of-the-art results as shown below.\n\n[FIGURE:fig3]\n\nThe results demonstrate..."

Example in figures array (results comparison):
  {"id": "fig3", "title": "Performance Comparison", "caption": "Comparison of geometric mean query latency across optimizers.", "image_gen_detailed_description": "Grouped bar chart. X-axis: model names. Y-axis: latency (seconds, 0-5). Values: PostgreSQL=4.6s (red), Bao=2.8s (blue), RLQOpt=2.0s (green). Error bars +/-0.3-0.8. Sans-serif font, white background.", "aspect_ratio": "16:9", "summary": "Compares latency across optimizers"}

Example in figures array (architecture diagram, hero):
  {"id": "fig1", "title": "System Architecture", "caption": "End-to-end pipeline: encoder feeds latents into the planner, which queries the value head before emitting actions.", "image_gen_detailed_description": "Horizontal flow diagram, left to right. Five labeled boxes: 'Input' (gray), 'Encoder' (blue), 'Latent (z, 256-dim)' (light blue, narrow), 'Planner' (green), 'Action Head' (orange). Arrows labeled with shapes. Value head as separate green box below 'Planner', bidirectional arrow. Sans-serif font, clean white background, no 3D.", "aspect_ratio": "21:9", "summary": "Hero architecture diagram"}

CRITICAL: Before writing figure specs, look through artifact workspace output files (*_out.json)
and code to find ALL the exact values. The figure generator cannot read files — every exact number
and value MUST be in the image_gen_detailed_description.
</figure_instructions>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-writing, aii-semscholar-bib.
TODO 2. LITERATURE REVIEW: Use web search tools to research the landscape — search key terms from
<hypothesis> and <all_artifacts>. Then use aii_semscholar_bib__fetch to batch-fetch real
BibTeX entries. Build a comprehensive Related Work section. Do NOT fabricate entries.
TODO 3. READ ARTIFACTS: Before writing each section, READ the relevant artifact source code, output
files, and data in the workspace. Extract concrete implementation details, technical innovations,
algorithmic specifics, and quantitative results. Do NOT write surface-level descriptions.

ARTIFACT REFERENCES: When you reference results, methodology, or findings from a specific artifact,
place an [ARTIFACT:artifact_id] marker inline. These become footnotes linking to the artifact's code
in the GitHub repository (first mention gets a footnote with URL, subsequent mentions are omitted).
Use the exact artifact ID from <all_artifacts>. Place the marker right after the claim it supports.
Example:
  "Our evaluation showed a 15% improvement over baselines [ARTIFACT:art_4f9d2c81ab37]." 
TODO 4. WRITE PAPER: Write the full paper text with [FIGURE:fig_id] markers per <figure_instructions>,
and provide the figure specs in the figures array. Cite with numeric references [1], [2], etc.
At the end of the paper text, include a full bibliography section. Do NOT compile LaTeX or generate
actual image/figure files. Your ONLY output is the structured JSON.
</todos><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_nsX47UW7n32-/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_nsX47UW7n32-/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "FigureSpec": {
      "description": "Figure specification \u2014 structured output from paper writing agent.\n\nThe LLM fills these as a list in PaperText.figures.\nLater converted to Figure objects for viz gen.",
      "properties": {
        "id": {
          "description": "Figure ID matching the [FIGURE:id] marker in paper_text (e.g., 'fig1')",
          "title": "Id",
          "type": "string"
        },
        "title": {
          "description": "Figure title in plain, everyday language \u2014 short and jargon-free. Aim for about 4-8 words (~40 characters).",
          "title": "Title",
          "type": "string"
        },
        "caption": {
          "description": "LaTeX figure caption \u2014 appears below the figure in the paper. Should describe what the figure shows and highlight key takeaways.",
          "title": "Caption",
          "type": "string"
        },
        "image_gen_detailed_description": {
          "description": "Detailed image generation prompt \u2014 axes, labels, ALL numeric values, colors, aspect ratio, layout. The image generator cannot read files; this is its ONLY input.",
          "title": "Image Gen Detailed Description",
          "type": "string"
        },
        "summary": {
          "description": "Brief summary of what this figure communicates",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "id",
        "title",
        "caption",
        "image_gen_detailed_description",
        "summary"
      ],
      "title": "FigureSpec",
      "type": "object"
    }
  },
  "description": "Paper text \u2014 structured output from paper writing agent.\n\nStructured output fields (LLMPrompt + LLMStructOut):\n- title, abstract, paper_text, figures, summary\n\npaper_text contains [FIGURE:fig_id] markers for positioning.\nfigures contains the full specs as structured objects.\n\nMetadata fields (plain, set by pipeline code):\n- id",
  "properties": {
    "title": {
      "description": "Paper title \u2014 clear, plain-language, and short so a non-expert understands the main contribution at a glance. Aim for about 6-10 words; avoid jargon and acronyms.",
      "title": "Title",
      "type": "string"
    },
    "abstract": {
      "description": "Paper abstract",
      "title": "Abstract",
      "type": "string"
    },
    "paper_text": {
      "description": "Full paper body text with markdown section headers (# Introduction, # Methods, # Results, # Discussion, # Conclusion). Use [FIGURE:fig_id] markers (e.g. [FIGURE:fig1]) to indicate where each figure should appear.",
      "title": "Paper Text",
      "type": "string"
    },
    "figures": {
      "description": "List of figure specifications. Each must have an id matching a [FIGURE:id] marker in paper_text.",
      "items": {
        "$ref": "#/$defs/FigureSpec"
      },
      "title": "Figures",
      "type": "array"
    },
    "summary": {
      "description": "Brief summary of the paper's main contribution and findings",
      "title": "Summary",
      "type": "string"
    }
  },
  "required": [
    "title",
    "abstract",
    "paper_text",
    "summary"
  ],
  "title": "PaperText",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_nsX47UW7n32-/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-07-30 10:45:42 UTC

```
Test whether a 3-point moving average beats a naive last-value forecast on a short synthetic series. Keep the investigation minimal.
```

### [3] SKILL-INPUT — aii-paper-writing · 2026-07-30 10:45:44 UTC

The agent loaded the **aii-paper-writing** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-paper-writing
description: Academic paper writing guidance for AI research. Covers paper structure, figure placeholders, bibliography building with Semantic Scholar, and citation rules. Does NOT cover LaTeX compilation or figure file generation — see aii-paper-to-latex for that.
---

## Technical Papers

Guidance for the standard "technical paper" format: propose a method/system/framework, evaluate it experimentally, report results. This is the main track at most CS venues (NeurIPS, ICML, ICLR, ACL, AAAI, etc.). Does NOT cover: pure theory/formal proofs, survey papers, position papers, or dataset/benchmark papers — those have different structures.

### Paper Structure

Target 6-8 pages. Use formal academic language, third person. Support claims with evidence from artifacts.

#### Rough Page Budget (8-page paper)

| Section | Pages | Notes |
|---|---|---|
| Abstract | 0.3 | Problem, approach, key result |
| Introduction | 1.0-1.5 | The most important section |
| Related Work | 0.5-1.0 | Beginning or end (see below) |
| Methods | 1.5-2.0 | Architecture fig on page 1 |
| Experiments | 1.5-2.0 | Setup + results + ablations |
| Discussion | 0.5-1.0 | Limitations go here |
| Conclusion | 0.3-0.5 | Do not repeat the abstract |
| References | 0.5-1.0 | Not counted in page limit |

**Critical rule**: A clear new technical contribution must be articulated by page 3 (quarter of the paper). If the reader doesn't know what you did by then, you've lost them.

#### Section Details

**Abstract** (150-250 words): State the problem, your approach, and the main results. Be factual and comprehensive. Do not repeat the abstract word-for-word later in the paper.

**Introduction** — Follow this 5-paragraph structure:

1. **What is the problem?** Define the task concretely.
2. **Why is it interesting and important?** Real-world impact, scale.
3. **Why is it hard?** Why do naive approaches fail?
4. **Why hasn't it been solved before?** What's wrong with prior solutions? How does yours differ?
5. **What are the key components of your approach and results?** Include specific limitations.

End with a "Summary of Contributions" subsection — bullet list of contributions with section references. This doubles as an outline, saving space.

**Related Work** — Placement decision:
- **Beginning** (Section 2): If it can be short yet detailed, or if you need a strong defensive stance against prior work early.
- **End** (before Conclusions): If comparisons require your technical content, or if it can be summarized briefly in the Introduction. Can be titled "Discussion and Related Work."

**Methods/Approach**: Every section tells a story — the story of the results, NOT the story of how you arrived at them. Use top-down description: readers should see where the material is going and be able to skip ahead. Move gory details to appendices.

**Experiments**: Setup (datasets, metrics, baselines) → main results → ablations → analysis. Every claim needs quantitative evidence.

**Discussion**: Interpret results, compare to prior work, state limitations honestly. Limitations should be specific and actionable, not vague disclaimers.

**Conclusion**: Short summarizing paragraph. Do NOT repeat material from the Abstract or Introduction. Make original claims more concrete (e.g., reference quantitative results). Include future work as bullet list — if actively pursuing follow-up, say so to mark territory.

#### Writing Quality Rules

- Define all notation/terminology before use, only once. Group global definitions in Preliminaries.
- Do NOT use nonreferential "this", "that", "these", "it". Always specify the referent. BAD: "This is important because..." GOOD: "This accuracy gap is important because..."
- Do NOT use "etc." unless remaining items are completely obvious. BAD: "We measure volatility, scalability, etc." GOOD: "We measure volatility and scalability."
- Do NOT write "for various reasons" — state the actual reasons.
- "That" is defining, "which" is nondefining. "The algorithms that are easy to implement" vs "The algorithms, which are easy to implement."
- Use italics for definitions and quotes, not for emphasis. Context alone should provide emphasis.

### Figure Format

Figures use a hybrid marker + structured array approach. ALL figures are generated by a separate pipeline step using an AI image model — your `image_gen_detailed_description` is the ONLY input that model sees. It cannot read files or access data. Do NOT generate actual image files yourself (no matplotlib, no PIL, no image generation scripts).

**In paper_text**: Place `[FIGURE:fig_id]` markers where figures should appear.

**In figures array**: Provide full specs as structured objects with these fields:
- `id` — matches the `[FIGURE:id]` marker in paper_text
- `title` — short descriptive title
- `caption` — LaTeX caption that appears below the figure in the paper
- `image_gen_detailed_description` — detailed prompt for the image generator (axes, ALL values, colors, layout)
- `summary` — brief summary of what the figure communicates

Example in paper_text:
```
...our method achieves state-of-the-art results as shown below.

[FIGURE:fig_1]

The results in Figure 1 demonstrate...
```

Example figure spec in figures array:
```json
{"id": "fig_1", "title": "Performance Comparison", "caption": "Comparison of geometric mean query latency across optimizers on JOB benchmark. RLQOpt achieves 2.3x speedup over PostgreSQL.", "image_gen_detailed_description": "Grouped bar chart. X-axis: model names. Y-axis: accuracy (0.0-1.0). Values: ModelA=0.847, ModelB=0.762, Baseline=0.531. Error bars with std: 0.02, 0.03, 0.05. Sans-serif font, white background.", "summary": "Compares accuracy of proposed methods vs baseline."}
```

Every marker in text MUST have a matching figure in the array, and vice versa.

#### Data Precision Requirement

`image_gen_detailed_description` MUST include exact numbers from artifact output files. Read the actual output files before writing figure specs.

- BAD: "Compare accuracy metrics across configurations"
- GOOD: "Grouped bar chart. X-axis: model names. Y-axis: accuracy (0.0-1.0). Values: K=3: 0.765, K=5: 0.729, Baseline: 0.121."

#### Figure vs Table Decision

Do NOT create figures for tabular data (rows/columns of text or numbers). Use `\begin{table}` in LaTeX instead. Figures are for actual visualizations only (charts, plots, diagrams).

#### Figure Placement Strategy

Be intentional with figure ordering. The architectural/method overview figure explaining the proposed approach MUST appear early — in the Introduction or at the start of Methods — so readers can immediately orient themselves. Readers skim papers top-down; if the first figure they see is a results bar chart, they have no mental model for interpreting it.

Recommended ordering:
1. **Architecture/method diagram** — Introduction or early Methods (so readers understand the approach before diving into details)
2. **Conceptual/analogy figures** — Introduction or Methods (to build intuition)
3. **Results figures** (bar charts, line plots, scatter plots) — Results section
4. **Analysis/ablation figures** — Discussion or later Results

#### Guidelines

- Plan 3-6 figures total across the paper
- Place [FIGURE:fig_id] markers INLINE where referenced in text
- Include axes, labels, ALL numeric values in figure descriptions
- Both data-driven figures (bar charts, line plots) and conceptual diagrams (architecture, flowcharts)
- Be as detailed as possible in descriptions: specify aspect ratio, preferred colors, all data values, axis labels, ranges, legend entries, and any other visual details. The more specific the description, the better the generated figure

### Bibliography with Semantic Scholar

Build `./references.bib` using the aii-semscholar-bib skill (real BibTeX from Semantic Scholar):

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Call `aii_semscholar_bib__fetch` with the full list in one batch
3. Write the returned .bib text into `./references.bib`

Rules:
- Do NOT fabricate BibTeX entries — always fetch from Semantic Scholar
- If a paper isn't found (very recent preprint), write the entry manually as fallback
- Use `\bibliography{references}` and `\bibliographystyle{plainnat}`
- Do NOT use inline `thebibliography` environment

### Citation Format (for Research Artifacts)

When writing research with numbered citations:

1. Every factual claim MUST have a numbered citation: `[1]`, `[2]`, `[1, 3]`, etc.
2. Each source in the "sources" array MUST have an "index" field
3. The index MUST EXACTLY MATCH citation numbers in the text
4. NEVER cite a number without a matching source index
5. Example: "LLMs show 40% improvement with multi-agent collaboration [1]."
````
