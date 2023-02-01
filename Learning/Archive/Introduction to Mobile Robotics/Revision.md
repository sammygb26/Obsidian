- Introduction
	- [x] Localization
	- [x] Object Detection
	- [x] Levels of Mobile Autonomy
- Sensors and Computing Systems
	- [x] Different sensor types
	- [x] RGB camera
	- [x] Stereo Cameras
	- [x] LiDAR
	- [x] mmWave Radar
	- [x] Ultrasonic Sonar
	- [x] GNSS IMU
	- [x] Wheel Odometry
	- [x] Parallel Processing
	- [x] Hardware synchronization
	- [x] Software Decomposition
	- [x] Environment Mapping
	- [x] Environment Perception
	- [x] Motion planning
	- [x] Controller
	- [x] System supervisor
	- [x] Actuators
	- [x] Sparse Keypoint Feature Map
	- [x] Sign Distance Function Map
	- [x] HD road map
- Camera and Images
	- [x] Image representation
	- [x] Pinhole camera model
	- [x] World and Image Coordinates
	- [x] stereo Camera Model
	- [x] Noise
	- [x] Mean Filter
	- [x] Cross correlation
	- [x] Gaussian filter
	- [x] Sobel Kernel
- Image Feature Matching
	- [ ] Feature Matching
	- [ ] Feature Detection
		- [x] Saliency
		- [x] Repeatability
		- [x] Locality
		- [x] Quantity
		- [x] Efficiency
	- [x] Feature detection
	- [ ] Harris Corner Detection
	- [x] Feature Descriptors
		- [x] Repeatability
		- [x] Distinctiveness
		- [x] Compact efficient
	- [x] SIFT
	- [x] Brute force feature matching
	- [x] Localization with Matched Features
	- [x] Localization model
	- [x] Localization Solution
	- [x] Outliers
	- [x] Ransack
	- [x] Visual Odometry
- Deep Neural Networks and CNNs
	- [x] Feedforward NNs
	- [x] Hidden Units
	- [x] ReLU
	- [x] Other activations
	- [x] Training
	- [x] Inference
	- [x] SoftMax output layers
	- [x] Cross entropy loss
	- [x] Mean output regression
	- [x] MSE
	- [x] Gradient Descent
	- [x] CNNs
	- [x] Convolutional operation
	- [x] Dense vs Sparse
	- [x] Kernel Channels
	- [x] Pooling
- Object Detection
	- [x] Problem
	- [x]  Hard
		- [x] No fully observed
		- [x] Scale Distraction
		- [x] Illumination
	- [x] Bounding box
	- [x] Class
	- [x] IOU
	- [x] TP, FP, FN
	- [x] Precision Recall
	- [ ] PR-curve
	- [x] Feature Extractor
	- [x] Anchor prior boxes
	- [x] Residual learning for prior boxes
	- [x] Output layers
	- [ ] NMS
	- [x] Minibatch selection 
		- [x] Clear 
		- [x] Hard Negative anchor mining
		- [ ] Control training bias
	- [ ] Loss functions
- Semantic Segmentation
	- [x] Problem formulation
	- [x] Hardness
	- [x] Evaluation metrics
	- [x] CNNs for SS
	- [x] Upsampling
	- [x] Upsampling Methods
		- [x] Naive
		- [x] Encoder decoder
		- [x] Max Indices
	- [x] Classification Loss
	- [x] Drivable surface estimation
	- [x] RANSAC
	- [x] Semantic Lane Estimation
	- [x] Instance Segmentation
	- [ ] RoI pooling
- Kalman Filter
	- [x] Robots states
	- [x] Motion model
	- [x] GPS challenges
	- [x] Combining the guess and observation
	- [ ] Prediction
	- [ ] Correction
	- [ ] EKF
	- [x] Measurement Model of LIDAR
	- [x] Linear Approximation
	- [x] Point to linearize at
	- [x] Jacobians
	- [x] Limitations of EKF
	- [x] Linearization Error
	- [x] Jacobian Computation
- Reference Frames and GPS
	- [x] MR coordinate system
	- [x] Rigid Body
	- [x] Right Hand Only
	- [x] Rigid Body Motion
	- [x] Degrees of Freedom
	- [x] Coordinate Rotation
	- [x] Rotation Representation
		- [ ] DCM
		- [x] Euler Angles
		- [ ] Unit Quaternions (optional)
	- [x] Earth Centered Earth Fixed Frame
	- [x] Navigation Frame
	- [x] Extrinsic Calibration
	- [x] GNSS
	- [x] GPS
	- [x] GPS encoding
	- [x] GPS Trilateration
	- [x] GPS Error Sources
- LiDAR point clouds and ICP
	- [x] LiDAR Detection
	- [x] Origin
	- [x] Math model
	- [x] Simple model
	- [x] Measurement Model 3D
	- [x] Point cloud data structure
	- [x] Translation on Point Cloud
	- [x] Rotation on Point Cloud
	- [x] Scaling point cloud
	- [ ] Operation Order
	- [x] State estimation via Point Set Registration
	- [x] ICP algorithm
	- [ ] ICP steps
	- [x] ICP outliers
	- [ ] Loss functions
- Occupancy Grid and Maps
	- [x] Occupancy grid
	- [x] Assumptions for occupancy grid
	- [x] Range sensor
	- [x] Measurement Noise
	- [x] Probabilistic Occupancy
	- [ ] Bayesian Update for Occupancy Grid
	- [x] Issues with pure Bayesian
	- [x] Bayesian Log Odds
	- [x] Inverse Measurement Model
	- [ ] IMM affected region
	- [x] Downsampling
	- [ ] Ground Plan Classification
	- [x] HD roat map
	- [ ] Lanelets
	- [x] Topological Map
	- [x] Semantic Map
	- [x] Feature Landmark Map
- Motion Planning
	- [x] Mission planning task
	- [x] Motion planning task
	- [x] Road structure
	- [x] Road intersection
	- [x] Obstacle
	- [x] Obstacle intersection
	- [x] Common Behavior Sets
	- [x] Hierarchical Planning Approach
	- [x] Bicycle Model
	- [x] Curvature
	- [x] Vehicle Dynamics
	- [x] Static object avoidance
	- [x] Dynamic Object Avoidance
	- [x] Leading vehicle constraint
	- [x] Road rules
	- [x] Objective functions
	- [x] Efficiency
	- [x] Path length
	- [x] Reference Tracking
	- [x] Smoothness
	- [x] Curvature
	- [x] Hierarchical Planner
	- [x] Mission planner (AIDS RA)
- Behavior Planning
	- [x] Hierarchical Planner Again
	- [x] Behavior Planner Idea
	- [x] Maneuvers
	- [x] Secondary Output
	- [x] Input requirements
	- [x] FSM formulation
	- [x] Advantages of FSM
	- [x] TTC
	- [x] Simulation Approach
	- [x] Estimation Approach
	- [x] Strengths and Weaknesses