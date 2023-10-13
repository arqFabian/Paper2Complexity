from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

# Store image URLs and user engagement data in a dictionary
image_data = {
    'image1.jpg': {'time_spent': 0},
    'image2.jpg': {'time_spent': 0},
    # Add more images and data as needed
}

@app.route('/')
def index():
    # Display the first image
    current_image = 'image1.jpg'
    return render_template('index.html', image=current_image)

@app.route('/track_time', methods=['POST'])
def track_time():
    # Get the current image and time spent from the client
    current_image = request.form.get('current_image')
    time_spent = float(request.form.get('time_spent'))

    # Update the time spent for the current image
    image_data[current_image]['time_spent'] += time_spent

    # Determine the next image to display (you can implement your logic here)
    # For simplicity, let's just rotate through the images
    image_list = list(image_data.keys())
    current_index = image_list.index(current_image)
    next_index = (current_index + 1) % len(image_list)
    next_image = image_list[next_index]

    return jsonify({'next_image': next_image})

if __name__ == '__main__':
    app.run(debug=True)
