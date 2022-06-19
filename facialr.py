from deepface import DeepFace

obj = DeepFace.analyze(img_path = "prueba.jpg", actions = ['age', 'gender', 'race', 'emotion'])

print (obj)