import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
import argparse
from argparse import ArgumentParser
from insightface.app import FaceAnalysis
from create_face_bank import main


class FaceIdentification():

    def __init__(self):
        pass


    def load_model(self):
        self.app = FaceAnalysis(name = "buffalo_s", providers = ["CPUExecutionProvider"])
        self.app.prepare(ctx_id = 0, det_size = (640, 640))

    def get_image(self, input_image):
        self.image = input_image    
    
    

    def update(self):
        main()


    def identification(self):

        THRESHOLD = 25
        
        input_image = cv2.imread(self.image)
        input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)

        result_image = input_image.copy()

        results = self.app.get(input_image)
        face_bank = np.load("face_bank.npy", allow_pickle=True)
        result_image = input_image.copy()

        for result in results:
            cv2.rectangle(result_image, (int(result.bbox[0]), 
                                        int(result.bbox[1])), 
                                        (int(result.bbox[2]), 
                                        int(result.bbox[3])),(0, 0, 255),4)    

            for person in face_bank:
                face_bank_person_embedding = person["embedding"]
                new_person_embedding = result["embedding"]

                distance = np.sqrt(np.sum((face_bank_person_embedding - new_person_embedding)**2))

                if distance < THRESHOLD:
                    cv2.putText(result_image, person["name"],
                    (int(result.bbox[0]) - 40, int(result.bbox[1] - 10)),
                    cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0),3, cv2.LINE_AA)
                    break

            else:
                cv2.putText(result_image, "Unknown",
                (int(result.bbox[0]) - 40, int(result.bbox[1])),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3,cv2.LINE_AA)

             
        plt.imshow(result_image)  
        plt.axis("off")
        plt.savefig('output/updated_output.png')  
        plt.show()     

    
            
    def face_bank(self):

        # app = FaceAnalysis(name = "buffalo_s", providers = ["CPUExecutionProvider"])
        # app.prepare(ctx_id = 0, det_size = (640, 640))

        face_bank_path = './face_bank'

        face_bank = []

        for person_name in os.listdir(face_bank_path):
            file_path = os.path.join(face_bank_path, person_name)
            if os.path.isdir(file_path):
                for image_name in os.listdir(file_path):
                    image_path = os.path.join(file_path, image_name)
                    print(image_path)

                    image = cv2.imread(image_path)
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                    result = self.app.get(image)

                    if len(result) > 1:
                        print("Warning : more than one face detected")
                        continue

                    embedding = result[0]["embedding"]
                    mydict = {"name": person_name, "embedding": embedding}
                    face_bank.append(mydict)

        np.save("face_bank.npy", face_bank)

            



if __name__ =="__main__":

    # parser = ArgumentParser()
    # parser.add_argument("--image",required=False, type = str, default = "input/one_direction.jpg")
    # parser.add_argument("--update", type=str , action = argparse.BooleanOptionalAction)
    # args = parser.parse_args()

    image = cv2.imread("input/one_direction.jpg")
        
    face_identification = FaceIdentification.face_bank()
    face_identification.load_model()
    face_identification.get_image(image)
    

    # if args.update:
    #     face_identification.update()
        
    face_identification.identification()