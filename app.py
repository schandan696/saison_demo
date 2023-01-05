from src.data.model import getFoodTrucksByApplicantName
from src.view.index import app



# print(getFoodTrucksByApplicantName('Golden ate Halal od'))
app.run(host='0.0.0.0', debug = True, port=3000)