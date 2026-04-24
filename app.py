from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)

# In-memory storage
crops = []

@app.route('/')
def home():
    return render_template('index.html', crops=crops)

# Add crop (Farmer)
@app.route('/add', methods=['POST'])
def add():
    crop = {
        "id": len(crops) + 1,
        "name": request.form['name'],
        "price": request.form['price'],
        "quantity": int(request.form['quantity']),
        "farmer": request.form['farmer']
    }
    crops.append(crop)
    return redirect('/')

# Buyer page
@app.route('/buy')
def buy():
    return render_template('buy.html', crops=crops)

# Buy crop (reduce quantity)
@app.route('/purchase/<int:id>', methods=['POST'])
def purchase(id):
    for crop in crops:
        if crop["id"] == id:
            qty = int(request.form['buy_qty'])
            if qty <= crop["quantity"]:
                crop["quantity"] -= qty
                return redirect('/buy')
    return "Invalid purchase"

if __name__ == '__main__':
    app.run(debug=True)