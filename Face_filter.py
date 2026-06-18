import cv2
import mediapipe as mp  
import math
import numpy as np

glasses = cv2.imread(r"D:\Python_Programming\Open CV\Face filter\glasses.png", -1)
dog = cv2.imread(r"D:\Python_Programming\Open CV\Face filter\dog.png", -1)
crown = cv2.imread(r"D:\Python_Programming\Open CV\Face filter\crown.png", -1)
mustache=cv2.imread(r"D:\Python_Programming\Open CV\Face filter\mustache.png",-1)
heart=cv2.imread(r"D:\Python_Programming\Open CV\Face filter\heart.png",-1)
hair=cv2.imread(r"D:\Python_Programming\Open CV\Face filter\hair.png",-1)
rainbow = cv2.imread(r"D:\Python_Programming\Open CV\Face filter\rainbow.png", -1)

print("Press 1 → Glasses 😎")
print("Press 2 → Dog 🐶")
print("Press 3 → Crown 👑")
print("Press 4 → Mustache🥸")
print("Press 5 → Heart💕") 
print("Press 6 → Hair 🦰")
print("Press 7 → Rainbow 🌈 (Mouth Open)")
print("Press 0 → No filter ")
print("Press Q → Exit")

if glasses is None or dog is None or crown is None or rainbow is None:
    print("Error Loading images")
    exit()

mp_face_mesh=mp.solutions.face_mesh
face_mesh=mp_face_mesh.FaceMesh(max_num_faces=1)

cap=cv2.VideoCapture(1)

filter_type=0

def overlay(frame,overlay_img,x,y,w,h):
        overlay_img = cv2.resize(overlay_img, (w, h))
            
        if x < 0: x = 0
        if y < 0: y = 0
        if x + w > frame.shape[1]: w = frame.shape[1] - x
        if y + h > frame.shape[0]: h = frame.shape[0] - y

        overlay_img = overlay_img[0:h, 0:w]

        if overlay_img.shape[2] < 4:
            return frame

        alpha = overlay_img[:, :, 3] / 255.0
        alpha_bg = 1.0 - alpha

        for c in range(3):
            frame[y:y+h, x:x+w, c] = (
                alpha * overlay_img[:, :, c] +
                alpha_bg * frame[y:y+h, x:x+w, c]
            )
        return frame

rainbow_offset = 0
rainbow_offset += 5

while True:
    ret, frame = cap.read()
    
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:

            # Eye landmarks
            left_eye = face_landmarks.landmark[33]
            right_eye = face_landmarks.landmark[263]

            x1 = int(left_eye.x * w)
            y1 = int(left_eye.y * h)
            x2 = int(right_eye.x * w)
            y2 = int(right_eye.y * h)

            eye_dist = int(math.hypot(x2 - x1, y2 - y1))
                # Nose & forehead
            nose = face_landmarks.landmark[1]
            forehead = face_landmarks.landmark[10]

            nx, ny = int(nose.x * w), int(nose.y * h)
            fx, fy = int(forehead.x * w), int(forehead.y * h)
            # Mouth landmarks
            upper_lip = face_landmarks.landmark[13]
            lower_lip = face_landmarks.landmark[14]

            ux, uy = int(upper_lip.x * w), int(upper_lip.y * h)
            lx, ly = int(lower_lip.x * w), int(lower_lip.y * h)

            mouth_open = abs(ly - uy)

# =============================================================================
#                                     FILTERS                                  
# =============================================================================

# ---------------------------------- Glasses ----------------------------------
            
            if filter_type == 1:  
    
                scale = 1.7
                fw = int(eye_dist * scale)
                fh = int(glasses.shape[0] * (fw / glasses.shape[1]))

                x = int((x1 + x2) / 2 - fw / 2)
                y = int((y1 + y2) / 2 - fh / 2) - 10
                frame = overlay(frame, glasses, x, y, fw, fh)

#---------------------------------- Dog ----------------------------------

            elif filter_type == 2:  
    
                scale = 2.3
                fw = int(eye_dist * scale)
                fh = int(dog.shape[0] * (fw / dog.shape[1]))

                x = int(nx - fw * 0.5)
                y = int(ny - fh * 0.9)
                frame = overlay(frame, dog, x, y, fw, fh)

            
#---------------------------------- Crown ----------------------------------
            
            elif filter_type == 3:                  
    
                scale = 2.5
                fw = int(eye_dist * scale)
                fh = int(crown.shape[0] * (fw / crown.shape[1]))

                x = fx - fw // 2

                y = fy - int(fh * 5.3)
                frame = overlay(frame, crown, x, y, fw, fh)

#---------------------------------- mustache ----------------------------------
            
            elif filter_type == 4:
    
                scale = 1.3
                fw = int(eye_dist * scale)
                fh = int(mustache.shape[0] * (fw / mustache.shape[1]))

                x = fx - fw // 2

                y = fy - int(fh * -2.3)
   
                frame = overlay(frame, mustache, x, y, fw, fh)

#---------------------------------- Hearts ----------------------------------
            
            elif filter_type == 5:  
    
                scale = 3.0
                fw = int(eye_dist * scale)
                fh = int(heart.shape[0] * (fw / heart.shape[1]))

                x = fx - fw // 2

                y = fy - int(fh * 0.8)
   
                frame = overlay(frame, heart, x, y, fw, fh)    
            
#---------------------------------- Hair ---------------------------------- 
            elif filter_type == 6:  
    
                scale = 2.0
                fw = int(eye_dist * scale)
                fh = int(hair.shape[0] * (fw / hair.shape[1]))

                x = fx - fw // 2

                y = fy - int(fh * 0.8)
   
                frame = overlay(frame, hair, x, y, fw, fh)    
    
#---------------------------------- Rainbow (Mouth Open Animated) ----------------------------------

            elif filter_type == 7:

                if mouth_open > 15:

                    scale = 2.0
                    fw = int(eye_dist * scale)
                    fh = int(rainbow.shape[0] * (fw / rainbow.shape[1]))

                    x = ux - fw // 2
                    # y = ly - 5
                    mouth_height = abs(ly - uy)
                    y = ly - int(mouth_height * 0.3)

                    # Animate (move downward)
                    rainbow_offset += 10
                    if rainbow_offset > fh:
                        rainbow_offset = 0

                    animated_rainbow = rainbow.copy()

                    # Shift image vertically
                    animated_rainbow = np.roll(animated_rainbow, rainbow_offset, axis=0)

                    frame = overlay(frame, animated_rainbow, x, y, fw, fh)
    
    cv2.imshow("Snapchat AI Filter", frame)

    key=cv2.waitKey(1)

    if key==ord('1'):
        filter_type=1
    elif key==ord('2'):
        filter_type=2
    elif key==ord('3'):
        filter_type=3
    elif key==ord('4'):             
        filter_type=4
    elif key==ord('5'):
        filter_type=5
    elif key==ord('6'):
        filter_type=6
    elif key==ord('7'):
        filter_type=7
    elif key==ord('0'):
        filter_type=0
    elif key==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
