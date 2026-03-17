import os
import plistlib

class GarageBandMetadataExtractor:
    def __init__(self, band_file):
        self.band_file = band_file
        self.metadata = {}

    def extract_metadata(self):
        # Check if the file exists and has the correct extension
        if not os.path.isdir(self.band_file):
            raise FileNotFoundError(f"The file {self.band_file} does not exist.")
        if not self.band_file.endswith('.band'):
            raise ValueError(f"The file {self.band_file} is not a valid .band file.")

        # Try to find GarageBand metadata files in the .band bundle
        # Common GarageBand metadata files include 'projectData' or files in 'Alternatives' folder
        possible_metadata_files = [
            'projectData',
            'project.plist',
            os.path.join('Alternatives', 'project.plist')
        ]
        
        metadata_file_path = None
        for possible_file in possible_metadata_files:
            full_path = os.path.join(self.band_file, possible_file)
            if os.path.isfile(full_path):
                metadata_file_path = full_path
                break
        
        if not metadata_file_path:
            raise FileNotFoundError(f"No recognizable metadata file found in {self.band_file}.")

        # Read the plist/metadata data from the file
        try:
            with open(metadata_file_path, 'rb') as file:
                try:
                    # Try binary plist first
                    self.metadata = plistlib.load(file)
                except plistlib.InvalidFileException:
                    # If binary fails, try XML format
                    file.seek(0)
                    content = file.read().decode('utf-8')
                    self.metadata = plistlib.loads(content.encode('utf-8'))
        except Exception as e:
            raise RuntimeError(f"Failed to read metadata from {metadata_file_path}: {e}")

    def get_metadata(self):
        # Return the extracted metadata
        return self.metadata

# Example usage:
if __name__ == '__main__':
    band_file_path = 'path/to/your/project.band'  # Change this to your actual .band file path
    extractor = GarageBandMetadataExtractor(band_file_path)

    try:
        extractor.extract_metadata()
        metadata = extractor.get_metadata()
        print("Extracted Metadata:")
        for key, value in metadata.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"Error: {e}")

# TODO: Add more specific metadata extraction features, like audio track details or effects used.
# TODO: Implement a way to output metadata in different formats (e.g., JSON, CSV).
# Limitations: Currently only extracts basic project metadata.
