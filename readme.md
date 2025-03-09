# **Causal Machine Learning for Adaptive Traffic Signal Timing to Reduce Red Light Running (RLR)**
🚦 **Optimizing Traffic Signal Timing Using Causal Forests to Reduce Red Light Violations by Accounting for Temporal and Spatial Heterogeneity**  

## **📌 Project Overview**
This project applies **Causal Machine Learning (ML) techniques** to dynamically adjust **Traffic Signal Timing (TST)** to minimize **Red Light Running (RLR) incidents**. By leveraging **Causal Forests**, the framework estimates the **Conditional Average Treatment Effect (CATE)** of signal timing adjustments on RLR occurrences while accounting for **time and location heterogeneity**.

### **🔹 Key Contributions**
✅ **Developed a Causal ML-based Adaptive Traffic Signal Timing (TST) Framework**  
✅ **Applied Causal Forests to estimate heterogeneous treatment effects of TST adjustments**  
✅ **Used ATSPM high-resolution event data to model Red Light Running (RLR) probabilities**  
✅ **Implemented an automated system to iteratively adjust TST based on CATE estimates**  

This project is **entirely data-driven** and provides an alternative to traditional **simulation-based traffic control methods**.

---

## **🚀 Methodology**
### **1️⃣ Data Processing & Transformation**
- Extracted **high-resolution Automated Traffic Signal Performance Measures (ATSPM) event logs** from **nine intersections in Hillsborough County, Tampa, FL**.
- Processed **Signal Phasing and Timing (SPaT) data** to define **yellow, and red-clearance intervals**.
- Identified **Red Light Running (RLR) violations** using count detectors.

### **2️⃣ Predicting Red Light Running (RLR) Incidents**
To estimate the probability of **unintentional** RLR (violations during the red-clearance interval), I applied multiple **Machine Learning (ML) models**, including Logistic Regression, Random Forest (RF), Adaptive Boosting (AdaBoost), and eXtreme Gradient Boosting (XGBoost). AdaBoost achieved the highest sensitivity and lowest false alarm rate, making it the optimal choice for predicting RLR likelihood. The predicted probability is expressed as $$/P(RLR_unintentional | X) = f(X; θ) /$$, where $$/ X /$$ represents historical SPaT and traffic features from previous cycles, and f(⋅) is the AdaBoost classifier.

---

### **3️⃣ Causal Inference: Estimating Conditional Average Treatment Effect (CATE)**
To determine how traffic signal timing adjustments impact RLR likelihood, I used **Causal Forests** to estimate **Conditional Average Treatment Effects (CATE)** as $$/ τ(X) = E[Y(1) - Y(0) | X] /$$, where $$/ Y(1) /$$ is the log-odds of RLR occurrence with TST adjustment, $$/ Y(0) /$$ is the log-odds of RLR occurrence without TST adjustment, and $$/ X /$$ represents covariates capturing SPaT and traffic conditions.

---

### **4️⃣ Treatment & Outcome Definitions**
- **Treatment Variables (T)** represent adjustments to **yellow, and red-clearance intervals**.
- **Outcome (Y)** is the log-odds of **unintentional RLR occurrence**.

To isolate the causal impact of TST adjustments, I applied **residualization (orthogonalization)**, modeled as $$/ Y - f̂(W, X) = τ(X) * (T - ĝ(W, X)) + ϵ /$$, where $$/ f̂(W, X) /$$ accounts for confounders, $$/ ĝ(W, X) /$$ models TST assignment, and $$/ τ(X) /$$ estimates the true **causal effect** of **TST adjustments**.

---

### **5️⃣ Translating CATE to Probability Changes**
To convert log-odds impact into probability shifts, we used the sigmoid function, where $$/ P_CATE = exp(τ(X)) / (1 + exp(τ(X))) /$$ and $$/ ΔP = P_CATE - 0.5 /$$. Here, $$/ P_CATE /$$ represents the probability shift from the baseline, and ΔP quantifies how much RLR probability changes per unit TST adjustment.

---

### **6️⃣ Traffic Signal Timing (TST) Adjustment Process**
**Objective:** Iteratively modify **TST parameters** until the **predicted probability of RLR drops below 0.5**.

**Adjustment Process:**
1️⃣ Compute **initial probability of RLR** using **AdaBoost**.  
2️⃣ If $$/ P > 0.5 /$$, compute **$$/ ΔP /$$ using Causal Forest CATE estimates**.  
3️⃣ Modify **TST parameters (e.g., increase yellow duration)**.  
4️⃣ **Re-evaluate probability** after modification.  
5️⃣ **Repeat until $$/ P ≤ 0.5 /$$**.  

🚦 **Example Adjustment Scenario:**  
- **Original TST Settings:** Green = 30s, Yellow = 4s, Red-Clearance = 2s → P(RLR) = 0.62  
- **CATE Estimate:** Increasing yellow by 1s reduces P(RLR) by 0.15.  
- **Updated TST Settings:** Green = 30s, Yellow = 5s, Red-Clearance = 2s → P(RLR) = 0.47 ✅  

---

## **📈 Results & Key Findings**
- **AdaBoost achieved the best RLR prediction accuracy** (highest sensitivity, lowest false alarm rate).  
- **Causal Forests captured heterogeneous treatment effects**, showing that **TST impact varies by intersection and time of day**.  
- **Optimal TST adjustments reduced RLR probability by 22-35%**.  
- **Dynamic adjustments were more effective than static traffic signal plans**.  

---
