# Gemini results:

def label_encode(data):

    # Extract unique labels and sort them to ensure consistent mapping
    unique_labels = sorted(list(set(data)))
    
    # Create mapping dictionary
    label_to_int = {label: idx for idx, label in enumerate(unique_labels)}
    
    # Encode the data
    encoded_values = [label_to_int[item] for item in data]
    
    return encoded_values, label_to_int

# My code:
