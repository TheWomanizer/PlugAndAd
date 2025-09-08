from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import random
from datetime import datetime, timedelta


class AdsSummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        platform = request.query_params.get('platform', '')
        date_range = request.query_params.get('range', '30')
        
        # Mock data - in real implementation, this would fetch from ad platforms APIs
        mock_data = {
            'spend': round(random.uniform(5000, 25000), 2),
            'impressions': random.randint(50000, 500000),
            'clicks': random.randint(2000, 15000),
            'conversions': random.randint(100, 800),
            'roas': round(random.uniform(2.5, 6.8), 1),
            'ctr': round(random.uniform(1.2, 4.5), 2),
            'cpc': round(random.uniform(0.8, 3.2), 2),
            'platform': platform or 'all',
            'date_range': f"{date_range} days"
        }
        
        return Response(mock_data)


class AdsTimeseriesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        metric = request.query_params.get('metric', 'spend')
        date_range = int(request.query_params.get('range', '30'))
        
        # Generate mock timeseries data
        end_date = datetime.now()
        dates = []
        values = []
        
        for i in range(date_range):
            date = end_date - timedelta(days=date_range - i - 1)
            dates.append(date.strftime('%Y-%m-%d'))
            
            # Generate realistic mock values based on metric
            if metric == 'spend':
                values.append(round(random.uniform(100, 1000), 2))
            elif metric == 'impressions':
                values.append(random.randint(1000, 20000))
            elif metric == 'clicks':
                values.append(random.randint(50, 800))
            elif metric == 'conversions':
                values.append(random.randint(5, 50))
            elif metric == 'roas':
                values.append(round(random.uniform(2.0, 8.0), 1))
            else:
                values.append(round(random.uniform(0, 100), 2))
        
        mock_data = {
            'metric': metric,
            'date_range': f"{date_range} days",
            'data': [
                {'date': date, 'value': value}
                for date, value in zip(dates, values)
            ]
        }
        
        return Response(mock_data)
