from flask import Flask, request, jsonify

app = Flask(__name__)

# Fake product stock
stock = {
    "laptop": 5
}

# Fake user wallet
wallet = {
    1: 1000
}

# -------------------------
# STEP 1: PLACE ORDER
# -------------------------
@app.route('/buy', methods=['POST'])
def buy():

    user_id = int(request.form.get("user_id"))
    product = request.form.get("product")
    quantity = int(request.form.get("quantity"))

    price = 200  # fixed price per item

    total = price * quantity

    # ❌ NO LIMIT CHECK
    if wallet[user_id] >= total:
        wallet[user_id] -= total
        stock[product] -= quantity

        return jsonify({
            "message": "Order placed successfully",
            "remaining_wallet": wallet[user_id],
            "remaining_stock": stock[product]
        })

    return jsonify({"error": "Insufficient balance"}), 400


# -------------------------
# STEP 2: REDEEM COUPON (NO LIMIT)
# -------------------------
@app.route('/redeem', methods=['POST'])
def redeem():

    user_id = int(request.form.get("user_id"))
    coupon_value = int(request.form.get("value"))

    # ❌ NO REDEEM LIMIT CHECK
    wallet[user_id] += coupon_value

    return jsonify({
        "message": "Coupon redeemed",
        "wallet": wallet[user_id]
    })


# -------------------------
# STEP 3: RESET STOCK (ABUSED FLOW)
# -------------------------
@app.route('/reset-stock', methods=['POST'])
def reset_stock():

    product = request.form.get("product")

    # ❌ NO AUTH CHECK
    stock[product] = 100

    return jsonify({
        "message": "Stock reset done",
        "stock": stock
    })
@app.route('/wallet', methods=['POST'])
def check_wallet():
    user_id = int(request.form.get("user_id"))

    return jsonify({
        "user_id": user_id,
        "wallet_balance": wallet.get(user_id, 0)
    })

if __name__ == '__main__':
    app.run(port=5001)