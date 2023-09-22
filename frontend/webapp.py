# Python webapp for the frontend using flask
# Author: Richard Dawson
# Date: 9/21/2023

import sqlite3
import yaml
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config.from_file("config.yaml", load=yaml.safe_load)


def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


def get_item(item_id):
    conn = get_db_connection()
    item = conn.execute("SELECT * FROM items WHERE id = ?", (item_id,)).fetchone()
    conn.close()
    if item is None:
        abort(404)
    return item


@app.route("/")
def index():
    conn = get_db_connection()
    items = conn.execute("SELECT * FROM items").fetchall()
    conn.close()
    return render_template("index.html", items=items)


@app.route("/create", methods=("GET", "POST"))
def create():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        quantity = request.form['quantity']

        if not name:
            flash('A name is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO items (name, description, quantity) VALUES (?, ?,?)',
                         (name, description, quantity))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_item(id)

    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        quantity = request.form['quantity']

        if not name:
            flash('A name is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE items SET name = ?, description = ?, quantity = ?'
                         ' WHERE id = ?',
                         (name, description, quantity, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', item=item)

@app.route("/<int:item_id>")
def item(item_id):
    item = get_item(item_id)
    return render_template("item.html", item=item)
