import math
from sklearn import neighbors
import os
import os.path
import pickle
from sklearn.externals import joblib 
from sklearn_pandas import DataFrameMapper
from sklearn2pmml import sklearn2pmml
from sklearn2pmml import PMMLPipeline
from PIL import Image, ImageDraw
#import face_recognition
from face_recognition_cli import image_files_in_folder
import temp
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def train(train_dir):
    X = []
    y = []

    # Loop through each person in the training set
    for class_dir in os.listdir(train_dir):
        if not os.path.isdir(os.path.join(train_dir, class_dir)):
            continue

        # Loop through each training image for the current person
        for img_path in image_files_in_folder(os.path.join(train_dir, class_dir)):
            image = face_recognition_models.load_image_file(img_path)
            face_bounding_boxes = face_recognition_models.face_locations(image)

            if len(face_bounding_boxes) != 1:
                # If there are no people (or too many people) in a training image, skip the image.
                # Add face encoding for current image to the training set
                #X.append(face_recognition.face_encodings(image, known_face_locations=face_bounding_boxes)[0])
                y.append(class_dir)


    #return knn_clf




if __name__ == "__main__":
    classifier = train("train_data")

    # STEP 2: Using the trained classifier, make predictions for unknown images
    for image_file in os.listdir("test_data"):
        full_file_path = os.path.join("test_data", image_file)

        print("Looking for faces in {}".format(image_file))

