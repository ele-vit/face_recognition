import os
import face_recognition

class Vector_face(object):
    """docstring for ."""

    def list_vector():
        known_faces = []
        faces_dir = "face_pic"
        for filename in os.listdir(f"{faces_dir}"):
            image = face_recognition.load_image_file(f"{faces_dir}/{filename}")
            encoding = face_recognition.face_encodings(image)[0]
            known_faces.append({'name_person':f"{filename}".split('.')[0], 'vector_face':encoding})

        return known_faces
