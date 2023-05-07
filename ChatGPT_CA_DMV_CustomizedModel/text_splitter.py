def split_text_into_files(file_path, chunk_size):
    # Read the text from the file
    with open(file_path, 'r') as file:
        text = file.read()

    # Split the text into chunks of the specified size
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

    # Create and save separate files for each chunk
    for i, chunk in enumerate(chunks):
        with open(f'chunk_{i+1}.txt', 'w') as output_file:
            output_file.write(chunk)


# Example usage
file_path = 'manual.txt'  # Replace with the path to your input file
chunk_size = 1800

split_text_into_files(file_path, chunk_size)
