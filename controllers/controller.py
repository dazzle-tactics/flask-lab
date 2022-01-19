from flask import render_template
from app import app
from models.order_list import orders


@app.route('/')
def index():
    return render_template('index.html', title='Home', activeOrders = orders)

@app.route('/orders')
def page():
    return render_template('order.html', title='Order', activeOrders = orders)    