# set-metadata-for-pelican
- Add metadata to Markdown files located in a specific directory for use with the Pelican
- The original files will not be modified; new files will be created at the specified path.
- Before running the script, Python installation and environment variable input are required.

<br><br>

# Getting Started
## 1. Prerequisites
### 1.1. Python install
- If Python is already installed, skip the following steps.

``` bash
# Mac OS
brew update
brew install python

# Linux Ubuntu
sudo apt update
sudo apt install python3
sudo apt install python3-pip

# Linux CentOS
sudo yum update
sudo yum install python3
sudo yum install python3-pip

# Windows
https://www.python.org/downloads/windows/
```

<br>

### 1.2. Setting Environment Variables
- Enter the absolute path of the directory where the files containing the metadata to be input are located, and the absolute path where the output will be located after execution.
- If the absolute path for the output is not provided, the script will use the path where it is executed.
- **Note**: Enter the values in the `.env` file copied from the `.env-temp` file.

```bash
cp .env-temp .env
vi .env
```

- Enter the corresponding values for each key

``` bash
INPUT_DIRECTORY_ABSOLUTE_PATH=
OUTPUT_DIRECTORY_ABSOLUTE_PATH=
```

<br><br>

## 2. Script Execution

``` bash
python main.py
```

<br><br>

## 3. Metadata Structure
**This metadata is placed at the top of the markdown file to provide structured information about the file's content, creation, and categorization.**

- **Title** : This field represents the name of the file without its extension. It is used to quickly identify the content of the file based on its name.
- **Date** : This field captures the creation date and time of the file. It is formatted to show both the date and the exact time when the file was originally created.
- **Category** : This field represents the first directory name in the file's path after the input directory. It categorizes the file based on its location within the directory structure.
- **Tags** : This field lists the directory path from the input directory to the file, excluding the input directory itself and the file name. Each directory in the path is separated by a comma, creating a tag-like structure that helps in identifying the file's location within the directory hierarchy.

**Example**
- For a file located at `/path/to/input/directory/java/file/example.md`, the metadata would be constructed as follows:

``` txt
Title: example
Date: 2022-01-01 12:34
Category: java
Tags: java, file
```

- Title: example
- Date: 2022-01-01 12:34 (creation date and time)
- Category: java (the first directory after the input directory)
- Tags: java, file (the directory path excluding the input directory and file name)
