from tkinter import * 
import requests
import json

root = Tk()
root.title('Tkinter GUI - Sailendra')
# root.geometry('600x100')

# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&API_KEY=E38E6EB3-93B2-4795-9982-79723D3DC0BD
# 89129  83814  83530 70801 93263

#create zipLookup function

def zipLookup():
    try:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+ zip.get() + "&distance=25&API_KEY=E38E6EB3-93B2-4795-9982-79723D3DC0BD") 
        api = json.loads(api_request.content)

        city = api[0]['ReportingArea'] 
        quality = api[0]['AQI']
        category =  api[1]['Category']['Name']

        if category == "Good":
            wheather_color = '#0C0'

        elif category == "Moderate":
            wheather_color = '#FFFF00'

        elif category == "Unhealthy for Sensitive Groups":
            wheather_color = '#ff9900'


        elif category == "Unhealthy":
            wheather_color = '#FF0000'

        elif category == "Very Unhealthy":
            wheather_color = '#990066'

        elif category == "Hazardous":
            wheather_color = '#660000'


        root.configure(background= wheather_color)

        myLabel = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font="Helvetica 20", background=wheather_color)
        myLabel.grid(row=1, column=0, columnspan=2) 

    except Exception as e: 
        api = "Error..."


zip = Entry(root)
zip.grid(row=0, column=0, sticky="wens")

zip_button = Button(root, text="Lookup Zipcode", command=zipLookup)
zip_button.grid(row=0, column=1, sticky="wens")

root.mainloop()