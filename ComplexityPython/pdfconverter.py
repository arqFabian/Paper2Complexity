import os
from Pillow import Image
from pdf2image import convert_from_path

def pdf_to_png(pdf_file, output_dir=None):
    try:
        # Get the base name of the PDF file (without the extension)
        base_name = os.path.splitext(os.path.basename(pdf_file))[0]

        # Convert PDF to a list of PIL images
        images = convert_from_path(pdf_file)

        # Create the output directory if it doesn't exist
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)

        # Save each page as a PNG image with the same name as the PDF file
        for i, image in enumerate(images):
            # Determine the output file path
            if output_dir:
                output_path = os.path.join(output_dir, f'{base_name}_{i + 1}.png')
            else:
                output_path = f'{base_name}_{i + 1}.png'

            image.save(output_path, 'PNG')

        print('PDF converted to PNG images successfully.')
    except Exception as e:
        print(f'Error converting PDF to PNG: {e}')


# Specify the PDF file path
#pdf_file_path = 'C:/Users/arqfa/UnityProjects/VRSLP/Assets/Resources/Images/ComplexityImages/complexitygraph.pdf'
pdf_file_path = 'C:/Users/arqfa/OneDrive/FABIAN DATA/Kyushu 2021/Research/Paper2Complexity/src/Images/test.pdf'

# Specify the output directory (replace with your desired directory)
output_directory = 'C:/Users/arqfa/OneDrive/FABIAN DATA/Kyushu 2021/Research/Paper2Complexity/src/Images'


# Call the function to convert the PDF to PNG and specify the output directory
pdf_to_png(pdf_file_path, output_directory)

