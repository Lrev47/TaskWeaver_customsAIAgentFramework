class ImageProcessingAgent:
    def __init__(self):
        # Initialize any necessary components (e.g., image processing libraries)
        pass

    def process(self, image_data):
        """
        Process the image data and return the result.
        
        :param image_data: Input image data to process.
        :return: Processed image data or an error message if processing fails.
        """
        try:
            # Example of a simple image processing task (like resizing)
            # This would be replaced by actual image processing code
            processed_image = self.resize_image(image_data)
            return processed_image
        except Exception as e:
            return {"error": str(e)}

    def resize_image(self, image_data, size=(100, 100)):
        """
        Resize the image to the given size.
        
        :param image_data: Image data to resize.
        :param size: Target size as a tuple (width, height).
        :return: Resized image data.
        """
        # Example: using Pillow library to resize an image
        from PIL import Image
        image = Image.open(image_data)
        resized_image = image.resize(size)
        return resized_image

# Example usage:
# agent = ImageProcessingAgent()
# result = agent.process("path_to_image.jpg")
