from etl.extract import extract_data
from etl.transform import transform_data
from etl.validate import validate_data
from etl.load import load_data
import yaml

# Load config
with open("config.yaml", 'r') as f:
    config = yaml.safe_load(f)

# Step 1: Extract
data = extract_data(config['data_sources'])

# Step 2: Transform
data = transform_data(data)

# Step 3: Validate
data, error_logs = validate_data(data, config['validation_rules'])

# Step 4: Load
load_data(data, error_logs, config['output_paths'])

print("ETL process complete. Check logs and outputs.")
