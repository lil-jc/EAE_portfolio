import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():

    # Load data into variable
    trans_rows = db.execute("""
        SELECT symbol, SUM(shares) as total_shares
        FROM transactions
        WHERE user_id = :user_id
        GROUP BY symbol
        HAVING total_shares > 0;
        """, user_id=session["user_id"])
    # collect and calculate data
    holdings = []
    grand_total = 0
    # put data into holding
    for row in trans_rows:
        stock = lookup(row["symbol"])
        holdings.append({
            "symbol": stock["symbol"],
            "name": stock["name"],
            "shares": row["total_shares"],
            "price": usd(stock["price"]),
            "total": usd(stock["price"] * row["total_shares"])
        })
        grand_total += stock["price"] * row["total_shares"]
    # get user's cash and calculate grand_total
    cash_rows = db.execute("SELECT cash FROM users WHERE id=:user_id", user_id=session["user_id"])
    cash = cash_rows[0]["cash"]
    grand_total += cash

    # pass data to index.html
    return render_template("index.html", holdings=holdings, cash=usd(cash), grand_total=usd(grand_total))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":

        # Ensure symbol is submitted
        if not request.form.get("symbol"):
            return apology("must provide symbol", 400)

        # Ensure shares is submitted
        elif not request.form.get("shares"):
            return apology("must provide shares", 400)

        # Ensure shares is digit
        elif not request.form.get("shares").isdigit():
            return apology("invalid shares", 400)

        # Ensure symbol exist
        elif not lookup(request.form.get("symbol")):
            return apology("invalid symbol", 400)

        # variables from webpage
        shares = int(request.form.get("shares"))
        stock = lookup(request.form.get("symbol"))
        # variables from SQL
        rows = db.execute("SELECT cash FROM users WHERE id=:id", id=session["user_id"])
        cash = rows[0]["cash"]

        # calculate amount to deduct from cash
        update_cash = cash - shares * stock["price"]
        # Ensure user have sufficient cash
        if update_cash < 0:
            return apology("insufficient cash", 400)
        # update cash
        db.execute("UPDATE users SET CASH=:update_cash WHERE id=:id",
                   update_cash=update_cash,
                   id=session["user_id"])
        # record purchase into transactions
        db.execute("""
            INSERT INTO transactions (user_id, symbol, shares, price)
            VALUES (:user_id, :symbol, :shares, :price)
            """,
                   user_id=session["user_id"],
                   symbol=stock["symbol"],
                   shares=shares,
                   price=stock["price"])
        flash("Bought!")
        # redirect to home page
        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    trans_row = db.execute("""
        SELECT symbol, shares, price, transacted
        FROM transactions
        WHERE user_id=:user_id;
    """, user_id=session["user_id"])
    for i in range(len(trans_row)):
        trans_row[i]["price"] = usd(trans_row[i]["price"])
    return render_template("history.html", transactions=trans_row)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username is submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password is submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 400)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        flash("Logged in!")
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":

        if not request.form.get("symbol"):
            return apology("must provide symbol", 400)

        # Ensure stock is valid
        elif not lookup(request.form.get("symbol").upper()):
            return apology("invalid symbol", 400)

        # look up stock
        stock = lookup(request.form.get("symbol").upper())
        price = usd(stock['price'])

        # pass data to quoted.html
        return render_template("quoted.html", stockinfo={
            'name': stock['name'],
            'symbol': stock['symbol'],
            'price': price})

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # when user summits registration form
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Ensure password is comfirmed
        elif not request.form.get("confirmation"):
            return apology("must confirm password", 400)

        # confirm password
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords must be the same", 400)

        # user username and passwords checked out
        else:

            try:
                # register user in data base
                db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)",
                           username=request.form.get("username"),
                           hash=generate_password_hash(request.form.get("password")))

            except:
                # username already exists
                return apology("user already exists", 400)

            # redirect user to log in
            return redirect("/login")

    # user is got in by GET (let user register)
    else:

        # render register.html
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":

        # Ensure shares is submitted
        if not request.form.get("shares"):
            return apology("must provide shares", 400)

        # Ensure shares is digit
        elif not request.form.get("shares").isdigit():
            return apology("invalid shares", 400)

        # variables from webpage
        symbol = request.form.get("symbol").upper()
        shares = int(request.form.get("shares"))
        stock = lookup(request.form.get("symbol"))
        # variables from SQL
        rows = db.execute("""
            SELECT symbol, SUM(shares) as total_shares
            FROM transactions
            WHERE user_id=:user_id
            GROUP BY symbol
            HAVING total_shares > 0;
        """, user_id=session["user_id"])
        # Ensure user only sell what they have
        for row in rows:
            if row["symbol"] == symbol and shares >= row["total_shares"]:
                return apology("invalid shares", 400)

        cash_rows = db.execute("SELECT cash FROM users WHERE id=:id", id=session["user_id"])
        cash = cash_rows[0]["cash"]

        # calculate amount to deduct from cash
        update_cash = cash + shares * stock["price"]
        # update cash
        db.execute("UPDATE users SET CASH=:update_cash WHERE id=:id",
                   update_cash=update_cash,
                   id=session["user_id"])
        # record sold into transactions
        db.execute("""
            INSERT INTO transactions (user_id, symbol, shares, price)
            VALUES (:user_id, :symbol, :shares, :price)
            """,
                   user_id=session["user_id"],
                   symbol=stock["symbol"],
                   shares=-1 * shares,
                   price=stock["price"])
        flash("Sold!")
        # redirect to home page
        return redirect("/")

    else:
        # Load data into variable
        trans_rows = db.execute("""
        SELECT symbol, SUM(shares) as total_shares
        FROM transactions
        WHERE user_id = :user_id
        GROUP BY symbol
        HAVING total_shares > 0;
        """, user_id=session["user_id"])
        # pass data to sell.html
        return render_template("sell.html", symbols=[row["symbol"] for row in trans_rows])


# Add cash page
@app.route("/add_cash", methods=["GET", "POST"])
@login_required
def add_cash():
    if request.method == "POST":

        # Ensure amount is not negative
        if int(request.form.get("add_cash")) < 1:
            return apology("invalid cash", 400)

        # Add amount to cash
        db.execute("""
            UPDATE users
            SET cash = cash + :amount
            WHERE id=:user_id
        """,
                   amount=int(request.form.get("add_cash")),
                   user_id=session["user_id"])

        # notify and redirect
        flash("Cash added!")
        return redirect("/")
    else:
        return render_template("add_cash.html")