##                 **Car Price Prediction - Machine Learning Regression Project**

<!-- <p align='center'>
  <img src='https://github.com/Shuhaib73/Classification_ML_Mushrooms_Project/blob/main/mus_ims.jpg' />
</p> -->
You can access the web application[Audio classification system] by following this link: https://audioclassification.streamlit.app/

## **Introduction**
  ** In the dynamic landscape of the automotive industry, setting accurate and competitive prices for cars is a critical factor for success. Cars undergo a fascinating economic transformation as they transition from new vehicles with manufacturer-set prices to used ones influenced by the intricate dynamics of supply, demand, and individual histories. This transformation, coupled with the unique features that distinguish each car, makes traditional valuation methods less effective. Leveraging the power of machine learning and data science to untangle the complex factors influencing car prices.

## **Problem Statement**
In this project, our primary aim is to develop an accurate car price prediction model using machine learning techniques. We're focusing on building a sophisticated system that leverages the capabilities of predictive analytics to unravel valuable insights for new companies in the automotive industry, particularly tailored for a used car seller company and also to empower individual car owners looking to sell their vehicles. The goal is to assist these companies in making informed decisions about their pricing strategies.
    *he dataset consists of 11,914 entries representing various car features. The columns include information such as the make, model, year, engine fuel type, engine horsepower, engine cylinders, transmission type, driven wheels, number of doors, market category, vehicle size, vehicle style, highway miles per gallon (MPG), city MPG, popularity, and Manufacturer's Suggested Retail Price (MSRP).
    Before delving into model development, essential data preprocessing steps are undertaken. This involves handling missing values in columns like 'Engine Fuel Type,' 'Engine HP,' 'Engine Cylinders,' and 'Number of Doors.' Additionally, categorical variables are often encoded for better model compatibility.
    Predictive analytics techniques, particularly machine learning algorithms, are employed to gain insights into the factors affecting car prices. Evaluation metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), or R-squared are used to assess model performance. The goal is to provide valuable insights for car seller company and also to empower individual car owners looking to sell their vehicles, assisting in crafting informed decisions about pricing strategies."

    
### Machine Learning & Deep Learning Models used in the project:
#### The project compares the results of different techniques :
##### - Linear Regression
##### - Decision Tree Regressor
##### - Random Forest Regressor
##### - K-Nearest Neighbors Regressor
##### - Gradient Boosting Regressor
##### - XGBoost Regressor Regressor

#### **Exploratory Data Analysis (EDA)**

<details>
       <summary>
              <strong>​✒️<Click here to see :</strong> Employee Attrition Status 
       </summary>
                     <p align='center'>
                            <img src='https://github.com/Shuhaib73/Employee_Attrition-Deep_Learning-ANN/blob/main/Attri_dis.PNG' style='width: 50%;' />
                     </p>
</details>

<details>
       <summary>
              <strong>​✒️<Click here to see :</strong> Attrition Count Based on Age
       </summary>
                     <p align='center'>
                            <img src='https://github.com/Shuhaib73/Employee_Attrition-Deep_Learning-ANN/blob/main/Age_att.PNG' style='width: 70%;' />
                     </p>
</details>

<details>
       <summary>
              <strong>​✒️<Click here to see :</strong> Attrition Count Based on Gender
       </summary>
                     <p align='center'>
                            <img src='https://github.com/Shuhaib73/Employee_Attrition-Deep_Learning-ANN/blob/main/gender_at.PNG' style='width: 50%;' />
                     </p>
</details>

<details>
       <summary>
              <strong>​✒️<Click here to see :</strong> Attrition Count By Department
       </summary>
                     <p align='center'>
                            <img src='https://github.com/Shuhaib73/Employee_Attrition-Deep_Learning-ANN/blob/main/Dep_at.PNG' style='width: 70%;' />
                     </p>
</details>

<details>
       <summary>
              <strong>​✒️<Click here to see :</strong> Attrition Count By City
       </summary>
                     <p align='center'>
                            <img src='https://github.com/Shuhaib73/Employee_Attrition-Deep_Learning-ANN/blob/main/city_at.PNG' style='width: 70%;' />
                     </p>
</details>

<details>
       <summary>
              <strong>​✒️<Click here to see :</strong> Classification Report
       </summary>
                     <p align='center'>
                            <img src='https://github.com/Shuhaib73/Employee_Attrition-Deep_Learning-ANN/blob/main/clss.PNG' style='width: 60%;' />
                     </p>
</details>

<details>
       <summary>
              <strong>​✒️<Click here to see :</strong> Confusion Matrix
       </summary>
                     <p align='center'>
                            <img src='https://github.com/Shuhaib73/Employee_Attrition-Deep_Learning-ANN/blob/main/Confu.PNG' style='width: 90%;' />
                     </p>
</details>

## The project pipeline can be summarized in the following steps: 
#### **Data Understanding and Exploration** : 
    * In this initial phase, the dataset is loaded, and a thorough exploration of the features is conducted. Understanding the data is crucial for selecting relevant features that will contribute to the final car price prediction model.  
#### <strong>Data Preprocessing</strong>: 
    * This phase involves handling missing values, addressing outliers, and performing necessary data cleansing tasks. Specifically, it includes addressing missing values in essential columns such as 'Engine Fuel Type,' 'Engine HP,' 'Engine Cylinders,' and 'Number of Doors.' This targeted approach ensures that the model is built on a foundation of complete and accurate data.
#### <strong>Feature Selection and Engineering</strong>: 
    *  Building on insights gained from Exploratory Data Analysis (EDA), the feature selection process is refined. Various feature engineering techniques are experimented with to improve the predictability of the car price prediction model.
#### <strong>Model Building and Hyperparameter Tuning</strong>: 
    * In this critical phase, the project conducted an extensive exploration of machine learning models for predicting car prices. Employing grid search techniques, the hyperparameters of six distinct models were fine-tuned to optimize their performance. The models evaluated include Linear Regression, Decision Tree, Random Forest, Gradient Boosting, k-Nearest Neighbors (kNN), and XGBoost (XGB).

    This meticulous approach allowed for a systematic investigation of the hyperparameter space, ensuring each model's configuration is finely tuned for maximum predictive accuracy. The diverse set of models considered provides a comprehensive understanding of their strengths and limitations in the context of car price prediction. The outcome of this phase lays the groundwork for selecting the most effective model, poised to deliver accurate and reliable predictions for the dynamic automotive market.
#### <strong>Model Evaluation</strong>: 
    * In this phase, a comprehensive evaluation of various machine learning models was conducted, revealing distinct variations in mean absolute error (MAE) and mean squared error (MSE) across different algorithms. Among these models, the Gradient Boosting algorithm emerged as a standout performer, showcasing superior predictive accuracy.
#### <strong>Deployment</strong>: 
    * The finalized car price prediction model is deployed, and in this case, it is potentially integrated into a web application using Streamlit. The deployment allows users to interact with the model conveniently through a user-friendly interface. 
  ``` You can access the web application by following this link: https://audioclassification.streamlit.app/


## **Conclusion** :
``` After a comprehensive evaluation of various machine learning models, distinct variations in mean absolute error (MAE) and mean squared error (MSE) have been observed across different algorithms. Notably, the Gradient Boosting algorithm emerges as a standout performer, showcasing superior predictive accuracy. The achievement of a remarkable 99% R-squared score underscores the model's excellent fit to the data.

In light of these findings, the decision has been made to deploy the Gradient Boosting model. This choice is driven by the anticipation of its robust performance in real-world applications. The model's demonstrated accuracy and resilience make it a promising model for making informed predictions and contributing valuable insights to the dynamic landscape of car pricing.```
