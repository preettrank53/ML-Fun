# Fake Currency Detection Using Deep Learning

## Project Overview
This project focuses on **detecting fake and real Indian currency notes** using deep learning. The goal was to build an end-to-end system that can accurately classify currency images as *real* or *fake*, utilizing both image data and extracted note features.  

The project consists of **four major notebooks**:
1. `01_Base_Model_Training.ipynb` — Builds and trains the base model using transfer learning.
2. `02_Two_Branch_Model_Training.ipynb` — Enhances the model using a two-branch architecture combining image and feature embeddings.
3. `03_Feature_Enhancements.ipynb` — Fine-tunes the base model for improved performance.
4. `04_Attention_Enhanced_Model.ipynb` — Implements attention mechanisms (CBAM) for further performance improvement.

---

## Notebook 1: Base Model Training (`01_Base_Model_Training.ipynb`)

### Objective
To train a baseline convolutional neural network using **MobileNetV2** as a pretrained feature extractor for classifying real vs fake currency notes.

### Key Steps
- Loaded the dataset of real and fake currency images using OpenCV.
- Preprocessed images (resizing to 224×224, normalization, RGB conversion).
- Created TensorFlow datasets for efficient loading and batching.
- Used **MobileNetV2 (ImageNet pretrained)** as a frozen feature extractor.
- Added custom classification layers on top of the base model.
- Trained the model using Adam optimizer with callbacks like EarlyStopping, ModelCheckpoint, and ReduceLROnPlateau.

### Model Summary
- **Architecture:** MobileNetV2 + Dense layers  
- **Input Shape:** (224, 224, 3)  
- **Loss:** Binary Cross-Entropy  
- **Optimizer:** Adam  
- **Best Validation Accuracy:** ~99.06%

### Training Output (Excerpt)
```
Epoch 20/20
187/187 ━━━━━━━━━━━━━━━━━━━━ 10s 44ms/step - accuracy: 0.9991 - loss: 0.0065 - val_accuracy: 0.9906 - val_loss: 0.0322
```

### Model Saved As
- `Models/best_model.h5`

---

## Notebook 2: Two-Branch Model Training (`02_Two_Branch_Model_Training.ipynb`)

### Objective
To improve classification accuracy by integrating both **main image features** and **currency-specific precomputed feature embeddings** into a unified two-branch neural network.

### Key Steps
- Loaded the pretrained base model (`best_model.h5`) and froze its layers.
- Built a **feature extractor** from the last convolutional layer of the base model.
- Precomputed embeddings for all feature images (e.g., watermark, security thread, color patterns) and stored them as `.npy` files.
- Designed a **custom data generator** (`TwoBranchEmbeddingGenerator`) to load both the main image and precomputed embeddings during training.
- Created a **Two-Branch Neural Network**:
  - **Branch 1:** Image branch (MobileNetV2 + dense layers)
  - **Branch 2:** Feature embedding branch (fully connected layers)
  - Combined using concatenation followed by dense layers.
- Trained using similar callbacks as the base model.

### Model Summary
- **Architecture:** Two-Branch CNN (Image + Embedding)  
- **Feature Extractor:** MobileNetV2 (frozen)  
- **Loss:** Binary Cross-Entropy  
- **Optimizer:** Adam  
- **Best Validation Accuracy:** ~98.59%

### Training Output (Excerpt)
```
Epoch 11/15
745/745 ━━━━━━━━━━━━━━━━━━━━ 260s 350ms/step - accuracy: 0.9949 - loss: 0.0158 - val_accuracy: 0.9859 - val_loss: 0.0567
```

### Model Saved As
- `Models/best_two_branch_model.keras`

---

## Notebook 3: Feature Enhancements (`03_Feature_Enhancements.ipynb`)

### Objective
Fine-tune the base MobileNetV2 model to **improve accuracy and generalization**.

### Key Steps
- Loaded the pretrained base model (`best_model.h5`) and unfroze deeper layers for fine-tuning.
- Compiled the model with a **very low learning rate** to prevent catastrophic forgetting.
- Used EarlyStopping, ReduceLROnPlateau, and ModelCheckpoint callbacks.
- Trained the fine-tuned model on the original dataset.
- Visualized training accuracy and loss.

### Model Summary
- **Architecture:** MobileNetV2 (fine-tuned) + Dense layers  
- **Input Shape:** (224, 224, 3)  
- **Loss:** Binary Cross-Entropy  
- **Optimizer:** Adam (low learning rate)  
- **Best Validation Accuracy:** ~99.66%

### Training Output (Excerpt)
```
Epoch 10/10
187/187 ─ 9s 49ms/step - accuracy: 0.9984 - loss: 0.0060 - val_accuracy: 0.9832 - val_loss: 0.0504
```

### Model Saved As
- `Models/fine_tuned_base_model.keras`

---

## Notebook 4: Attention-Enhanced Model (`04_Attention_Enhanced_Model.ipynb`)

### Objective
Further improve model performance using **attention mechanisms** (CBAM) to focus on key regions of currency images.

### Key Steps
- Loaded fine-tuned base model and applied **CBAM blocks** to enhance feature representation.
- Added GlobalAveragePooling and Dense layers after attention.
- Compiled and trained the attention-enhanced model with callbacks.
- Evaluated the model using **accuracy, confusion matrix, precision, recall, f1-score, and ROC-AUC**.
- Achieved robust classification performance with minimal misclassifications.

### Model Summary
- **Architecture:** MobileNetV2 + CBAM + Dense layers  
- **Loss:** Binary Cross-Entropy  
- **Optimizer:** Adam  
- **Evaluation Metrics:** Accuracy, Precision, Recall, F1-score, ROC-AUC  
- **Best Validation Accuracy:** ~98–99%

### Sample Evaluation Output
```
Confusion Matrix:
 [[489  13]
 [ 18 969]]

Classification Report:
               precision    recall  f1-score   support
        Fake       0.96      0.97      0.97       502
        Real       0.99      0.98      0.98       987

ROC-AUC Score: 0.9986
```

### Model Saved As
- `Models/attention_enhanced_model.keras`

---



## Visualizations (To Be Added)
Below plots will be added in future updates:
- Accuracy and Loss curves for both models  
- Confusion Matrix  
- Sample Predictions Visualization  
- ROC-AUC Curve

---

## Repository Structure
```
├── 01_Base_Model_Training.ipynb
├── 02_Two_Branch_Model_Training.ipynb
├── 03_Feature_Enhancements.ipynb
├── 04_Attention_Enhanced_Model.ipynb
├── Models
│   ├── best_model.h5
│   ├── best_two_branch_model.keras
│   ├── fine_tuned_base_model.keras
│   └── attention_enhanced_model.keras
└── README.md
```
---
## Dependencies

- TensorFlow / Keras  
- OpenCV (cv2)  
- NumPy  
- scikit-learn  
- matplotlib  
- tqdm

