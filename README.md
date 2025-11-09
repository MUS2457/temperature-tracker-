🌤 Temperature & Weather Tracker

A Python project that allows users to track temperatures and weather types for multiple cities, generate summaries, and save results in both readable text and structured JSON formats.

Project Versions
Version 1 (v1)

Lets the user enter temperatures for days of the week.

Finds the hottest and coldest days.

Calculates the average temperature.

Saves data to temperatures.txt.

Version 2 (v2)

Tracks multiple cities with both temperature and weather type.

Finds the hottest, coldest, and average city temperatures.

Saves detailed weather reports to weather.txt.

Version 3 (v3)

Uses nested dictionaries to store data: city → {temperature, type}.

Automatically calculates hottest, coldest, and average temperature.

Adds a timestamp for each entry.

Nicely formatted report with clear line spacing.

Saves data to weather.txt in append mode for history.

Version 4 (v4)

Enter multiple cities with their temperature and weather type.

Input validation:

Prevent empty city names.

Reject non-numeric temperature entries.

Automatically calculates:

Hottest and coldest city

Total number of cities

Sum and average of temperatures

Counts of each weather type

Saves results in:

weather v4.txt → readable text format

weather v4.json → structured JSON format

Displays a summary in the terminal.

🛠 Features

User-friendly input for multiple cities.

Automatic calculations for min, max, and average.

Error handling for invalid input.

Data storage in both human-readable and machine-readable formats.

📂 Files Generated

weather v4.txt → A readable history of all city entries with summary.

weather v4.json → A structured JSON file containing all statistics and city data.
