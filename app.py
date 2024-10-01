from flask import Flask, render_template, url_for, flash, redirect, request
from flask_mail import Mail, Message


app = Flask(__name__)
app.secret_key = '1234'  

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'punitsinha495@gmail.com'  
app.config['MAIL_PASSWORD'] = 'yhih rgyj nkkl sunj'  
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


shoes = [
    {
        "id": 1,
        "name": "Airforce1",
        "description": "Taking height and craft to new levels, the Nike Air Force 1 Sage Low re-imagines classic hoops styleby and for women.A clean leather upper is easy to style.The sculpted collar reduces hot spots.And its platform midsole adds unflinching boldness because we know: you're not just in the game, you're leading it.",
        "price": "1,600",
        "images": ["Af 1 1600.JPG", "Af1.JPG", "Af11600.JPG"]  
    },
    {
        "id": 2,
        "name": "Dunk Low Retro Unisex Shoes",
        "description": "This is a description for shoe 2.",
        "price": "2,000",
        "images": ["Dunk panda 2000.WEBP", "Dunk panda 2000 2.WEBP"]
    },
    {
        "id": 3,
        "name": "Jordan Air",
        "description": "This is a description for shoe 3.",
        "price": "2,000",
        "images": ["jordan-air-jordan-1-retro-high-og-chicago-lost-and-found_18316489_45637604_1000.webp", "jordan-air-jordan-1-retro-high-og-chicago-lost-and-found_18316489_45638485_1000.webp", "jordan-air-jordan-1-retro-high-og-chicago-lost-and-found_18316489_45638492_1000.webp", "jordan-air-jordan-1-retro-high-og-chicago-lost-and-found_18316489_45638527_1000.webp"]
    },
    {
        "id": 4,
        "name": "Converse Black",
        "description": "This is a description for shoe 4.",
        "price": "1,000",
        "images": ["metro-fusion-converse-chuck-taylor-all-star-hi-top-black-3-5-m-5-5-w-m9160-shoes-948_1400x1400.webp"]
    },
    {
        "id": 5,
        "name": "Jordan 1 High Spider-Man",
        "description": "This is a description for shoe 5.",
        "price": "2,100",
        "images": ["Spider 2100.JPG", "pinterestdownloader.com-1727612213.688505.jpg", "pinterestdownloader.com-1727612257.836546.jpg"]
    },
    {
        "id": 6,
        "name": "Jordan 1 Retro High University Blue",
        "description": "This is a description for shoe 6.",
        "price": "2,100",
        "images": ["s-l1600.webp", "/s-l960 (1).webp", "s-l960 (2).webp", "s-l960.webp"]
    },
    {
        "id": 7,
        "name": "Jordan 1 low bred toe",
        "description": "This is a description for shoe 6.",
        "price": "2,100",
        "images": ["IMG_9201.JPG", "IMG_9202.JPG", 'IMG_9203.JPG', 'IMG_9204.JPG']
    }
]

@app.route('/')
def home():
    return render_template('index.html', shoes=shoes)

@app.route('/product/<int:product_id>')
def product(product_id):
    
    product = next((shoe for shoe in shoes if shoe['id'] == product_id), None)

    
    if product is None:
        return "Product not found", 404

    
    return render_template('product.html', product=product)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        email = request.form['email']
        message = request.form['message']

    
        msg = Message('New Contact Message from LazeUp',
                      sender=email,
                      recipients=['punitsinha495@gmail.com'])  
        msg.body = f"Message from {email}:\n\n{message}"
        
        try:
            mail.send(msg)
            flash('Your message has been sent successfully!', 'success')
        except Exception as e:
            flash(f'Failed to send email. Error: {str(e)}', 'danger')

        return redirect(url_for('contact'))

    return render_template('contact.html')

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
