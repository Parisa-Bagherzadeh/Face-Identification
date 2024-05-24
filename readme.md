## Face Identification  
This is a python package that identify faces on an image.  
### How to install  
```
pip install face-identification
```
### Usage  
First of all it's needed to create a face_bank, a .npy file containing name and the 512D feature vector of each person.
You can add new feature vector by putting your images of each person in face_bank folder then create a folder named input and put an image including the persons you have added in the face_bank folder and running the following commands :  
```
from face_identification import face_identification  
face_identification.main()
```  
The directory of each folder:
``` 
face_bank
│
└───Harry
│   │   Harry_1.jpg
│   │   Harry_2.jpg
│   │   ...
│   
└───Zayn
│   │   Zayn_1.jpg
│   │   Zayn_2.jpg
│   │   ...
│
│
...  
```
```
input
│
└───one_direction.jpg
```

#### Output 
![Sample Image](output/output.png) 