import pickle

print("Hello! I am Pritam's AI Assistant")


with open('bill_model.pkl', 'rb') as f:
    model = pickle.load(f)

amount = float(input("Enter your bill amount: "))
prediction = model.predict([[amount]])
print(f"AI Prediction: {prediction}")