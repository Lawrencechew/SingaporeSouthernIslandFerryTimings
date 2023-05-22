from flask import Flask, request, jsonify

app = Flask(__name__)

ferry_schedule = ferry_schedule = [
    {
        "company": "Singapore Island Cruise and Ferry Services",
        "routes": [
            {
                "start": "Marina South Pier",
                "destination": "St John's Island",
                "weekday_times": ["09:00", "10:00", "11:00", "14:00"],
                "weekend_holiday_times": ["09:00", "11:00", "13:00", "15:00", "17:00"]
            },
            {
                "start": "St John's Island",
                "destination": "Kusu Island",
                "weekday_times": ["10:45", "14:45"],
                "weekend_holiday_times": ["09:50", "11:50", "13:50", "15:50", "17:50"]
            },
            {
                "start": "St John's Island",
                "destination": "Marina South Pier",
                "weekday_times": ["15:00", "17:00"],
                "weekend_holiday_times": []
            },
            {
                "start": "Kusu Island",
                "destination": "Marina South Pier",
                "weekday_times": ["12:30", "16:00"],
                "weekend_holiday_times": ["10:15", "12:15", "14:15", "16:15", "18:15"]
            }
        ]
    },
    {
        "company": "Marina South Ferries",
        "routes": [
            {
                "start": "Marina South Pier",
                "destination": "St John's Island",
                "weekday_times": ["09:00", "11:00", "13:00"],
                "weekend_holiday_times": ["09:00", "11:00", "13:00"]
            },
            {
                "start": "St John's Island",
                "destination": "Kusu Island",
                "weekday_times": ["09:30", "11:30", "15:30"],
                "weekend_holiday_times": ["09:30", "11:30", "15:30"]
            },
            {
                "start": "Kusu Island",
                "destination": "Marina South Pier",
                "weekday_times": ["10:00", "12:00", "14:00"],
                "weekend_holiday_times": ["10:00", "12:00", "14:00"]
            },
            {
                "start": "Marina South Pier",
                "destination": "Kusu Island",
                "weekday_times": ["15:00", "17:00"],
                "weekend_holiday_times": ["15:00", "17:00"]
            },
            {
                "start": "Kusu Island",
                "destination": "St John's Island",
                "weekday_times": ["15:30", "17:30"],
                "weekend_holiday_times": ["15:30", "17:30"]
            },
            {
                "start": "St John's Island",
                "destination": "Marina South Pier",
                "weekday_times": ["16:00", "18:00"],
                "weekend_holiday_times": ["16:00", "18:00"]
            }
        ]
    }
]

@app.route('/ferry_schedule', methods=['GET'])

def get_ferry_schedule():
    if request.method == 'GET':
        if len(ferry_schedule) >0:
            return jsonify(ferry_schedule)
        else:
            'Nothing Found', 404


if __name__ == '__main__':
    app.run()
