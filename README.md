![Alt_Text](https://github.com/KevinNourian/Stroke/blob/main/Image/Stroke.PNG)
# Project File
Open Stroke.ipynb

# Introduction
A stroke, occurs when the blood supply to part of the brain is disrupted or reduced, depriving brain tissue of oxygen and nutrients. This can happen due to a blockage or rupture of a blood vessel. Without prompt medical attention, strokes can cause permanent brain damage or even death. Immediate treatment is crucial to minimize damage and improve outcomes for stroke patients.

It will become evident in this analysis that the data is extremely limited. Predicting a complex disease like a storke with such basic information as marital status or residence is simply laughable. In the end, the only predictor worth really looking at was age, which is the most obvious answer, but lacking better information, this is the best that can be done with this data.

# Dataset
The "Stroke Prediction Dataset" from Kaggle is a dataset designed to predict whether a patient is likely to have a stroke based on various health and demographic factors. It contains several features including demographic information (age, gender), health parameters (hypertension, heart disease), lifestyle factors (smoking status), and medical history  (glucose and BMI levels). The target variable indicates whether a person has had a stroke or not.


# Goal
For this project, I picked recall for evaluating my models. My goal in this analysis is to understand the factors can predict a patient suffering a stroke and to build predictive models for stroke occurrence with a recall score of 75% or higher.Recall measures how well a model identifies all actual positive cases (like patients with a disease). It is the percentage of true positive results out of all the actual positives. For example, if 100 patients truly have a disease and the model correctly identifies 90 of them, the recall is 90%. High recall means the model is good at detecting the condition whenever it is present. 


# Notebooks Folder
This folder contains the various versions of this project. 


# Technical Requirements
1. Perform exploratory data analysis. 
2. Perform statistical inference. 
3. Apply various machine learning models to predict the occurance of stroke. 
4. Provide clear explanations. 
5. Provide suggestions about how the analysis can be improved.


# Standards
**Standard 1:** My standard for an acceptable recall score is 75% or higher .<BR>
**Standard 2:** My significance level (alpha) for all hypothesis tests is 0.05. <BR>
**Standard 3:** My standard for a strong correlation between features is a Pearson correlation coefficient of 0.8 or higher. <BR> 

# Biases
The main bias in this dataset was that it is highly imbalanced. Out of 5,000 patients, there are only 249 who suffered a stroke. This is a good for the patients, but it makes it difficult to build a good predictive model. 

# Conclusions
**The Analysis of the Data:** I reviewed over 5,000 datapoint related to patients with stroke. <br> 
**The Goal of the Project:** The goal of this project was to find a model that could predict if a patient is likely to have a stroke with a recall score of 0.75 or higher.<br>
**Models:** I utilized numerous models and numerous ways to hyperparameter tuning.  I chose two simple models, Logistic Regressin and Support Vector Machines. I chose three boosting classifiers, CAT, LGBM and XGB.<br>
**Encoding:** For categorical data, I tried both Label Encoding and One-Hot Encoding. I did not see significant differences. I chose Label Encoding since the resulting table was more readable.  <br>
**Imputing Missing Data:** For imputing missing data, I tried mean, median, zero and random imputers. I saw no signinficant difference between them in the predictions of my models. I chose Randmo Imputer, since it I thought with such little information about the participants, it makes no sense to make any judgments about their features.  <br>
**Feature Engineering and Hyperparameter Testing:** I tried feature engineering and hyperparameter testing with techniques such as Backward Elimination, SHAP and OPTUNA. Some, I included in this report and some I didn't for sake of brevity. None of the measures I utilized improved resutls significanlty.<br> 
**Support Vector Machines:** For a simple model and using only default hyperparameters, SVC was able to get better or similar results than any other model, including the more complex ones.<br>  
**Boosting Models:** Of the boosting models that I utilized, none of them performed better than SVC.
**Age:** In the end, the only feature that could predict suffering a stroke was age. No other combination of features, including features that I created from other features, was a better predictor than age. This shows the real short comings of the data itself that I mentioned in the secton below: "Suggestions for Improvment."
**Recommendation:** I am not able to make any medical recommendations based on this data. However, some obvious elements that I was sure would contribute to the risk of stroke such as smoking or BMI, turned out to be a very poor predictors. <br> <br>

# Suggestions for Improvement
**Domain Knowledge:** It is best if the data scientist has adequate domain knowledge on the topic of the analysis. I do not have any expertise in the medical field. There may be parts of the data that I have overlooked that may have been important and I may have given importance to parts that may have had little significance. <br>
**More Detailed Data:** The data provide only general information on patients. This information is not adequate to predict a disease as complex as stroke. Information such as family history, genetic markers, blood trace element markers and more are missing in this data. More detailed information could have helped make better predictions. <br>  
**Balance:** The data is heavely imbalanced. Of the more than 5,000 datapoints, only about 300 are related to stroke patients. This, in addition to inadequcy of the data as mentioned above adds to the complexity predictions.  <br>  
**Visualizations:** If I had more time, I would improve on the bar graphs to emphasize certain data by using specific colors.  <br>  
**Functions:** I modularized most of the code in this notebook but not all due to limitation of time.  <br>  
**Statistics:** Continue to improve my statistical knowledge to create better analyses.<br>
**Pandas:** Continue to learn to utilize more optimized Pandas techniques and algorithms.<br>
**Seaborn and Matplotlib:** Continue to improve my knowledge of Seaborn and Matplotlib for creating visualizations. <br>
**Python Code:** Continue to write better and more efficient Python code. <br>
**Clean Code:** Continue to adhere to the principles of writing clean code. <br>
**Readability and Efficiency:** Continue to improve my skills to find the delicate balance between readability and efficiency in coding.<br>