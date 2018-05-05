from flask import *
from pymongo import MongoClient
import json
'''Flask '''
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
'''Mongo DB Connection'''

client = MongoClient('mongodb://main:rcb#123@ds257627.mlab.com:57627/pbl_farming')
db = client.pbl_farming
farmer_details = db.farmer_details
survey_details = db.survey_details

'''Index page route'''
@app.route("/",methods=["GET","POST"])
def index():
    #variables
    survey_no_list = []
    for survey_number in survey_details.find():
        survey_no_list.append(survey_number["surveyno"])

    crop_list=[]
    for farrmer_entry in farmer_details.find():
        crop_list.append(farrmer_entry["ccrop"])
    crop_list=list(set(crop_list))
    #get method
    if request.method=="GET":
        #get the drop down list
       return render_template("index.html", survey_no_list=survey_no_list,crop_list=crop_list)

    #post method
    if request.method=="POST":

        #get the survey no.and query the db accordingly
        survey_no_selected=request.form.get("survey_dropdown");
        land_details=survey_details.find_one({"surveyno":survey_no_selected})
        print(survey_no_selected + " is selected  and land details \n"+str(land_details))
        land_details.pop('_id')
        print(land_details)

        #get the crop detail and query the db accordingly


        return render_template("index.html",land_details=land_details["coordinates"],survey_no_list=survey_no_list,crop_list=crop_list)


'''Farmer Registeration : pushing data to mlab mongo database'''
@app.route('/farmerRegistration', methods=["GET","POST"])
def farmer_registration():
    if request.method=="GET":
        return render_template("farmer_reg.html")
    if request.method=="POST":
        survey_no=request.form["survey_no"].upper()
        farmer_name=request.form["name"].upper()
        farmer_age=request.form["age"].upper()
        farmer_phno=request.form["phone"].upper()
        agri_area=request.form["area"].upper()
        agri_soil=request.form["soil_type"].upper()
        agri_irrigation=request.form["irrigation_type"].upper()
        agri_ccrop=request.form["current_crop"].upper()
        agri_prev_crop=request.form["prev_crop"].upper()
        agri_cattles=request.form["cattle"].upper()

        #spliting the agri_prev_crop with , as del
        agri_pcrop=agri_prev_crop.split(",")
        print(agri_pcrop)
        print(".........................................................")
        print(survey_no+farmer_age+farmer_name+farmer_phno+agri_area+agri_soil+agri_irrigation+agri_ccrop+agri_prev_crop+agri_cattles)
        print(".........................................................")




        #get the geojson data

        geo_data=survey_details.find_one({"surveyno":request.form["survey_no"]})
        agri_geodata=geo_data["coordinates"]
        print(geo_data)


        #create the document for collection
        farmer_details_data={
            "surveyno":survey_no,
            "name":farmer_name,
            "age":farmer_age,
            "phone_no":farmer_phno,
            "area":agri_area,
            "soil_type":agri_soil,
            "irrigation":agri_irrigation,
            "ccrop":agri_ccrop,
            "pcrop":agri_pcrop,
            "coordinates":agri_geodata,
            "no_of_cattles":agri_cattles
        }
        obj_id=farmer_details.insert_one(farmer_details_data).inserted_id;
        print(obj_id)
        return render_template("farmer_reg.html")
if __name__ == '__main__':
    app.run()
