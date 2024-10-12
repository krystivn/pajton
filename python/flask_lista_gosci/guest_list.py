from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista wiadomości w księdze gości
guestbook_entries = []

@app.route('/')
def index():
    # Renderujemy stronę główną i przekazujemy listę wiadomości
    return render_template('index.html', entries=guestbook_entries)

@app.route('/add', methods=['POST'])
def add_entry():
    # Pobieramy imię i wiadomość z formularza
    name = request.form['name']
    message = request.form['message']
    
    # Dodajemy nowy wpis do listy księgi gości
    guestbook_entries.append({'name': name, 'message': message})
    
    # Przekierowanie na stronę główną po dodaniu wpisu
    return redirect(url_for('index'))

# Uruchomienie aplikacji
if __name__ == '__main__':
    app.run(debug=True)
