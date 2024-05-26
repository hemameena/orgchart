from .models import ChartData

def get_team_members():
    return ChartData.query.all()
