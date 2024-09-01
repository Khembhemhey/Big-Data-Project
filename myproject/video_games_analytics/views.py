
# Create your views here.
from django.shortcuts import render

import pandas as pd

def index(request):
    game_data = None  # Initialize variable to hold game data
    
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        
        # Check if the uploaded file is a CSV file
        if not csv_file.name.endswith('.csv'):
            return HttpResponse('File is not a CSV')

        # Use pandas to read the CSV file
        try:
            df = pd.read_csv(csv_file)
            # Now you have a DataFrame 'df' containing your CSV data
            # You can pass this data to the template for rendering
            game_data = df.to_dict(orient='records')
            
            # Example: Saving DataFrame to database
            # df.t_osql('your_table_name', your_database_connection, if_exists='append', index=False)
            
        except pd.errors.ParserError as e:
            return HttpResponse(f'Error parsing CSV file: {e}')
    
    return render(request, 'index.html', {'game_data': game_data})


def analytics(request):
    return render(request, 'video_games_analytics/analytics.html')
