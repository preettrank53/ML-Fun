# 🧠 Customer Segmentation using KMeans (RFM Analysis)

This project applies **unsupervised learning** (KMeans clustering) to segment customers based on their **Recency**, **Frequency**, and **Monetary (Totalexpenses)** behavior.


---

## 🚀 Project Workflow

1. Cleaned and preprocessed customer transaction data
2. Removed outliers to improve clustering quality
3. Scaled features using `StandardScaler`
4. Used the **Elbow Method** and **Silhouette Score** to find optimal `k`
5. Applied **KMeans with k-means++** and custom `max_iter`
6. Labeled each cluster based on customer behavior
7. Visualized clusters in 3D and explored distribution per segment

---

## 🧠 Final Cluster Interpretation

| Cluster | Totalexpenses | Frequency | Recency | Label              |
|---------|----------------|-----------|---------|---------------------|
| 0       | Low            | Low       | Medium  | Occasional Shopper |
| 1       | High           | High      | Low     | Loyal High-Value   |
| 2       | Medium         | Medium    | Medium  | Mid-Tier Customer  |
| 3       | Low            | Low       | High    | Lost or Dormant    |

---

## 📁 Files

- `customer_segmentation.ipynb`: Full notebook with plots
- `final_customer_segments_original_values.csv`: Cleaned and labeled data
- `README.md`: This file

---

## 🛠️ Tech Stack

- Python (Pandas, Scikit-learn, Seaborn, Matplotlib)
- Kaggle Notebook

---

## 📌 Business Value

With clear segments identified, businesses can:
- 🎯 Target **loyal customers** for retention
- 🔁 Reactivate **dormant customers**
- 📈 Upsell to **mid-tier** and **occasional** shoppers

---

## 📬 Contact

Created by PreetRank.  
🔗 [LinkedIn](https://www.linkedin.com/in/preet-rank-8999a5284/) | ✉️ [Email](preetrank53@gmail.com)  
