from flask import Flask, request, render_template
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
import webbrowser
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    show_thank_you = False

    # Default form values
    form_values = {
        'gender': '',
        'ethnicity': '',
        'parental_level_of_education': '',
        'lunch': '',
        'test_preparation_course': '',
        'reading_score': '',
        'writing_score': ''
    }

    if request.method == 'POST':
        # Finish button clicked
        if request.form.get('finish'):
            show_thank_you = True
            results = None
            form_values = {key: '' for key in form_values}  # clear form
        # Predict Another clicked
        elif request.form.get('another'):
            results = None
            form_values = {key: '' for key in form_values}  # reset form
        else:
            # Collect form data
            form_values = {
                'gender': request.form.get('gender'),
                'ethnicity': request.form.get('ethnicity'),
                'parental_level_of_education': request.form.get('parental_level_of_education'),
                'lunch': request.form.get('lunch'),
                'test_preparation_course': request.form.get('test_preparation_course'),
                'reading_score': request.form.get('reading_score', ''),
                'writing_score': request.form.get('writing_score', '')
            }

            # Prepare data for prediction
            data = CustomData(
                gender=form_values['gender'],
                race_ethnicity=form_values['ethnicity'],
                parental_level_of_education=form_values['parental_level_of_education'],
                lunch=form_values['lunch'],
                test_preparation_course=form_values['test_preparation_course'],
                reading_score=float(form_values['reading_score'] or 0),
                writting_score=float(form_values['writing_score'] or 0)
            )

            pred_df = data.get_data_as_data_frame()
            pipeline = PredictPipeline()
            results = pipeline.predict(pred_df)[0]

    return render_template('home.html', results=results, show_thank_you=show_thank_you, form=form_values)


if __name__ == '__main__':
    # Get the port from Render environment variable, default to 5000 for local
    port = int(os.environ.get("PORT", 5000))
    # Do not open browser on server
    app.run(host="0.0.0.0", port=port, debug=True)
