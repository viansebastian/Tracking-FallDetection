# ***Combination of Optical Flow and Rank Pooling for Vision Based Fall Detection System***
 

***Abstract*** — Falls pose a significant health risk, especially to the elderly, leading to serious injuries such as fractures, head trauma, and loss of consciousness. The World Health Organization identifies falls as the second leading cause of accidental injury deaths globally, highlighting the vulnerability of the elderly due to age-related factors. Computer vision has emerged as a promising solution to enhance elderly safety. By leveraging advanced image processing and Convolutional Neural Networks (CNNs), these systems can automatically detect falls in real-time, providing immediate alerts to caregivers and ensuring timely intervention. Traditional video analysis methods for fall detection are burdened by high computational demands and often suffer from accuracy issues, making them less feasible for real-time applications. Recent advancements, such as rank pooling, optical flow, and object tracking, address these challenges by capturing temporal information, measuring motion between frames, and enhancing detection accuracy. These techniques enable the development of lightweight, efficient vision-based fall detection systems, providing reliable and timely alerts without high computational costs. This work proposes a method to accurately detect falls through video input, aiming for maximum efficiency and reduced computational burden using sophisticated preprocessing techniques.

***Keywords*** — Fall detection, CNN, Optical Flow, Rank Pooling, Image Processing

---

This is a repository for my computer vision class assignment, where I am tasked to build a vision based fall detection system using tracking. The method of tracking used is optical flow, and rank pool is applied to essentially 'compress' optical flow images into a single image/vector to lighten computational burden. Using the EfficientNetV2 architecture, this project goes in depth into video analysis methods, as well as its strengths and weaknesses. The flow of the project can be seen in fig. 1 below. 

![Project FlowChart](docs/flowchart.png?raw=true "Project FlowChart")

*fig 1.0: project flowchart*

---
***Data Acquisition***

The dataset used in this project is taken from two sources, with their description as follows. 
 - The [Multicam Dataset](), containing 22 scenarios of Fall and  2 scenarios of Not Fall scenes, each with 8 different angles. After downloading them, it is recorded to 120 fps. 
 - The [URFD Dataset](), containing 30 sequences of frames of Fall and 40 sequences of frames of ADL (Activities of Daily Life) scenarios. 

Both of these dataset also offers Depth data, but this project also performs frame extractions and other data input handling, so only original data is taken. 

---
***Data Preprocessing***

The main preprocessing methods used in this project are optical flow and rank pooling. Optical flow generates an image that represents the movement of pixels between n-frames. Then, it is rank pooled to output a single image/vecotr that represents the dynamic of sequences. This approach is taken referencing many predescent researches, and its aim is to reduce computational burden substantially. After extracting frames from videos, and computing the optical flow and rank pool, only 46 Daily Activity and 53 Fall optical flow rank pooled images remain. This number is reduced from the total amount of frames stated in the Data Acquisition section above. A sample of these images can be seen in fig 2.0 below. 

![sample img](docs/sample.png?raw=true "sample img")
*fig 2.0: sample preprocessed image, input*

---
***Modeling***

This project utilizes Transfer Learning for its modeling. The EfficientNetV2S pre-trained model is a 55-layer neural network achitecture branced from the EfficientNet family. At its core, EfficientNet utilizes combination of scaling (width, height, resolution), as well as MBConv layers. EfficientNetV2 uses the Fused-MBConv, which is optimized for speed and parameter efficiency. The base architecture of EfficientNetV2 can be seen in fig. 3 below. 

![EfficientNetV2S](docs/eff.jpg?raw=true "EfficientNetV2S")

*fig 3.0: EfficientNetV2 base architecture*
[src](https://www.sciencedirect.com/science/article/pii/S1076633222006328)

After loading the pre-trained model, multiple convolution, max pooling, and global average pooling layers are added, with dense layers as output. This is to ensure custom dataset specialization. 

---
***Evaluation and Discussion***

The training history can be observed in fig. 4.0 below. 

![hist](docs/hist.png?raw=true "hist")
*fig 4.0: training history*

The results of the training can be evaluated using Accuracy, Precision, Recall, and F1-Score, which can be seen in table 1.0 below. 

|              | **Precision** | **Recall** | **F1-Score** | **Support** |
|:------------:|:-------------:|:----------:|:------------:|:-----------:|
|    RP_ADL    |      0.00     |    0.00    |     0.00     |      9      |
|    RP_FALL   |      0.53     |    1.00    |     0.69     |      10     |
|   accuracy   |               |            |     0.53     |      19     |
|   macro avg  |      0.26     |    0.50    |     0.34     |      19     |
| weighted avg |      0.26     |    0.53    |     0.36     |      19     |

Given the results of the training, through the visualization and metrics, it can be seen that the model is heavily biased and shows overfitting behaviours. After thorough researching (details can be seen in the report), potential factors would be imbalanced dataset, lack of image preprocessing before optical flow and rank pooling computation, as well as the nature of the EfficientNet architecture itself. 

--- 
***Conclusion***

It is worth noting that the training time took 3 minutes for 30 epochs. This is a note-taking worthy results, as various sources claim that video based analysis could take hours to just render, even more so training with deep learning. 

As a final note, the strength of this approach lies when the dataset is abundant in size as well as amount, proving scalability and efficiency in computational optimization. For more details, please do read my report in this repository!
