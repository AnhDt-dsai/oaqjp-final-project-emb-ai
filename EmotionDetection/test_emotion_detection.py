from emotion_detection import emotion_detector

test_cases = [["I am glad this happened", "joy"],
              ["I am really mad about this", "anger"],
              ["I feel disgusted just hearing about this", "disgust"],
              ["I am so sad about this", "sadness"],
              ["I am really afraid that this will happen", "fear"]]

def run_test(test_cases):
    count = 0
    for test_case in test_cases:
        print("=======================")
        statement, emotion = test_case
        pred_dict = emotion_detector(statement)
        pred_dict = {key: value for key, value in sorted(pred_dict.items(), key=lambda item: item[1])}
        pred = list(pred_dict)[-1]
        print(f"Statement: {statement}\nActual: {emotion}\nPredict: {pred}")
        if pred == emotion: count += 1
    
    print(f"Accuracy = {count/len(test_cases)*100}%")

run_test(test_cases)
	
	
	
	