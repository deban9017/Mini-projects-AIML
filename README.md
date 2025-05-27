In this repository, I have added some of my mini-projects in AI-ML.
Each mini-project is in a separate folder containing the necessary data files and code files (jupyter notebooks). Folder names same as the project names.

### Mini-Projects:
1. **Stock Prediction**: 
    - This project uses XGBoost to predict stock prices.
    - The dataset contains intraday stock prices of MSFT (15 min intervals). Historical data of most recent 5000 timestamps.
    - I did EDA, feature engineering (lag features, moving averages) and simulation of a realistic trading strategy based on the model predictions.
2. **Feature Matching, distance measurement**:
    - This project uses OpenCV to match features between two images.
    - It uses ORB feature detector.
    - First I did feature matching. Then I manually defined a bounding box having an object of interest in one image and used the matched features to find the same object in the second image. Then I find the distance between camera and the object using the matched features (by calculating angle of view and known focal length of my camera).
