from flask import Flask, render_template, url_for, request
import joblib
import pandas as pd

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('home.html')


@app.route('/model/')
def model_page():
    return render_template('model.html')

def predict_housing_price(input_data):
    try:
        model = joblib.load('housing_price_model_nn2.joblib')
    except:
        return "Error loading model"
    
    try:
        prediction = model.predict(input_data)
    except:
        return "Error making prediction"
    
    return prediction[0]


@app.route('/predict/', methods=['GET', 'POST'])
def saleprice():
    #if request.method == 'POST':
# Prepare the input data
    LotFrontage = request.form['Lot Frontage']
    LotArea = request.form['Lot Area']
    LotConfig = request.form['Lot Config']
    Neighborhood = request.form['Neighborhood']
    BldgType = request.form['Bldg Type']
    HouseStyle = request.form['House Style']
    OverallQual = request.form['Overall Qual']
    OverallCond = request.form['Overall Cond']
    YearBuilt = request.form['Year Built']
    Foundation = request.form['Foundation']
    BsmtFinSF = request.form['BsmtFin SF 1']
    BsmtUnfSF = request.form['Bsmt Unf SF']
    BsmtTotalSF = request.form['Total Bsmt SF']
    CentralAir = request.form['Central Air']
    GrLivArea = request.form['Gr Liv Area']
    FullBath = request.form['Full Bath']
    HalfBath = request.form['Half Bath']
    BedroomAbvGr = request.form['Bedroom AbvGr']
    GarageCars = request.form['Garage Cars']
    
    #prediction = predict_housing_price(test_pred)
    lot_frontage = float(LotFrontage)
    lot_area = float(LotArea)
    lot_config = str(LotConfig)
    neighborhood = str(Neighborhood)
    bldg_type = str(BldgType)
    house_style = str(HouseStyle)
    overall_qual = str(OverallQual)
    overall_cond = str(OverallCond)
    year_built = float(YearBuilt)
    foundation = str(Foundation)
    bsmt_fin_sf = float(BsmtFinSF)
    bsmt_unf_sf = float(BsmtUnfSF)
    bsmt_total_sf = float(BsmtTotalSF)
    central_air = str(CentralAir)
    gr_liv_area = float(GrLivArea)
    full_bath = str(FullBath)
    half_bath = str(HalfBath)
    bedroom_abv_gr = str(BedroomAbvGr)
    garage_cars = str(GarageCars)

    input_data = [[
        [lot_frontage],
        [lot_area],
        [year_built],
        [bsmt_fin_sf],
        [bsmt_unf_sf],
        [bsmt_total_sf],
        [gr_liv_area],
        [1 if lot_config == 'Corner' else 0],
        [1 if lot_config == 'Cul-De-Sac' else 0],
        [1 if lot_config == 'FR2' else 0],
        [1 if lot_config == 'FR3' else 0],
        [1 if lot_config == 'Inside' else 0],
        [1 if neighborhood == 'Blmngtn' else 0],
        [1 if neighborhood == 'Blueste' else 0],
        [1 if neighborhood == 'BrkSide' else 0],
        [1 if neighborhood == 'ClearCr' else 0],
        [1 if neighborhood == 'CollgCr' else 0],
        [1 if neighborhood == 'Crawfor' else 0],
        [1 if neighborhood == 'Edwards' else 0],
        [1 if neighborhood == 'Gilbert' else 0],
        [1 if neighborhood == 'Greens' else 0],
        [1 if neighborhood == 'IDOTRR' else 0],
        [1 if neighborhood == 'MeadowV' else 0],
        [1 if neighborhood == 'Mitchel' else 0],
        [1 if neighborhood == 'NAmes' else 0],
        [1 if neighborhood == 'NPkVill' else 0],
        [1 if neighborhood == 'NWAmes' else 0],
        [1 if neighborhood == 'NoRidge' else 0],
        [1 if neighborhood == 'NridgHt' else 0],
        [1 if neighborhood == 'OldTown' else 0],
        [1 if neighborhood == 'SWISU' else 0],
        [1 if neighborhood == 'Sawyer' else 0],
        [1 if neighborhood == 'SawyerW' else 0],
        [1 if neighborhood == 'Somerst' else 0],
        [1 if neighborhood == 'StoneBr' else 0],
        [1 if neighborhood == 'Timber' else 0],
        [1 if neighborhood == 'Veeker' else 0],
        [1 if bldg_type == '1Fam' else 0],
        [1 if bldg_type == '2fmCon' else 0],
        [1 if bldg_type == 'Duplex' else 0],
        [1 if bldg_type == 'Twnhs' else 0],
        [1 if bldg_type == 'TwnhsE' else 0],
        [1 if house_style == '1.5Fin' else 0],
        [1 if house_style == '1.5Unf' else 0],
        [1 if house_style == '1Story' else 0],
        [1 if house_style == '2.5Fin' else 0],
        [1 if house_style == '2.5Unf' else 0],
        [1 if house_style == '2Story' else 0],
        [1 if house_style == 'SFoyer' else 0],
        [1 if house_style == 'SLvl' else 0],
        [1 if overall_qual == '1' else 0],
        [1 if overall_qual == '2' else 0],
        [1 if overall_qual == '3' else 0],
        [1 if overall_qual == '4' else 0],
        [1 if overall_qual == '5' else 0],
        [1 if overall_qual == '6' else 0],
        [1 if overall_qual == '7' else 0],
        [1 if overall_qual == '8' else 0],
        [1 if overall_qual == '9' else 0],
        [1 if overall_qual == '10' else 0],
        [1 if overall_cond == '1' else 0],
        [1 if overall_cond == '2' else 0],
        [1 if overall_cond == '3' else 0],
        [1 if overall_cond == '4' else 0],
        [1 if overall_cond == '5' else 0],
        [1 if overall_cond == '6' else 0],
        [1 if overall_cond == '7' else 0],
        [1 if overall_cond == '8' else 0],
        [1 if overall_cond == '9' else 0],
        [1 if foundation == 'BrkTil' else 0],
        [1 if foundation == 'CBlock' else 0],
        [1 if foundation == 'PConc' else 0],
        [1 if foundation == 'Slab' else 0],
        [1 if foundation == 'Stone' else 0],
        [1 if foundation == 'Wood' else 0],
        [1 if central_air == 'N' else 0],
        [1 if central_air == 'Y' else 0],
        [1 if full_bath == '0' else 0],
        [1 if full_bath == '1' else 0],
        [1 if full_bath == '2' else 0],
        [1 if full_bath == '3' else 0],
        [1 if full_bath == '4' else 0],
        [1 if half_bath == '0' else 0],
        [1 if half_bath == '1' else 0],
        [1 if half_bath == '2' else 0],
        [1 if bedroom_abv_gr == '0' else 0],
        [1 if bedroom_abv_gr == '1' else 0],
        [1 if bedroom_abv_gr == '2' else 0],
        [1 if bedroom_abv_gr == '3' else 0],
        [1 if bedroom_abv_gr == '4' else 0],
        [1 if bedroom_abv_gr == '5' else 0],
        [1 if bedroom_abv_gr == '6' else 0],
        [1 if garage_cars == '0.' else 0],
        [1 if garage_cars == '1.' else 0],
        [1 if garage_cars == '2.' else 0],
        [1 if garage_cars == '3.' else 0],
        [1 if garage_cars == '4.' else 0],
        [1 if garage_cars == '5.' else 0]
    ]]

    '''test_pred = [[705, 8765, 2005, 450, 200, 900, 1850, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 
            0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 
            0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 
            0, 0, 1, 0, 0, 0]]'''

    prediction = predict_housing_price(input_data)

    return render_template('predict.html', prediction=prediction)
    #else:
       # return render_template('predict.html')


if __name__ == "__main__":
    app.run(debug=True)