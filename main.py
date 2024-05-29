import os
from pathlib import Path
from datetime import datetime
import shutil

# Load environment variables from .env file
def load_env(file_path):
    env_vars = {}
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip() and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                env_vars[key] = value
    return env_vars

# Load environment variables
env_vars = load_env('.env')

INPUT_DIRECTORY = env_vars['INPUT_DIRECTORY_ABSOLUTE_PATH']
OUTPUT_DIRECTORY = env_vars.get('OUTPUT_DIRECTORY_ABSOLUTE_PATH', os.getcwd())

# Ensure the output directory exists
Path(OUTPUT_DIRECTORY).mkdir(parents=True, exist_ok=True)

def get_file_metadata(file_path, input_dir):
    relative_path = file_path.relative_to(input_dir)
    file_name = file_path.stem
    creation_time = datetime.fromtimestamp(file_path.stat().st_ctime)
    parts = relative_path.parts
    first_directory = parts[0] if len(parts) > 1 else ''
    tags = ', '.join(parts[:-1])
    
    return file_name, creation_time, first_directory, tags

def process_files(input_dir, output_dir):
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    
    for file in input_path.rglob('*'):
        if file.is_file():
            if file.suffix == '.md':
                file_name, creation_time, first_directory, tags = get_file_metadata(file, input_path)
                
                metadata = f"""Title: {file_name}
Date: {creation_time.strftime('%Y-%m-%d %H:%M')}
Category: {first_directory}
Tags: {tags}

"""
                with open(file, 'r', encoding='utf-8') as original_file:
                    content = original_file.read()
                
                new_content = metadata + content
                
                output_file_path = output_path / file.relative_to(input_path)
                output_file_path.parent.mkdir(parents=True, exist_ok=True)
                
                with open(output_file_path, 'w', encoding='utf-8') as new_file:
                    new_file.write(new_content)
            else:
                output_file_path = output_path / file.relative_to(input_path)
                output_file_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(file, output_file_path)

process_files(INPUT_DIRECTORY, OUTPUT_DIRECTORY)
