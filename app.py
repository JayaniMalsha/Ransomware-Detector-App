from flask import Flask, request, render_template_string
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# Define the criteria for ransomware detection
def is_ransomware(row, criteria):
    if (row['Machine'] == criteria.get('Machine', row['Machine']) and 
        row['DebugSize'] == criteria.get('DebugSize', row['DebugSize']) and 
        row['NumberOfSections'] == criteria.get('NumberOfSections', row['NumberOfSections']) and 
        row['MajorImageVersion'] == criteria.get('MajorImageVersion', row['MajorImageVersion']) and 
        row['MajorOSVersion'] == criteria.get('MajorOSVersion', row['MajorOSVersion'])):
        return True
    return False

@app.route('/', methods=['GET', 'POST'])
def index():
    # Define the data as a dictionary
    data = {
        'Machine': [1, 4, 1, 4, 4, 4, 1, 4, 1, 4, 1, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 1, 4, 1, 4, 4, 1, 1, 1, 1, 4],
        'DebugSize': [0, 11, 0, 11, 11, 11, 0, 11, 6, 11, 6, 11, 11, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 6, 11, 6, 10, 10, 11, 11, 6, 6, 6, 11, 11, 11, 11, 11],
        'NumberOfSections': [2, 7, 2, 5, 6, 6, 2, 6, 2, 5, 2, 6, 6, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5, 4, 5, 4, 5, 5, 5, 6, 3, 4, 9, 5, 4, 4, 5, 6],
        'MajorImageVersion': [0, 10, 0, 10, 10, 10, 0, 10, 0, 10, 0, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 6, 10, 6, 6, 6, 10, 10, 6, 6, 0, 0, 10, 10, 10, 10],
        'MajorOSVersion': [4, 10, 4, 10, 10, 10, 4, 10, 4, 10, 4, 6, 10, 10, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 10, 6, 10, 6, 6, 6, 10, 10, 6, 6, 6, 6, 10, 10, 10, 10]
    }

    # Create a DataFrame
    df = pd.DataFrame(data)
    
    # Default criteria
    criteria = {
        'Machine': 4,
        'DebugSize': 11,
        'NumberOfSections': 6,
        'MajorImageVersion': 10,
        'MajorOSVersion': 10
    }

    if request.method == 'POST':
        # Get user input from the form
        criteria = {
            'Machine': int(request.form.get('Machine', criteria['Machine'])),
            'DebugSize': int(request.form.get('DebugSize', criteria['DebugSize'])),
            'NumberOfSections': int(request.form.get('NumberOfSections', criteria['NumberOfSections'])),
            'MajorImageVersion': int(request.form.get('MajorImageVersion', criteria['MajorImageVersion'])),
            'MajorOSVersion': int(request.form.get('MajorOSVersion', criteria['MajorOSVersion']))
        }

    # Add a column 'DebugRVA' to match the function criteria
    df['DebugRVA'] = 0  # Assuming this value is 0 for simplicity

    # Apply the ransomware detection logic
    df['Ransomware'] = df.apply(lambda row: is_ransomware(row, criteria), axis=1)

    # Count the occurrences of Ransomware and Not Ransomware
    counts = df['Ransomware'].value_counts()

    # Create a bar plot
    plt.figure(figsize=(8, 6))
    counts.plot(kind='bar', color=['green', 'red'])
    plt.title('Ransomware Detection Results')
    plt.xlabel('Classification')
    plt.ylabel('Number of Instances')
    plt.xticks(ticks=[0, 1], labels=['Not ransomware', 'Ransomware'], rotation=0)

    # Save plot to a BytesIO object
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()

    # Encode image in base64
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')

    # Render the HTML template with the plot and form
    html = '''
    <!DOCTYPE html>
<html>
<head>
    <title>Ransomware Detection</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            text-align: center;
        }
        h1 {
            font-family: Arial, sans-serif;
            font-size: 2.5em; 
            color: #333; 
            margin-top: 20px; 
            margin-bottom: 20px; 
            text-align: center;
            font-weight: bold; 
        }
        form {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            display: inline-block;
            margin: 20px auto;
            text-align: left;
        }
        input[type="number"] {
            width: 100px;
            padding: 8px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        input[type="submit"] {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 4px;
        }
        input[type="submit"]:hover {
            background-color: #45a049;
        }
        img {
            margin-top: 20px;
            max-width: 90%;
            height: auto;
            border: 1px solid #ddd;
            border-radius: 8px;
        }
    </style>
</head>
<body>
    <h1>Ransomware Detection Results</h1>
    <form method="post">
        Machine: <input type="number" name="Machine" value="{{ criteria['Machine'] }}"><br>
        DebugSize: <input type="number" name="DebugSize" value="{{ criteria['DebugSize'] }}"><br>
        NumberOfSections: <input type="number" name="NumberOfSections" value="{{ criteria['NumberOfSections'] }}"><br>
        MajorImageVersion: <input type="number" name="MajorImageVersion" value="{{ criteria['MajorImageVersion'] }}"><br>
        MajorOSVersion: <input type="number" name="MajorOSVersion" value="{{ criteria['MajorOSVersion'] }}"><br>
        <input type="submit" value="Update">
    </form>
    <br>
    <img src="data:image/png;base64,{{ plot_url }}" alt="Ransomware Detection Results">
</body>
</html>

    '''
    return render_template_string(html, plot_url=plot_url, criteria=criteria)

if __name__ == '__main__':
    app.run(debug=True)
