# Brain-Stroke-Prediction

# Tujuan Project
Pembuatan model Classification untuk memprediksi pasien stroke menggunakan dataset brain-stroke_default

# Background Project
Stroke merupakan keadaan darurat medis.Gejala stroke yaitu sulit berjalan, berbicara, dan memahami, serta kelumpuhan atau mati rasa pada wajah, lengan, atau tungkai.
Penanganan dini dengan obat-obatan seperti tPA (penghancur gumpalan darah) dapat meminimalkan kerusakan otak. Pengobatan lain berfokus dalam membatasi komplikasi dan mencegah stroke lainnya.

# Library
library yang digunakan dalam project ini, yaitu:
1. pandas versi 1.4.2
2. numpy versi 1.21.5
3. scikit learn versi 1.1.2
4. feature engine packages versi 1.4.1

# Feature Engineering
Pada project dilakukan beberapa feature engineering seperti:
1. Feature selection mengunakan phik matriks
2. Handling outlier mengunakan metode capping
3. Feature scalling mengunakan metode minmax scaller
4. Feature encoding mengunakan metode one hot encoder
5. Handling data imbalance mengunakan metode Smote over sampling

# Model
Model yang digunakan dalam project ini, sebagai berikut:
1. Logistic Regression
2. SVM Model
3. Random Forest
4. LightGBM 
5. K-Nearest Neighbor (KNN)

# Kesimpulan
Model yang memiliki performa paling bagus dalam memprediksi pasien stroke atau bukan adalah model LightGBM dengan nilai akurasi sekitar 81%

