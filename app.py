from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple disease prediction database
disease_database = {
    'COVID-19': ['fever', 'cough', 'fatigue', 'shortness_of_breath', 'loss_of_taste', 'body_aches'],
    'Common Cold': ['sore_throat', 'runny_nose', 'cough', 'sneezing', 'mild_fever', 'congestion'],
    'Migraine': ['headache', 'nausea', 'dizziness', 'sensitivity_to_light', 'blurred_vision', 'fatigue'],
    'Allergy': ['rash', 'itching', 'swelling', 'sneezing', 'watery_eyes', 'congestion'],
    'Heart Disease': ['chest_pain', 'shortness_of_breath', 'fatigue', 'irregular_heartbeat', 'dizziness', 'sweating'],
    'Flu': ['fever', 'cough', 'body_aches', 'fatigue', 'headache', 'sore_throat'],
    'Food Poisoning': ['nausea', 'vomiting', 'diarrhea', 'stomach_cramps', 'fever', 'weakness'],
    'Asthma': ['wheezing', 'shortness_of_breath', 'chest_tightness', 'cough', 'fatigue', 'anxiety'],
    'Diabetes': ['excessive_thirst', 'frequent_urination', 'fatigue', 'blurred_vision', 'hunger', 'weight_loss'],
    'Hypertension': ['headache', 'dizziness', 'chest_pain', 'shortness_of_breath', 'anxiety', 'fatigue'],
    'Depression': ['fatigue', 'loss_of_interest', 'sleep_problems', 'anxiety', 'sadness', 'concentration_problems'],
    'Anxiety Disorder': ['anxiety', 'panic', 'rapid_heartbeat', 'sweating', 'trembling', 'concentration_problems'],
    'Gastritis': ['stomach_pain', 'nausea', 'bloating', 'indigestion', 'loss_of_appetite', 'vomiting'],
    'Bronchitis': ['cough', 'chest_congestion', 'fatigue', 'mild_fever', 'shortness_of_breath', 'wheezing'],
    'Arthritis': ['joint_pain', 'stiffness', 'swelling', 'reduced_mobility', 'weakness', 'fatigue']
}

# List of all symptoms (automatically generated from disease database)
symptoms_list = sorted(list(set(
    symptom
    for symptoms in disease_database.values()
    for symptom in symptoms
)))

def predict_disease(symptoms):
    # Calculate match score for each disease
    disease_scores = {}
    
    for disease, disease_symptoms in disease_database.items():
        # Count matching symptoms
        matching_symptoms = set(symptoms).intersection(set(disease_symptoms))
        match_count = len(matching_symptoms)
        
        # Calculate score as percentage of disease symptoms matched
        if match_count > 0:
            score = (match_count / len(disease_symptoms)) * 100
            disease_scores[disease] = score
    
    # Find the disease with highest score
    if disease_scores:
        predicted_disease = max(disease_scores.items(), key=lambda x: x[1])
        return predicted_disease[0], predicted_disease[1]
    else:
        return "Unknown", 0

@app.route('/')
def home():
    return render_template('index.html', symptoms=symptoms_list)

@app.route('/predict', methods=['POST'])
def predict():
    selected_symptoms = request.json.get('symptoms', [])
    if not selected_symptoms:
        return jsonify({'error': 'No symptoms provided'}), 400
    
    predicted_disease, confidence = predict_disease(selected_symptoms)
    
    return jsonify({
        'disease': predicted_disease,
        'confidence': round(confidence, 2)
    })

if __name__ == '__main__':
    app.run(debug=True) 