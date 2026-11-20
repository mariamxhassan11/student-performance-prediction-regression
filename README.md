# Student Performance Index Regression

Educational analytics regression model predicting student academic performance index from study habits and prior scores.

## Project Structure

```text
07_Student_Performance_Index_Regression/
├── student_performance_index_regression_data.csv
├── student_performance_index_regression_pipeline.ipynb
├── app.py
├── best_model.pkl
├── model_metadata.json
├── requirements.txt
└── README.md
```

## Dataset & Features

- **Dataset File:** `student_performance_index_regression_data.csv`
- **Task Type:** `Regression`
- **Target Variable:** `performance_index`
- **Numerical Features (5):** `hours_studied, previous_scores, sleep_hours, sample_question_papers_practiced, attendance_rate`
- **Categorical Features (1):** `extracurricular_activities`

## Model Evaluation Summary

- **Selected Best Model:** `Ridge`

| Metric | Score |
| :--- | :--- |
| `r2` | `0.9131` |
| `mae` | `6.15` |
| `rmse` | `9.97` |

## Quickstart & Deployment

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the Streamlit web application:
   ```bash
   streamlit run app.py
   ```
