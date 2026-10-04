from database import save_prediction

test_data = {
    "gender": "female",
    "ethnicity": "group B",
    "reading_score": 72,
    "writing_score": 74,
    "predicted_score": 75.4
}

save_prediction(test_data)