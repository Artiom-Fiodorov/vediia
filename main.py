from deepface import DeepFace
import json



def face_verify(img_1, img_2):
    try:
        result_dict = DeepFace.verify(img1_path=img_1,img2_path=img_2)

        with open('result_dict', 'w') as file:
            json.dump(result_dict, file, indent=4,ensure_ascii=False)


        if result_dict.get('verified'):
            return 'Galit praeiti'
        return 'Negali praeiti'

    except Exception as _ex:
        return _ex



def face_analyze():
    result_dict = DeepFace.analyze(img_path='faces/art4.jpg', actions=['age','gender','race','emotion'])

    print(f'[+] Age: {result_dict.get("age")}')
    print(f'[+] Gender: {result_dict.get("gender")}')
    print('[+] Race:')

    for k, v in result_dict.get('race').items():
        print(f'{k} - {round(v, 2)}%')

    print('[+] Emotions:')

    for k, v in result_dict.get('emotion').items():
        print(f'{k} - {round(v, 2)}%')


print(face_analyze())
