# Customer Segmentation with K-Means (RFM Analysis)

This project uses **unsupervised learning** (K-Means clustering) to segment customers based on **Recency**, **Frequency**, and **Monetary value (TotalExpenses)**.

## Project overview

### Workflow

1. Clean and preprocess customer transaction data
2. Remove outliers to improve clustering quality
3. Scale features using `StandardScaler`
4. Determine an appropriate number of clusters using the **Elbow Method** and **Silhouette Score**
5. Train **K-Means** (k-means++) with a tuned `max_iter`
6. Assign cluster labels based on customer behavior
7. Visualize clusters (including 3D views) and analyze segment distributions

### Cluster interpretation

| Cluster | TotalExpenses | Frequency | Recency | Segment label        |
|--------:|---------------|-----------|---------|----------------------|
| 0       | Low           | Low       | Medium  | Occasional Shopper   |
| 1       | High          | High      | Low     | Loyal High-Value     |
| 2       | Medium        | Medium    | Medium  | Mid-Tier Customer    |
| 3       | Low           | Low       | High    | Lost or Dormant      |

## Repository contents

- `customer_segmentation.ipynb`: End-to-end notebook (preprocessing, modeling, and visualizations)
- `final_customer_segments_original_values.csv`: Cleaned dataset with assigned segments
- `README.md`: Project documentation

## Tech stack

- Python (Pandas, scikit-learn, Seaborn, Matplotlib)
- Jupyter / Kaggle Notebook environment

## Business value

The resulting customer segments can support:

- Retention strategies for loyal, high-value customers
- Re-engagement campaigns for dormant customers
- Upsell and cross-sell targeting for mid-tier and occasional shoppers

## Contact

Created by PreetRank  
LinkedIn: https://www.linkedin.com/in/preet-rank-8999a5284/  
Email: preetrank53@gmail.com
