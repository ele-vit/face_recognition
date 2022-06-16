import face_recognition
import os
import cv2
from resources.rectangle import Rectangle
from resources.vector_faces import Vector_face

cap = cv2.VideoCapture(0)
TOLERANCE = 0.6

known_faces = Vector_face.list_vector()

while True:
    ret, frame = cap.read()
    locations = face_recognition.face_locations(frame)
    encodings = face_recognition.face_encodings(frame, locations)

    for face_encoding, face_location in zip(encodings, locations):
        vector_face = [x['vector_face'] for x in known_faces]
        result = face_recognition.compare_faces(vector_face, face_encoding, TOLERANCE)

        p = result.index(True) if True in result else -1
        name_person = known_faces[p]['name_person']
        text, color = (name_person, (255, 255, 255)) if True in result else ('NOT DATA', (50, 50, 255))

        x_y = (face_location[3], face_location[0])
        h_w = (face_location[1], face_location[2])
        corner_radius = 0
        line_length = 50
        Rectangle.draw_border(frame, x_y, h_w, color, 1, corner_radius, line_length)

        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, text.upper(), (face_location[3], face_location[0]-10), font, 0.7, color, 1)


    cv2.imshow("Facial Recognition", frame)
    esc =  cv2.waitKey(1)
    close = cv2.getWindowProperty('Facial Recognition',cv2.WND_PROP_VISIBLE)
    if esc == 27 or close < 1:
        break

cap.release()
cv2.destroyAllWindows()
