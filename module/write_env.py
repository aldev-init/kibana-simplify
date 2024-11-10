def write_to_env(key, value):
    """
    Write or update a key-value pair in the .env file
    Args:
        key (str): The configuration key
        value (str): The value to set
    """
    env_path = '.env'  # Adjust path if needed
    
    # Read existing contents
    with open(env_path, 'r') as file:
        lines = file.readlines()
    
    # Try to find and replace existing key
    key_found = False
    for i, line in enumerate(lines):
        if line.strip() and not line.startswith('#'):  # Skip comments and empty lines
            if line.split('=')[0].strip() == key:
                lines[i] = f"{key}={value}\n"
                key_found = True
                break
    
    # If key wasn't found, append it
    if not key_found:
        lines.append(f"{key}={value}\n")
    
    # Write back to file
    with open(env_path, 'w') as file:
        file.writelines(lines)