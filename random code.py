
'''      
  
    # Load the pre-trained machine learning model
        #model = joblib.load('model.pkl')

       

       

        return X
    
    def model_prediction(DataFrame)

        prediction = model.predict(X)[0]

        # Use the model to make a prediction on the input data
        #predicted_price = model.predict([input_data])[0]

        # Return the predicted price as a response to the user
        #return render_template('result.html', predicted_price=predicted_price)
    return render_template('predict.html', prediction=prediction)
    #return render_template('pre.html')

input_data = {
            'Lot Frontage': float(lot_frontage),
            'Lot Area': float(lot_area),
            'Lot Config': lot_config,
            'Neighborhood': neighborhood,
            'Bldg Type': bldg_type,
            'House Style': house_style,
            'Overall Qual': int(overall_qual),
            'Overall Cond': int(overall_cond),
            'Year Built': int(year_built),
            'Foundation': foundation,
            'Bsmt Fin SF': int(bsmt_fin_sf),
            'Bsmt Unf SF': int(bsmt_unf_sf),
            'Bsmt Total SF': int(bsmt_total_sf),
            'Central Air': central_air,
            'GrLiv Area ': float(gr_liv_area),
            'FullBath': int(full_bath),
            'HalfBath': int(half_bath),
            'Bedroom AbvGr': int(bedroom_abv_gr),
            'Garage Cars': int(garage_cars)
        }


if request.method == 'POST':
        data = model_data()
        pred = model_pred(data)

@app.route('/predict/', methods=['GET', 'POST'])
def saleprice():
    data = model_data()
    prediction = model_pred(data)
    return render_template('predict.html', prediction=prediction)


@app.route('/')
def Home():
    return render_template('home.html')


@app.route('/model/')
def model_page():
    return render_template('model.html')

@app.route('/predict/', methods=['GET', 'POST'])
def saleprice():
    if request.method == 'POST':
        lot_frontage = request.form['Lot Frontage']
        lot_area = request.form['Lot Area']
        lot_config = request.form['Lot Config']
        neighborhood = request.form['Neighborhood']
        bldg_type = request.form['Bldg Type']
        house_style = request.form['House Style']
        overall_qual = request.form['Overall Qual']
        overall_cond = request.form['Overall Cond']
        year_built = request.form['Year Built']
        foundation = request.form['Foundation']
        bsmt_fin_sf = request.form['BsmtFin SF 1']
        bsmt_unf_sf = request.form['Bsmt Unf SF']
        bsmt_total_sf = request.form['Total Bsmt SF']
        central_air = request.form['Central Air']
        gr_liv_area = request.form['Gr Liv Area']
        full_bath = request.form['Full Bath']
        half_bath = request.form['Half Bath']
        bedroom_abv_gr = request.form['Bedroom AbvGr']
        garage_cars = request.form['Garage Cars']

 # Prepare the input data
        X = pd.DataFrame({
            'Lot Frontage': [lot_frontage],
            'Lot Area': [lot_area],
            'Year Built': [year_built],
            'BsmtFin SF 1': [bsmt_fin_sf],
            'Bsmt Unf SF': [bsmt_unf_sf],
            'Total Bsmt SF': [bsmt_total_sf],
            'Gr Liv Area': [gr_liv_area],
            'Lot Config_Corner': [1 if lot_config == 'Corner' else 0],
            'Lot Config_CulDSac': [1 if lot_config == 'Cul-De-Sac' else 0],
            'Lot Config_FR2': [1 if lot_config == 'FR2' else 0],
            'lot_config_FR3': [1 if lot_config == 'FR3' else 0],
            'lot Config_Inside': [1 if lot_config == 'Inside' else 0],
            'Neighborhood_Blmngtn': [1 if neighborhood == 'Blmngtn' else 0],
            'Neighborhood_Blueste': [1 if neighborhood == 'Blueste' else 0],
            'Neighborhood_BrkSide': [1 if neighborhood == 'BrkSide' else 0],
            'Neighborhood_ClearCr': [1 if neighborhood == 'ClearCr' else 0],
            'Neighborhood_CollgCr': [1 if neighborhood == 'CollgCr' else 0],
            'Neighborhood_Crawfor': [1 if neighborhood == 'Crawfor' else 0],
            'Neighborhood_Edwards': [1 if neighborhood == 'Edwards' else 0],
            'Neighborhood_Gilbert': [1 if neighborhood == 'Gilbert' else 0],
            'Neighborhood_Greens': [1 if neighborhood == 'Greens' else 0],
            'Neighborhood_IDOTRR': [1 if neighborhood == 'IDOTRR' else 0],
            'Neighborhood_MeadowV': [1 if neighborhood == 'MeadowV' else 0],
            'Neighborhood_Mitchel': [1 if neighborhood == 'Mitchel' else 0],
            'Neighborhood_NAmes': [1 if neighborhood == 'NAmes' else 0],
            'Neighborhood_NPkVill': [1 if neighborhood == 'NPkVill' else 0],
            'Neighborhood_NMAmes': [1 if neighborhood == 'NWAmes' else 0],
            'Neighborhood_NoRidge': [1 if neighborhood == 'NoRidge' else 0],
            'Neighborhood_NridgHt': [1 if neighborhood == 'NridgHt' else 0],
            'Neighborhood_OldTown': [1 if neighborhood == 'OldTown' else 0],
            'Neighborhood_SWISU': [1 if neighborhood == 'SWISU' else 0],
            'Neighborhood_Sawyer': [1 if neighborhood == 'Sawyer' else 0],
            'Neighborhood_SawyerW': [1 if neighborhood == 'SawyerW' else 0],
            'Neighborhood_Somerst': [1 if neighborhood == 'Somerst' else 0],
            'Neighborhood_StoneBr': [1 if neighborhood == 'StoneBr' else 0],
            'Neighborhood_Timber': [1 if neighborhood == 'Timber' else 0],
            'Neighborhood_Veeker': [1 if neighborhood == 'Veeker' else 0],
            'Bldg Type_1Fam': [1 if bldg_type == '1Fam' else 0],
            'Bldg Type_2fmCon': [1 if bldg_type == '2fmCon' else 0],
            'Bldg Type_Duplex': [1 if bldg_type == 'Duplex' else 0],
            'Bldg Type_Twinhs': [1 if bldg_type == 'Twnhs' else 0],
            'Bldg Type_TwnhsE': [1 if bldg_type == 'TwnhsE' else 0],
            'House Style_1.5Fin': [1 if house_style == '1.5Fin' else 0],
            'House Style_1.5Unf': [1 if house_style == '1.5Unf' else 0],
            'House Style_1Story': [1 if house_style == '1Story' else 0],
            'House Style_2.5Fin': [1 if house_style == '2.5Fin' else 0],
            'House Style_2.5Unf': [1 if house_style == '2.5Unf' else 0],
            'House Style_2Story': [1 if house_style == '2Story' else 0],
            'House Style_SFoyer': [1 if house_style == 'SFoyer' else 0],
            'House Style_SLvl': [1 if house_style == 'SLvl' else 0],
            'Overall Qual_1': [1 if overall_qual == '1' else 0],
            'Overall Qual_2': [1 if overall_qual == '2' else 0],
            'Overall Qual_3': [1 if overall_qual == '3' else 0],
            'Overall Qual_4': [1 if overall_qual == '4' else 0],
            'Overall Qual_5': [1 if overall_qual == '5' else 0],
            'Overall Qual_6': [1 if overall_qual == '6' else 0],
            'Overall Qual_7': [1 if overall_qual == '7' else 0],
            'Overall Qual_8': [1 if overall_qual == '8' else 0],
            'Overall Qual_9': [1 if overall_qual == '9' else 0],
            'Overall Qual_10': [1 if overall_qual == '10' else 0],
            'Overall Cond_1': [1 if overall_cond == '1' else 0],
            'Overall Cond_2': [1 if overall_cond == '2' else 0],
            'Overall Cond_3': [1 if overall_cond == '3' else 0],
            'Overall Cond_4': [1 if overall_cond == '4' else 0],
            'Overall Cond_5': [1 if overall_cond == '5' else 0],
            'Overall Cond_6': [1 if overall_cond == '6' else 0],
            'Overall Cond_7': [1 if overall_cond == '7' else 0],
            'Overall Cond_8': [1 if overall_cond == '8' else 0],
            'Overall Cond_9': [1 if overall_cond == '9' else 0],
            'Foundation_BrkTil': [1 if foundation == 'BrkTil' else 0],
            'Foundation_CBlock': [1 if foundation == 'CBlock' else 0],
            'Foundation_PConc': [1 if foundation == 'PConc' else 0],
            'Foundation_Slab': [1 if foundation == 'Slab' else 0],
            'Foundation_Stone': [1 if foundation == 'Stone' else 0],
            'Foundation_Wood': [1 if foundation == 'Wood' else 0],
            'Central Air_N': [1 if central_air == 'N' else 0],
            'Central Air_Y': [1 if central_air == 'Y' else 0],
            'Full Bath_0': [1 if full_bath == '0' else 0],
            'Full Bath_1': [1 if full_bath == '1' else 0],
            'Full Bath_2': [1 if full_bath == '2' else 0],
            'Full Bath_3': [1 if full_bath == '3' else 0],
            'Full Bath_4': [1 if full_bath == '4' else 0],
            'Half Bath_0': [1 if half_bath == '0' else 0],
            'Half Bath_1': [1 if half_bath == '1' else 0],
            'Half Bath_2': [1 if half_bath == '2' else 0],
            'Bedroom AbvGr_0': [1 if bedroom_abv_gr == '0' else 0],
            'Bedroom AbvGr_1': [1 if bedroom_abv_gr == '1' else 0],
            'Bedroom AbvGr_2': [1 if bedroom_abv_gr == '2' else 0],
            'Bedroom AbvGr_3': [1 if bedroom_abv_gr == '3' else 0],
            'Bedroom AbvGr_4': [1 if bedroom_abv_gr == '4' else 0],
            'Bedroom AbvGr_5': [1 if bedroom_abv_gr == '5' else 0],
            'Bedroom AbvGr_6': [1 if bedroom_abv_gr == '6' else 0],
            'Garage Cars_0.0': [1 if garage_cars == '0.' else 0],
            'Garage Cars_1.0': [1 if garage_cars == '1.' else 0],
            'Garage Cars_2.0': [1 if garage_cars == '2.' else 0],
            'Garage Cars_3.0': [1 if garage_cars == '3.' else 0],
            'Garage Cars_4.0': [1 if garage_cars == '4.' else 0],
            'Garage Cars_5.0': [1 if garage_cars == '5.' else 0]
            })
        X = X.to_numpy()
        prediction = predict_housing_price(X)

        return prediction

    else:
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
    
    output = {"prediction": prediction[0]}
    return output




if __name__ == "__main__":
    app.run(debug=True)


lot_frontage = request.form['Lot Frontage']
    if lot_frontage:
        lot_frontage = float(lot_frontage)
    else:
        lot_frontage = 0
    lot_area = request.form['Lot Area']
    if lot_area:
        lot_area = float(lot_area)
    else:
        lot_area = 0
    lot_config = request.form['Lot Config']
    neighborhood = request.form['Neighborhood']
    bldg_type = request.form['Bldg Type']
    house_style = request.form['House Style']
    overall_qual = request.form['Overall Qual']
    overall_cond = request.form['Overall Cond']
    year_built = request.form['Year Built']
    if year_built:
        year_built = int(year_built)
    else:
        year_built = 0
    foundation = request.form['Foundation']
    bsmt_fin_sf = request.form['BsmtFin SF 1']
    if bsmt_fin_sf:
        bsmt_fin_sf = float(bsmt_fin_sf)
    else:
        bsmt_fin_sf = 0
    bsmt_unf_sf = request.form['Bsmt Unf SF']
    if bsmt_unf_sf:
        bsmt_unf_sf = float(bsmt_unf_sf)
    else:
        bsmt_unf_sf = 0
    bsmt_total_sf = request.form['Total Bsmt SF']
    if bsmt_total_sf:
        bsmt_total_sf = float(bsmt_total_sf)
    else:
        bsmt_total_sf = 0
    central_air = request.form['Central Air']
    gr_liv_area = request.form['Gr Liv Area']
    if gr_liv_area:
        gr_liv_area = float(gr_liv_area)
    else:
        gr_liv_area = 0
    full_bath = request.form['Full Bath']
    half_bath = request.form['Half Bath']
    bedroom_abv_gr = request.form['Bedroom AbvGr']
    garage_cars = request.form['Garage Cars']
    
    '''