from deepface import DeepFace

obj = DeepFace.analyze(img_path = "erika.jpg", actions = ['age', 'gender', 'race', 'emotion'])

print (obj)