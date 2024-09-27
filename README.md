# Detection and Classification of Network Traffic Anomalies

The experiments utilize the lightweight version of the
[IoT-23](https://www.stratosphereips.org/datasets-iot23) [[1]](#footnote-1) dataset.

## 1. Requirements

### 1.1. Install Required Libraries 

No  | <div style="width:100px">Library Name</div>| Version          | Description
--- |------------   |------------   |-------------
1   | [Python](https://www.python.org/downloads/release/python-380/)|3.8.8|Programming Language
2   | [scikit-learn](https://scikit-learn.org/stable/)|0.24.1|Machine Learning tools for Python
3   | [NumPy](https://numpy.org/)|1.19.5|Library for Scientific Computing in Python
4   | [pandas](https://pandas.pydata.org/)|1.2.2|Library for Data Analysis & Manipulation in Python
5   | [matplotlib](https://matplotlib.org/stable/tutorials/introductory/pyplot.html)|3.3.4|Library for Data Visualization in Python
6   | [seaborn](https://seaborn.pydata.org/)|0.11.1|Statistical Visualization Library
7   | [psutil](https://github.com/giampaolo/psutil)|5.8.0|Cross-platform library for accessing information on running processes and system usage (CPU, memory, disks, network, sensors) in Python
8   | [scikit-plot](https://github.com/reiinakano/scikit-plot)|0.3.7|Library for visualizations
9   | [pickle](https://docs.python.org/3/library/pickle.html)|-|Python's object serialization for model saving

### 1.2. Download & Unzip Dataset

1. Download the lightweight version of [IoT-23](https://www.stratosphereips.org/datasets-iot23) (archive size - 8.8 GB)
> This version contains only labeled flows, excluding the pcap files.
2. Extract the archive (total size - approximately 44 GB)
> 

## 2. Configure Project
1. Clone this repository.
2. Install any missing libraries.
3. Open **config.py** and set the required directory paths.
> base_path = 'E:\\machine-learning\\datasets\\iot23\\'
> scenarios_directory = f'{base_path}1_scenarios\\'
> attacks_directory = f'{base_path}2_attacks\\'
> data_directory = f'{base_path}3_data_v2\\'
> experiments_directory = f'{base_path}4_experiments_v2\\'
4. Verify your configuration by running **run_step00_configuration_check.py**
> Ensure the output message indicates that you can proceed to the next step. If not, check your configuration and resolve any issues.

## 3. Prepare Data for Machine Learning
### 3.1. Extract Data from Scenarios
Execute data extraction by running **run_step01_extract_data_from_scenarios.py**
> Despite multiple scenarios, the files contain mixed attack and benign traffic.
> Thus, we will separate entries of similar types into distinct files.
> The output files will be saved to **iot23_attacks_dir**.
>
> Expect this step to take about 2 hours to complete.

### 3.2. Shuffle File Content
Run content shuffling by executing **run_step01_shuffle_file_content.py**
> This step enhances the reliability of data samples.
> Larger files are divided into 1 GB partitions, and the contents of all partitions (from the same file) are shuffled. 
> Once shuffling is complete, the partitions are merged back into a single file, replacing the original.
> 
>  This step is expected to take approximately 2.5 to 3 hours.

----

# Option 1: Run Demonstration

#### 1.1. Requirements
>
> 1. [Download & Unzip Dataset](#12-download--extract-dataset)
>
> 2. [Configure Project](#2-configure-project)
>
> 3. [Prepare Data for Machine Learning](#3-prepare-data-for-machine-learning)

#### 1.2. Execute demo by running **run_demo.py**

> Use this option to verify that everything is functioning correctly. 
> It processes only 10,000 records per file, allowing the entire operation to complete in a few minutes if the data is prepared.

# Option 2: Execute Designed Experiments

#### 2.1. Requirements
>
> 1. [Download & Unzip Dataset](#12-download--extract-dataset)
>
> 2. [Configure Project](#2-configure-project)
>
> 3. [Prepare Data for Machine Learning](#3-prepare-data-for-machine-learning)

#### 2.2. Execute designed experiments by running **run_experiments.py**
>  **This step is anticipated to take around 24 hours to complete!**
>  
> The data samples for training and testing include over **20M** records.

>TODO

# Option 3: Execute Custom Experiments
#### 3.1. Requirements
>
> 1. [Download & Unzip Dataset](#12-download--extract-dataset)
>
> 2. [Configure Project](#2-configure-project)
>
> 3. [Prepare Data for Machine Learning](#3-prepare-data-for-machine-learning)

#### 3.2. Execute custom experiments by running **run_experiments.py**

>TODO


---
<a name="footnote-1">[1]</a>: “Stratosphere Laboratory. A labeled dataset with malicious and benign IoT network traffic. January 22nd. Agustin
Parmisano, Sebastian Garcia, Maria Jose Erquiaga. Online: https://www.stratosphereips.org/datasets-iot23"

