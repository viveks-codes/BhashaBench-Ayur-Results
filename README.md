# BhashaBench-Ayur: Benchmark Results

This repository contains the raw evaluation logs and summary results for **VaidhLlama** and other Ayurvedic LLMs on the **BhashaBench-Ayur** benchmark.

**BhashaBench-Ayur** is a specialized evaluation suite designed to test classical reasoning, physiological logic (*Sharir Kriya*), and clinical application in Ayurveda, distinct from generic medical benchmarks.

## Summary Results (Zero-Shot)

| Model | Parameters | Accuracy (%) | Note |
| :--- | :--- | :--- | :--- |
| **VaidhLLaMA** | **3B** | **41.91%** | **Fine-tuned (Ours)** |
| Llama-3.2-Instruct | 3B | 40.74% | Base Model |
| Gemma-2-Instruct | 2B | 41.00% | Comparable Size |
| Qwen2.5 | 3B | 46.76% | Strong Baseline |
| Gemma-2-Instruct | 27B | 52.17% | Large Model SOTA |
| AyurParam | 2.9B | 28.03% | Previous Attempt |

## File Contents

*   `benchmark_summary.csv`: Aggregated performance metrics for all models.
*   `results_*.csv`: Detailed row-by-row prediction logs for each model run.
    *   Columns: `question`, `correct_answer`, `prediction`, `is_correct`, `subject_domain`, `topic`

## Methodology
All models were evaluated in a **Zero-Shot** setting using valid JSON schema enforcement to ensure parsing reliability.

*   **Metric:** Exact Match (after parsing option keys A/B/C/D).
*   **Prompting:** Standard medical system prompt urging clinical precision.
*   **Infrastructure:** Tested on NVIDIA A6000 Ada (48GB) via vLLM.

## Related Resources
*   **Model Weights:** [Hugging Face (VaidhLLaMA-3.2-3B-Instruct)](https://huggingface.co/Vivekdas/VaidhLLaMA-3.2-3B-Instruct)
*   **Technical Blog:** [VaidhLlama: Engineering Higher Reasoning Density](https://github.com/Vivekdas/VaidhLlama-Blog) *(Link placeholder)*
