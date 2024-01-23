from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

def predict_behaviour(data):
    result = ''

    #Defining features for the product and purchase intrest
    product_features = ['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts','MntSweetProducts', 'MntGoldProds']
    purchase_features = ['NumDealsPurchases','NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases','NumWebVisitsMonth',]

    #Extracting data from the main data
    product_intrest_data = data[product_features]
    purchase_intrest_data = data[purchase_features]

    #importing the model
    #Finding the Product Intrest
    with open('model\product_model.pkl' , 'rb') as model:
        prod_model = pickle.load(model)
        product_intrest = prod_model.predict(product_intrest_data)

        #Finding the Purchase Intrest
        if product_intrest == 0:
            result+=("This person seems to have a balanced spending pattern with a focus on wines and meat product")

        elif product_intrest == 1:
            result+=("This person product intrest is  a frugal and minimalistic spending behavior on all the products")
        
        elif product_intrest == 2:
            result+=("This person appears to be enthusiasts in terms of spending on wines, meat, and fish products.")
        
        elif product_intrest == 3:
            result+=("This person unique intrest with a diverse and relatively high spending pattern across all product categories.")


    #Finding the Purchase Intrest
    with open('model\purchase_model.pkl' , 'rb') as model_1:
        pur_model = pickle.load(model_1)
        purchase_intrest = pur_model.predict(purchase_intrest_data)
        
        #Finding the Purchase Intrest
        if purchase_intrest == 0:
            result+=(" and have a Balanced mix of online and in-store purchases, with an emphasis on store purchases")

        elif purchase_intrest == 1:
            result+=(" and have a Strong focus on online activities, especially web visits, with fewer catalog purchases.")
        
        elif purchase_intrest == 2:
            result+=(" and have a Diverse mix of purchases, with a strong emphasis on deals and web transactions.")

    return result


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve all form values dynamically
    form_data = {field: request.form.get(field) for field in request.form}
    data = pd.DataFrame.from_dict(form_data, orient='index').transpose()
    result = predict_behaviour(data)
    print(result)
    # Render the result on the same page
    return render_template('result.html' , result = result)

if __name__ == '__main__':
    app.run(debug=True)
